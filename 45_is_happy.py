'''
Write a Python program to check if the given number is Happy Number.
Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
the number by the sum of the squares of its digits and continue the process, eventually
reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
is not a Happy Number.
For example:
'''

def is_happy(num):
    seen=set()
    
    while num != 1 and num not in seen:
        seen.add(num)
        num=sum(int(i)**2 for i in str(num))
    
    return num == 1

number = int(input("Enter any +ve number :"))

if is_happy(number):
    print('The number {} is a Happy number '.format(number))
else:
    print('The number {} is not a Happy number '.format(number))