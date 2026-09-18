'''
Program 88
Please write a program using generator to print the even numbers between 0 and n in
comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
'''

def even_num(n):
    
    for num in range(n+1):
        if num % 2 == 0:
            yield num

try:
    n = int(input("Enter a number for range :"))
    even_number = even_num(n)
    print(','.join(map(str,even_number)))

except ValueError as e:
    print("Please enter only integer value...",e)