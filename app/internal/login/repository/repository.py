import hashlib
import sqlite3

from app.internal.common.db.db import get_db_connection


def verify_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 检索用户信息
        cursor.execute("SELECT passwd_hash, salt FROM users WHERE name = ?", (username,))
        user = cursor.fetchone()
        if user is None:
            return False

        # 验证密码
        passwd_hash, salt = user

        calc_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()
        return passwd_hash == calc_hash
    except sqlite3.Error as e:
        print(e)
        return False
    finally:
        conn.close()