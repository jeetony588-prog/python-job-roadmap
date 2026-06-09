import json
import argparse

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ 已添加: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 暂无任务")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def delete(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"🗑️ 已删除: {removed}")
    else:
        print("❌ 编号无效")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Todo 命令行工具")
    subparsers = parser.add_subparsers(dest="command")

    p_add = subparsers.add_parser("add", help="添加任务")
    p_add.add_argument("task", type=str, help="任务内容")

    p_list = subparsers.add_parser("list", help="查看所有任务")

    p_del = subparsers.add_parser("del", help="删除任务")
    p_del.add_argument("index", type=int, help="任务编号")

    args = parser.parse_args()

    if args.command == "add":
        add(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "del":
        delete(args.index)
    else:
        parser.print_help()