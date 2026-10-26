from datetime import date
y,m,d = map(int, input("DOB YYYY-MM-DD: ").split("-"))
today = date.today()
age = today.year - y - ((today.month, today.day) < (m,d))
print(f"Age: {age} years")
