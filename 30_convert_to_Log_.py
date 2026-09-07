# Write a Python Program to calculate the natural logarithm of any number.

import math

number = float(input("enter anumber to convert logarithm :"))

if number <=0:
    print("Please enter positive number")
else:
    result=math.log(number)
    print(f"The natural logarithm of {number} is: {result}")