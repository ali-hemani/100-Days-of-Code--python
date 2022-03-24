# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight) / (float(height) ** 2)
if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal weight")
elif BMI < 30:
    print("Overweight")
elif BMI < 35:
    print("Obese")
else:
    print("clinically obese")
