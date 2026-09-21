'''
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) 
➞ outputs 1
print(middle) 
➞ outputs [2, 3, 4, 5]
print(last) 
➞ outputs 6
'''
writeyourcodehere = [1,2,3,4,5,6]

# Unpack the list into variables
first, *middle, last = writeyourcodehere

print(first)
print(middle)
print(last)