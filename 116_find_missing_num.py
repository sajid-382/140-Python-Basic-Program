'''
Create a function that takes a list of numbers between 1 and 10 (excluding one
number) and returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) 
➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) 
➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) 
➞ 7
'''

def find_missing(lst):
    n= len(lst)+1
    sum_lst = sum(i for i in lst)
    '''for i in lst:
        sum_lst += i'''
    
    total_sum = n*(n+1)//2
    
    return total_sum-sum_lst

print("Missing Numb :", find_missing([1, 2, 3,4,6,7,8,9,10]))
print("Missing Numb :", find_missing([7, 2, 3, 6, 5, 9, 1, 4, 8]))