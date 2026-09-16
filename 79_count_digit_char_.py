'''
Write a program that accepts a sentence and calculate the number of letters and
digits. Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

inp = input("Enter a sentence : ")
digit_count = 0
letter_count = 0
for x in inp:
    if x.isalpha():
        letter_count += 1
    elif x.isdigit():
        digit_count += 1
        
print("The no. of character present : ",letter_count)
print("The no. of Digit present : ",digit_count)