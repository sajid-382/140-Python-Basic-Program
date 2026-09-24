'''
Create a function that takes a number as an argument and returns True or False
depending on whether the number is symmetrical or not. A number is symmetrical
when it is the same as its reverse.
Examples
is_symmetrical(7227) 
➞ True
is_symmetrical(12567) 
➞ False
is_symmetrical(44444444) 
➞ True
is_symmetrical(9939) 
➞ False
is_symmetrical(1112111) 
➞ True
'''

def is_symmetric(num):
    str_num = str(num)
    
    return str_num == str_num[::-1]

print(is_symmetric(11011))
print(is_symmetric(11242))