import pandas as pd
from config.DB_operation import DatabaseTools
from config.config import conn
db_tool = DatabaseTools()
# 读取new_product 表
sql = "select * from product"
data = db_tool.pd_read_db(sql)
print(data.columns)

# 创建新的product表
# data = data[['chinese', 'English', 'CAS', 'appearance', '不做', '备注', 'ID']]
# data.rename(columns={'CAS':'cas','English':'name'}, inplace=True)
# data['chinese'] = data['chinese'].replace('	', '', regex=True)
# data['chinese'] = data['chinese'].replace('\xa0', '', regex=True)
# data['chinese'] = data['chinese'].replace('\t', '', regex=True)
data = data.groupby('cas').apply(lambda group: group.fillna(method='ffill'))
print(data.columns)
total_rows = len(data)
print(total_rows)
# 设置每个切割部分的最大行数
max_rows_per_part = 5000
# 计算切割的次数
num_parts = (total_rows + max_rows_per_part - 1) // max_rows_per_part
new_table = 'product'
for i in range(num_parts):
    start_idx = i * max_rows_per_part
    end_idx = (i + 1) * max_rows_per_part
    if end_idx > total_rows:
        end_idx = total_rows
    part_df = data.iloc[start_idx:end_idx]

    # 将数据存入sqlite数据库中
    part_df.to_sql(new_table, con=conn, if_exists='append', index=False)


# # 从sqlite读取数据,只取10条
sql2 = "select * from " + new_table
# #
new_data = pd.read_sql(sql2, conn)  # 完成数据库的查询读取到数据框dataframe 中
len_new_data = len(new_data.index)
print(total_rows, len_new_data)
# print(new_data)