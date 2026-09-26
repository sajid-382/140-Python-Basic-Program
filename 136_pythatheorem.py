'''
Create a function that validates whether three given integers form a Pythagorean
triplet. The sum of the squares of the two smallest integers must equal the square of
the largest number to be validated.
Examples
is_triplet(3, 4, 5) 
3² + 4² = 25
5² = 25
➞ True
is_triplet(13, 5, 12) 
➞ True
5² + 12² = 169
13² = 169
is_triplet(1, 2, 3) 
➞ False
1² + 2² = 5
3² = 9
Notes
Numbers may not be given in a sorted order.
'''
def pytha_theorom(a,b,c):
    sorted_numbers = sorted([a,b,c])
    
    return sorted_numbers[0]**2 + sorted_numbers[1]**2 == sorted_numbers[2]**2

print(pytha_theorom(13,12,5))
print(pytha_theorom(1,2,3))