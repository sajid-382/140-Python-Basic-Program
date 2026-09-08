'''
Write a Python program to determine whether the given number is a Harshad
Number.

A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
In other words, a number is considered a Harshad number if it can be evenly divided by the
sum of its own digits.
For example:

18 is a Harshad number because 1 +8 =9, and 18 is divisible by 9
4 +2 =6 42 is a Harshad number because, and 42 is not divisible by 6.
'''

def is_harshad(num):
    sum_of_digit = sum(int(i) for i in str(num))
    
    return num % sum_of_digit == 0

num = int(input("Enter a number to check harshad number :"))

if is_harshad(num):
    print(f"the number {num} is a Harshad Number.")
else:
    print(f"the number {num} is not a Harshad Number.")
