import os
import sqlite3

# def get_db_connection():
#
#     current_dir = os.path.dirname(__file__)
#     db_path = os.path.join(current_dir, '../../../db/pycan.db')
#     print()
#     conn = sqlite3.connect(db_path)
#     return conn
def get_db_connection():
    # 假设数据库存储在用户的文档目录下
    documents_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    db_path = os.path.join(documents_dir, "db", "pycan.db")
    print(db_path)
    # 确保存放数据库的目录存在
    # if not os.path.exists(os.path.dirname(db_path)):
    #     os.makedirs(os.path.dirname(db_path))

    # 连接到数据库
    conn = sqlite3.connect(db_path)
    return conn
