import json


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


tasks = load_tasks()

while True:

    print("\n==== Todo ====")
    print("1 添加")
    print("2 查看")
    print("3 删除")
    print("4 退出")

    choice = input("选择：")

    if choice == "1":

        task = input("任务：")

        tasks.append(task)

        save_tasks(tasks)

        print("完成")

    elif choice == "2":

        for i, t in enumerate(tasks, 1):

            print(i, t)

    elif choice == "3":

        index = int(input("删除编号：")) - 1

        if 0 <= index < len(tasks):

            tasks.pop(index)

            save_tasks(tasks)

            print("已删除")

    elif choice == "4":

        break