"""
a sample of create view with two tables
"""

from config.DB_operation import DatabaseTools
db = DatabaseTools()

create_view_query = """
CREATE VIEW test_view AS
SELECT history.code, history.price, xqhistory.code, xqhistory.stock_name
FROM history
JOIN xqhistory ON history.code = xqhistory.code
"""

db.execute_sql(create_view_query)