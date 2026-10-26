p=float(input("Principal: "))
r=float(input("Rate %: "))
t=float(input("Years: "))
amt = p*(1+r/100)**t
print(f"Total Amount: {amt:.2f}")
