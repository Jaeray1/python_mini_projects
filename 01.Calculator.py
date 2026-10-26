a = float(input("Enter 1st number: "))
op = input("Operator (+,-,*,/): ")
b = float(input("Enter 2nd number: "))

if op == '+': print(f"Result: {a+b}")
elif op == '-': print(f"Result: {a-b}")
elif op == '*': print(f"Result: {a*b}")
elif op == '/': print(f"Result: {a/b}" if b!=0 else "Can't divide by 0")
