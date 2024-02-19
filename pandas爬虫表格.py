"""
用pandas 下载网页上的表格，测试可以用
"""
import pandas as pd
import time
from config.database import db_new_chemical
# from util.stock_util import save_data_to_db

def get_data(url,x):

     # 获取网页的table，得到一个list，如果中文乱码需要解码
    tables_list = pd.read_html(url,encoding='utf-8')
    '''
        # 如何知道网页的编码呢？如下方式:
        response = requests.get(url)
        print(response.encoding)
    '''
    # list 有可能不止一个dataframe，x为第几个table
    tables = tables_list[x]
    return tables

def save_to_excel(data,path):
    data.to_excel(path)

def ChemicalsBook ():
    # 每翻一页URL的数字会递增100，通过这个规律，可以遍历出想要的URL_list
    url = "https://www.chemicalbook.com/ProductCASList_20_{1}.htm"

    for j in range(0, 49201, 1000):
        for i in range(j,j+1000,100):
            # print(str(i))
            # print(url)
            try:
                data = get_data(url.replace('{1}', str(i)),x=0)
                # print(data.columns)

                # if i == 30000:
                #     time.sleep(100)
            except Exception as e:
                print(e,"获取错误，序号为：", i)
                return  # 退出整个for循环，如果为break只退出一个
            # print(data)

            try:
                if not data.empty:
                    save_data_to_db(data, 'product')
                    print("已经存取编号为：",i)
            except Exception as e:
                print(e,"存取错误，序号为：%s, j为：%s", (i,j))
            # time.sleep(0.5)



if __name__ ==  '__main__':

    # 获取chemicalbook表product中的 product
    # ChemicalsBook()
    # collection = DB_CONN['product']
    # cursor = collection.find({'CAS': '20-73-5'},projection={'_id': False})
    # df = pd.DataFrame(list(cursor))
    # print(df)

    #测试一下其他网站
    url = "https://www.chemicalbook.com/Search.aspx?keyword=7-Aminoheptanoic acid"
    url = url.replace(" ", "%20")
    print(url)
    data = get_data(url,x=0)
    print(type(data))
    s = data[0].loc[0]

    separators = [":", "  "]

    # 首先使用第二个分隔符进行分割
    _parts = s.split(separators[1])
    parts = [x.replace('：', '') for x in _parts]
    print(parts)
    parts.pop(0)
    parts.pop(-1)
    # print(parts)

    # 初始化结果字典
    result_dict = {}

    # 对每个部分使用第一个分隔符进行分割，并构建字典
    result_dict = {}
    for i in range(0, len(parts), 2):
        key = parts[i].strip()
        value = parts[i + 1].strip()
        result_dict[key] = value
    # 输出字典
    print(result_dict)