'''
Write a Python Program to Check Armstrong Number?
Armstrong Number:
It is a number that is equal to the sum of its own digits, each raised to a power equal to the
number of digits in the number.
For example, let's consider the number 153:
It has three digits (1, 5, and 3).
If we calculate 
 1^3 + 5^3 + 3^3 , we get 1 +125+27, which is equal to 153.
So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
of the number of digits in the number.

Another example is 9474:
It has four digits (9, 4, 7, and 4).
If we calculate 9^4 + 4^4 + 7^4 + 4^4 , we get 6561 + 256 +2401 +256, which is equal to 9474


'''

num = int(input("Enter a number : "))

num_str=str(num)
num_digit=len(num_str)
sum_of_square=0
temp_num=num

while temp_num>0:
    digit=temp_num%10
    sum_of_square=sum_of_square+digit**num_digit
    temp_num //=10
if sum_of_square== num:
    print(f"the given number {num} is Armstrong number")
else:
    print(f"the given number {num} is not Armstrong number")