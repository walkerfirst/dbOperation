"""
将access 数据库的某个表数据整体转移到 sqlite中去
"""
from access_db import read_access_db
import pandas as pd
from config.config import conn as DB_CONN



def TransferData(table_name):
    # 从access 中读取buy表数据，并转换成dataframe
    sql = 'select * from ' + table_name
    print(sql)
    data = read_access_db(sql)

    # 删除name列中的不间断空白符
    # data['CAS'] = data['CAS'].replace('\xa0', '', regex=True)
    # data['CAS'] = data['CAS'].replace('\t', '', regex=True)
    # data['CAS'] = data['CAS'].replace(' ', '', regex=True)
    # data['supplier'] = data['supplier'].replace(' ', '', regex=True)
    # data['supplier'] = data['supplier'].replace('\t', '', regex=True)
    # data['supplier'] = data['supplier'].replace('\xa0', '', regex=True)
    # data['产品名称'] = data['产品名称'].replace(' ', '', regex=True)
    # data['产品名称'] = data['产品名称'].replace('\t', '', regex=True)
    # data['产品名称'] = data['产品名称'].replace('\xa0', '', regex=True)

    # supplier_data = data[['CAS','supplier','不推荐','备注','chinese']]
    # 获取 DataFrame 的总行数
    total_rows = len(data)
    print(total_rows)
    # 设置每个切割部分的最大行数
    max_rows_per_part = 5000
    # 计算切割的次数
    num_parts = (total_rows + max_rows_per_part - 1) // max_rows_per_part

    for i in range(num_parts):
        start_idx = i * max_rows_per_part
        end_idx = (i + 1) * max_rows_per_part
        if end_idx > total_rows:
            end_idx = total_rows
        print(start_idx,end_idx)
        part_df = data.iloc[start_idx:end_idx]
        print(part_df[:2])
        print(part_df.columns)
        # 将数据存入sqlite数据库中
        part_df.to_sql(table_name,con=DB_CONN,if_exists='append',index=False)


    # 将数据存入sqlite数据库中
    # supplier_data.head(1).to_sql(table_name,con=DB_CONN,if_exists='append',index=False)
    #
    # # 从sqlite读取数据,只取10条
    sql2 = "select * from " + table_name
    # #
    new_data = pd.read_sql(sql2,DB_CONN)#完成数据库的查询读取到数据框dataframe 中
    len_new_data = len(new_data.index)
    print(total_rows,len_new_data)
    # print(new_data)

if __name__ == '__main__':
    TransferData('跟单进程')