from config.config import conn
import pandas as pd
def save(df,table_name):
    data = df
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
        print(start_idx, end_idx)
        part_df = data.iloc[start_idx:end_idx]
        print(part_df[:2])
        print(part_df.columns)
        # 将数据存入sqlite数据库中
        part_df.to_sql(table_name, con=conn, if_exists='append', index=False)

    # 将数据存入sqlite数据库中
    # supplier_data.head(1).to_sql(table_name,con=DB_CONN,if_exists='append',index=False)
    #
    # # 从sqlite读取数据,只取10条
    sql2 = "select * from " + table_name
    # #
    new_data = pd.read_sql(sql2, conn)  # 完成数据库的查询读取到数据框dataframe 中
    len_new_data = len(new_data.index)
    print(total_rows, len_new_data)