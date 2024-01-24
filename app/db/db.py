import sqlite3

DB_PATH = 'pycan.db'

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    UNIQUE (username)
);
''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS permissions (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            passwd_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            permission_id INTEGER,
            status TEXT NOT NULL CHECK(status IN ('active', 'suspended', 'deleted')),
            createtime TEXT NOT NULL,
            updatetime TEXT NOT NULL,
            FOREIGN KEY (permission_id) REFERENCES permissions (id)
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully.")
