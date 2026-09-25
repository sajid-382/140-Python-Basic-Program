'''
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) 
setify([4, 4, 4, 4]) 
➞ [1, 3, 5]
➞ [4]
setify([5, 7, 8, 9, 10, 15]) 
➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) 
➞ [1, 2, 3]
'''
# Method - 1
def setify(lst):
    unique_set = set(sorted(lst))
    # Convert the set back to a list and return it
    return list(unique_set)

print(setify([4, 4, 4, 4]))

# Method -2
def remove_duplicates(lst):
    new_list =[]
    
    for n in lst:
        if n not in new_list:
            new_list.append(n)
    
    return sorted(new_list)

print(remove_duplicates([1, 3, 3, 5, 5]))
print(remove_duplicates([5, 7, 8, 9, 10, 15]))