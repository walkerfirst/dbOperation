import time
import pandas as pd
from config.DB_operation import DatabaseTools
# import requests

def get_data(url, x):
    # 获取网页的table，得到一个list，如果中文乱码需要解码
    tables_list = pd.read_html(url, encoding='utf-8')
    '''
        # 如何知道网页的编码呢？如下方式:
        response = requests.get(url)
        print(response.encoding)
    '''
    # list 有可能不止一个dataframe，x为第几个table
    tables = tables_list[x]
    return tables

def process_data(keyword):
    # 测试一下其他网站
    url = r"https://www.chemicalbook.com/Search.aspx?keyword={1}"
    url = url.replace('{1}', str(keyword))
    url = url.replace(" ", "%20")
    # print(url)
    data = get_data(url, x=0)
    # print(type(data))
    s = data[0].loc[0]

    # 首先使用空格分隔符进行分割
    _parts = s.split('  ')
    # print(_parts)
    # 删除': '
    parts = [x.replace('：', '') for x in _parts][:17]
    print(parts)
    if "CAS" in parts:
        index = parts.index("CAS")
        cas = str(parts[index+1])
    else:
        cas = ""
    if '中文名称' in parts:
        index2 = parts.index('中文名称')
        chinese = str(parts[index2+1])
    else:
        chinese = ''
    return cas,chinese


def fill_cas():
    sql = 'select ID,English,CAS,chinese,不推荐,备注 from new_product where CAS IS NULL'
    data = DatabaseTools().read_db(sql)
    print('总共空数据为：',len(data))
    for item in data:
        id = item[0]
        name = item[1]
        # print(item)
        chinese_db = item[3]

        if item[4] == 1 and item[5] is None:
            del_url = "DELETE FROM new_product WHERE ID = %s" % id
            DatabaseTools().execute_sql(del_url)
        else:
            try:
                cas,chinese = process_data(name)
                print(cas)
                if '-' in cas:
                    print('cas=',cas)
                    print(name)

                    if chinese != 'MF' and chinese_db is None and "'" not in chinese:
                        print('中文名：',chinese_db)
                        update_url2 = "UPDATE new_product SET chinese = '" + chinese + "', CAS = '"+ cas + "' WHERE ID = %s" %id
                        if "'" in update_url2:
                            # 如果含有，替换为其他字符串或空字符串
                            update_url2 = update_url2.replace("'\''", "''")
                        print(update_url2)
                        DatabaseTools().execute_sql(update_url2)

                    else:
                        update_url = "UPDATE new_product SET CAS = '" + cas + "' WHERE ID = %s" % id
                        print(update_url)
                        DatabaseTools().execute_sql(update_url)

                else:
                    del_url = "DELETE FROM new_product WHERE ID = %s" %id
                    DatabaseTools().execute_sql(del_url)
                    print('del',name)
                time.sleep(0.4)
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    fill_cas()