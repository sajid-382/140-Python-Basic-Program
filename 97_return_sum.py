'''
Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) 
➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) 
➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) 
➞ 18
# 3 + 6 + 9 = 18
'''

def sum_of(a,b,c):
    if c > b:
        return f"No number between {a} and {b} can be evenly divided by {c}"
    
    summ = 0
    for num in range(a, b+1):
        if num % c == 0:
            summ = summ + num
    
    return summ

a,b,c = map(int, input("Enter the value of a , b and c seperate by ',' :").split(','))

print("Sum = ", sum_of(a,b,c))