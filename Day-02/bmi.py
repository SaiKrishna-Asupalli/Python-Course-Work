#Write a Python program that calculates a person's Body Mass Index (BMI) and categorizes it into different categories (underweight, normal weight, overweight, obese).
weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in meters: "))

bmi=weight/(height ** 2)
print(f"Your BMI is: {bmi:.1f}")

if bmi <18.5:
   print("Category: Underweight")
elif bmi >=18.5 and bmi<25.0:
   print("Category: Normal weight")
elif bmi>=25 and bmi<30.0:
   print("Category: Overweight")
else:
   print("Category: Obese")         
