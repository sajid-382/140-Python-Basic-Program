'''
Please write a program using generator to print the numbers which can be divisible
by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
'''

def divisible_5_7_(n):
    for num in range(n):
        if num % 5 == 0 and num % 7 == 0:
            yield num

try:
    n = int(input("Enter number for range :"))
    result = divisible_5_7_(n)
    print(type(result))
    print(','.join(map(str,result)))
except ValueError :
    print("Please enter integer value only...")