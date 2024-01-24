import sqlite3

from app.internal.common.db.db import get_db_connection


def query_users_from_db(query_param):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if query_param:
            cursor.execute("SELECT name FROM users WHERE name LIKE ?", ('%' + query_param + '%',))
        else:
            cursor.execute("SELECT name FROM users")

        users = cursor.fetchall()
        return [{'name': user[0]} for user in users]
    except sqlite3.Error as e:
        print(e)
        return []
    finally:
        conn.close()