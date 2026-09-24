'''
Create a function that takes a string and returns True or False, depending on whether
the characters are in order or not.
Examples
is_in_order("abc") 
➞ True
is_in_order("edabit") 
➞ False
is_in_order("123") 
➞ True
is_in_order("xyzz") 
➞ True
'''

def is_in_order(string):
    
    return string == ''.join(sorted(string))

print(is_in_order('abcd'))
print(is_in_order('abtd'))
print(is_in_order('abdst'))