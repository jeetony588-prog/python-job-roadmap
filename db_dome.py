import sqlite3

# 1. 连接数据库
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# 2. 创建表（如果不存在）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
''')

# 3. 插入数据
cursor.execute("INSERT INTO tasks (name) VALUES (?)", ("学习SQL",))
conn.commit()

# 4. 查询
cursor.execute("SELECT * FROM tasks")
print(cursor.fetchall())

# 5. 更新
cursor.execute("UPDATE tasks SET done = 1 WHERE id = 1")
conn.commit()

# 6. 再查询确认
cursor.execute("SELECT * FROM tasks")
print(cursor.fetchall())

# 7. 最后才关闭连接（全部操作完成后）
conn.close()