'''
Q. Write a Python program to solve quadratic equation.

The standard form of a quadratic equation is:

ax^2 +bx+c=0
where
a, b and c are real numbers and
a ≠ 0
The solutions of this quadratic equation is given by:

(-b ± (b^2 - 4ac )/(2a)
)1/
'''

import math

a = float(input("Enter valueof a :"))
b = float(input("Enter valueof b :"))
c = float(input("Enter valueof c :"))

if a==0:
    print("Value of a can't be zero ")
    exit()

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b - math.sqrt(discriminant))/(2*a)
    root2 = (-b + math.sqrt(discriminant))/(2*a)
    print("Roots are real and different :")
    print("Root 1 = ",root1)
    print("Root 2 = ",root2)
elif discriminant==0:
    root=-b/(2*a)
    print("Roots are real and equal:")
    print("Root =",root)
else:
    realPart=-b/(2*a)
    imaginaryPart = math.sqrt(abs(discriminant))/(2*a)
    print("Roots are imaginary and different :")
    print(f" Root 1 = {realPart} + {imaginaryPart}")
    print(f" Root 2 = {realPart} - {imaginaryPart}")