import sqlite3,pyodbc
import os
# 获取当前路径
path = os.getcwd()
# print(path)
if 'config' in path:
    path = path.replace("\\config","")
    # print(path)
# SQLite db 数据库
file_record = path + '\db\stock_record.db'
db_record = sqlite3.connect(file_record) #如果路径里面没有这个数据库，会自动创建

# Access db 数据库
# odbc_file = path + '\db\product.mdb'  # 存放股票的数据库文件
# mdb_product = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + odbc_file + ";Uid=;Pwd=;")

# file_product = path + '\db\lib.db'
# db_product = sqlite3.connect(file_product)

# Pharmasi access 数据库
# chemical_db_path = path + '\db\chemical.accdb'  # 存放chemical 订单的数据库文件
# chemical_db = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + chemical_db_path + ";Uid=;Pwd=jh2005;")

new_chemical_file = path + '\db\chemical.db'
db_new_chemical = sqlite3.connect(new_chemical_file)