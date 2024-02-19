from config.DB_operation import DatabaseTools
from config.config import conn
dbtool = DatabaseTools()
sql = 'select * from new_product'
data = dbtool.pd_read_db(sql)
data['English'] = data['English'].replace('（', '(', regex=True)
data['English'] = data['English'].replace('）', ')', regex=True)
data['English'] = data['English'].replace('’', '\'', regex=True)

_df = data.groupby('English').apply(lambda group: group.fillna(method='ffill'))


_df.to_sql('new_product2',con=conn,if_exists='append',index=False)