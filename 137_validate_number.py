'''
Create a function that takes three integer arguments (a, b, c) and returns the amount
of integers which are of equal value.
Examples
equal(3, 4, 3) 
➞ 2
equal(1, 1, 1) 
➞ 3
equal(3, 4, 1) 
➞ 0
Notes
Your function must return 0, 2 or 3.
'''

def validate_num(a,b,c):
    if a==b or b==c:
        return 3
    elif a==b or b==c or a==c:
        return 2
    else:
        return 0

print(validate_num(3,2,3))
print(validate_num(3,3,3))
print(validate_num(1,2,3))