weight = float(input("Weight kg: "))
height_cm = float(input("Height cm: "))
height_m = height_cm/100
bmi = weight/(height_m**2)
print(f"Your BMI is {round(bmi,1)}")
if bmi<18.5: print("Underweight")
elif bmi<25: print("Normal")
elif bmi<30: print("Overweight")
else: print("Obese")
