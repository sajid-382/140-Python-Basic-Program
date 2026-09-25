'''
Create a function that returns the mean of all digits.
Examples
mean(42) 
➞ 3
mean(12345) 
➞ 3
mean(666) 
➞ 6
Notes:
The mean of all digits is the sum of digits / how many digits there are (e.g. mean
of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer.
'''

def mean(num):
    num_str = str(num)
    num_digit = len(num_str)
    
    sum_digit = sum(int(n) for n in num_str)
    
    digit_mean = sum_digit/num_digit
    
    return int(digit_mean)

print(mean(666))
print(mean(124536))
print(mean(136))

