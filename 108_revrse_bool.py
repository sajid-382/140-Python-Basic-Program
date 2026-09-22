'''
Create a function that reverses a boolean value and returns the string "boolean
expected" if another variable type is given.
Examples
reverse(True) 
➞ False
reverse(False) 
➞ True
reverse(0) 
➞ "boolean expected"
reverse(None) 
➞ "boolean expected"
'''
def reverse_bool(value):
    if isinstance(value,bool):
        return not value
    else:
        return "Boolean expected"
    
print(reverse_bool(True))
print(reverse_bool(False))
print(reverse_bool(0))