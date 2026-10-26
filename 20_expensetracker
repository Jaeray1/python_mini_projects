expenses = []
while True:
    print("\n1.Add 2.View 3.Total 4.Exit")
    ch=input("Choice: ")
    if ch=='1':
        amt=float(input("Amount: "))
        cat=input("Category: ")
        expenses.append([amt,cat])
    elif ch=='2': print(expenses)
    elif ch=='3': print(f"Total: {sum(e[0] for e in expenses)}")
    else: break
