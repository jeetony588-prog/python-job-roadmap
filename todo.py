tasks = []

while True:
    print("\n==== Todo ====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 退出")

    choice = input("请选择：")

    if choice == "1":
        task = input("输入任务：")
        tasks.append(task)

        with open("tasks.txt", "a", encoding="utf-8") as f:
            f.write(task + "\n")

        print("已保存")

    elif choice == "2":
        print("\n任务列表：")

        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                data = f.readlines()

            for i, task in enumerate(data, 1):
                print(f"{i}. {task.strip()}")

        except:
            print("暂无任务")

    elif choice == "3":
        print("退出")
        break

    else:
        print("输入错误")