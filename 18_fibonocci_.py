'''
Write a Python Program to Print the Fibonacci sequence.

Fibonacci sequence:
The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
the next number is obtained by adding the previous two numbers. This pattern continues
indefinitely, generating a sequence that looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Mathematically, the Fibonacci sequence can be defined using the following recurrence
relation:
f(0) = 0 f(1) = 1 f(n) = f(n-1)+f(n-2)forn > 1
'''

num=int(input("Enter a number : "))

num1=0
num2=1
print(num1,end=' ')
print(num2,end=' ')

for i in range(0,num):
    result=num1+num2
    print(result, end=' ')
    num1=num2
    num2=result
