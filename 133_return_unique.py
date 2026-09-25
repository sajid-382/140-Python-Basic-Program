'''
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) 
➞ 7
unique([0, 0, 0.77, 0, 0]) 
➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) 
Notes
➞ 0
Test cases will always have exactly one unique number while all others are the same.
'''

def unic_num(numbers):
    
    num_dict = {}
    
    for n in numbers:
        if n in num_dict:
            num_dict[n] += 1
        else:
            num_dict[n]=1
    
    for n, count in num_dict.items():
        if count == 1:
            return n
        
print(unic_num([0, 1, 1, 1, 1, 1, 1, 1]))
print(unic_num([3, 3, 3, 7, 3, 3]))