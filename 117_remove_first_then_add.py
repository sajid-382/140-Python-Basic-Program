'''
Write a function that takes a list and a number as arguments. Add the number to the
end of the list, then remove the first element of the list. The function should then
return the updated list.
Examples
next_in_line([5, 6, 7, 8, 9], 1) 
➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) 
➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42 ], 6) 
➞ [10, 20, 42, 6]
next_in_line([], 6) 
➞ "No list has been selected"
'''
def add_num(lst,n):
    if lst:
        lst.pop(0)
        lst.append(n)
        return lst
    else:
        return "No list has been selected"

print(add_num([6,3,23,17,10],7))
print(add_num([1,20,10,42],6))