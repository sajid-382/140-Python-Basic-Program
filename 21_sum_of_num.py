'''
Write a Python Program to Find the Sum of Natural Numbers.
Natural numbers are a set of positive integers that are used to count and order objects.
They are the numbers that typically start from 1 and continue indefinitely, including all the
whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
denoted as "N" and can be expressed as:
N =1,2,3,4,5,6,7,8,...

'''


num=int(input("Enter number want to sum up to :"))

sum = 0
for x in range(1,num+1):
    sum += x

print(f"sum of first {num} natural number is = {sum}")