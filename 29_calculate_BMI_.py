'''
Write a Python Program to calculate your Body Mass Index.
Body Mass Index (BMI) is a measure of body fat based on an individual's weight and
height. It is commonly used as a screening tool to categorize individuals into different weight
status categories, such as underweight, normal weight, overweight, and obesity.
The BMI is calculated using the following formula:
BMI= weight/(hight)^2

'''

def calculate_bmi(h,w):
    #bmi = w/(h**2)
    return round((w / h**2),2)

hight=float(input("Enter hight of boddy :"))
weight=float(input("Enter weight of boddy :"))

bmi=calculate_bmi(hight,weight)

print("Your BMI =",bmi)
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")