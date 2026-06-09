import sqlite3
import argparse

DB_FILE = "todo.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                done INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

def add_task(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
        conn.commit()
        print(f"✅ 已添加: {name}")

def list_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, done FROM tasks")
        rows = cursor.fetchall()
        if not rows:
            print("📭 暂无任务")
        else:
            for row in rows:
                status = "✅" if row[2] else "⏳"
                print(f"{row[0]}. {status} {row[1]}")

def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print("❌ 未找到该编号")
        else:
            conn.commit()
            print(f"🗑️ 已删除编号 {task_id}")

def complete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print("❌ 未找到该编号")
        else:
            conn.commit()
            print(f"🎉 已完成编号 {task_id}")

if __name__ == "__main__":
    init_db()  # 确保表存在

    parser = argparse.ArgumentParser(description="Todo 数据库版")
    subparsers = parser.add_subparsers(dest="command")

    p_add = subparsers.add_parser("add", help="添加任务")
    p_add.add_argument("name", type=str, help="任务内容")

    p_list = subparsers.add_parser("list", help="列出所有任务")

    p_del = subparsers.add_parser("del", help="删除任务")
    p_del.add_argument("id", type=int, help="任务编号")

    p_done = subparsers.add_parser("done", help="标记任务为完成")
    p_done.add_argument("id", type=int, help="任务编号")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.name)
    elif args.command == "list":
        list_tasks()
    elif args.command == "del":
        delete_task(args.id)
    elif args.command == "done":
        complete_task(args.id)
    else:
        parser.print_help()