from config.DB_operation import DatabaseTools
from config.config import conn
db_tool = DatabaseTools()
import re

# quotaton data
sql = "select id,cas,name from orders where cas IS NOT NULL"
data = db_tool.pd_read_db(sql)
cas_list = list(set(list(data['cas'])))
for cas in cas_list:
    if cas != '':
        sql_product = "select id,cas,name from product where cas = '" + cas + "' "
        product_data = db_tool.read_db(sql_product)
        if len(product_data) > 0:
            quo_name = str(list(data[data['cas'] == cas]['name'])[0])
            if not re.search("[\u4e00-\u9fa5]", quo_name):
                if "'" not in quo_name:
                    for row in product_data:
                        if quo_name != str(row[2]):
                            print('orders_name', quo_name)
                            print('pro_name', row[2])
                            update_sql = "UPDATE product SET name= '" + quo_name + "' WHERE id = %s" %row[0]
                            print(update_sql)
                            db_tool.execute_sql(update_sql)