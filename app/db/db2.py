import sqlite3

# 创建或连接到SQLite数据库
conn = sqlite3.connect('rbac_example.db')
cursor = conn.cursor()

# 创建用户表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        full_name TEXT
    )
''')

# 创建角色表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roles (
        role_id INTEGER PRIMARY KEY,
        role_name TEXT NOT NULL UNIQUE,
        description TEXT
    )
''')

# 创建权限表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Permissions (
        permission_id INTEGER PRIMARY KEY,
        permission_name TEXT NOT NULL UNIQUE,
        description TEXT
    )
''')

# 创建角色-权限关联表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Role_Permissions (
        role_permission_id INTEGER PRIMARY KEY,
        role_id INTEGER,
        permission_id INTEGER
    )
''')

# 创建用户-角色关联表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User_Roles (
        user_role_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        role_id INTEGER
    )
''')

# 插入示例数据
cursor.execute('''
    INSERT INTO Users (username, password_hash, full_name) VALUES (?, ?, ?)
''', ('user1', 'password_hash1', 'User One'))

cursor.execute('''
    INSERT INTO Roles (role_name, description) VALUES (?, ?)
''', ('admin', 'Admin Role'))

cursor.execute('''
    INSERT INTO Permissions (permission_name, description) VALUES (?, ?)
''', ('read_data', 'Read Data Permission'))

cursor.execute('''
    INSERT INTO Role_Permissions (role_id, permission_id) VALUES (?, ?)
''', (1, 1))

cursor.execute('''
    INSERT INTO User_Roles (user_id, role_id) VALUES (?, ?)
''', (1, 1))

# 提交更改并关闭连接
conn.commit()
conn.close()

# 查询示例数据
conn = sqlite3.connect('rbac_example.db')
cursor = conn.cursor()

# 查询用户信息
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
print("Users:")
for user in users:
    print(user)

# 查询角色信息
cursor.execute('SELECT * FROM Roles')
roles = cursor.fetchall()
print("\nRoles:")
for role in roles:
    print(role)

# 查询权限信息
cursor.execute('SELECT * FROM Permissions')
permissions = cursor.fetchall()
print("\nPermissions:")
for permission in permissions:
    print(permission)

# 查询角色-权限关联信息
cursor.execute('SELECT * FROM Role_Permissions')
role_permissions = cursor.fetchall()
print("\nRole_Permissions:")
for role_permission in role_permissions:
    print(role_permission)

# 查询用户-角色关联信息
cursor.execute('SELECT * FROM User_Roles')
user_roles = cursor.fetchall()
print("\nUser_Roles:")
for user_role in user_roles:
    print(user_role)

# 关闭连接
conn.close()
