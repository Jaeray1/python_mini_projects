tasks = []
while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    c = input("Choice: ")
    if c=='1': tasks.append(input("Task: "))
    elif c=='2': print(tasks if tasks else "Empty")
    elif c=='3':
        for i,t in enumerate(tasks): print(i, t)
        tasks.pop(int(input("Index to delete: ")))
    else: break
