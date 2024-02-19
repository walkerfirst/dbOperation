import pandas as pd
from config.DB_operation import DatabaseTools
from save_df_to_db import save
# from config.config import conn
db_tool = DatabaseTools()
# excel = pd.read_excel(r"C:\Users\Administrator\project\dbOperations\db\quotation.xls")
# print(excel)
# print(excel.columns)
# 读取new_product 表
sql = "select * from orders"
df = db_tool.pd_read_db(sql)
df['month'] = pd.to_datetime(df['month'])
# print(df[['month','cas','create_date']].head(10))
# print(df[['month','cas','create_date']].tail(10))
# print(type(df['month'][0]))
# excel = excel.drop_duplicates(subset=['cas'], keep='first')
# print(excel.head(20))
# merged_df = pd.merge(df, excel, on='cas', how='left')
# print(merged_df.columns)
# print(merged_df.head(10))
#
# merged_df['english'] = merged_df['english'].fillna(merged_df['name'])
# print(merged_df.columns)
# merged_df['名称'] = merged_df['名称'].fillna(merged_df['chinese'])
# merged_df['物理性状'] = merged_df['物理性状'].fillna(merged_df['appearance'])
#
# new_df = merged_df[['cas', 'remark', 'ignore', 'id', '名称','english', 'HS', '物理性状']]
# new_df.rename(columns={'名称': 'chinese', 'english': 'name', '物理性状': 'appearance'}, inplace=True)
# print(new_df.columns)
#
# 按列 'A' 进行分组，并对其他列进行字符串的合并
# merged_df = data.groupby('name', as_index=False).agg(lambda x: ', '.join(x))

# # merged_df = pd.merge(data, sum, on='order_no', how='left')
# df['order_no'] = df['order_no'].astype(int)
# # 找出表1中不存在但表2中存在的行
# missing_rows = sum[~sum['order_no'].isin(df['order_no'])]
#
# # 将找出的行添加到表1中
# new_df = pd.concat([df, missing_rows], ignore_index=True)
# print(df.columns)
# new_df = df[['id','report', 'remark', 'date', 'unit_cn', 'supplier', 'qty',
#        'cas', 'content', 'delivery']]
save(df,'orders_new')
