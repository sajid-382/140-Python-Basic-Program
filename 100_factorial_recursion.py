'''
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) 
➞ 120
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5 :",factorial(5))