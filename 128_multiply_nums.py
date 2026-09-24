'''
Given a string of numbers separated by a comma and space, return the product of
the numbers.
Examples
multiply_nums("2, 3") 
➞ 6
multiply_nums("1, 2, 3, 4") 
➞ 24
multiply_nums("54, 75, 453, 0") 
➞ 0
multiply_nums("10, -2") 
➞ -20
'''
def product_nums(str_num):
    
    nums = [int(num) for num in str_num.split(', ')]
    result = 1
    
    for num in nums:
        result *= num
    
    return result

print(product_nums("54, 75, 453, 0"))
print(product_nums("10, -2"))
print(product_nums("1, 2, 3, 4"))