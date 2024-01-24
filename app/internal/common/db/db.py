import os
import sqlite3

def get_db_connection():
    current_dir = os.path.dirname(__file__)
    db_path = os.path.join(current_dir, '../../../db/pycan.db')
    conn = sqlite3.connect(db_path)
    return conn

