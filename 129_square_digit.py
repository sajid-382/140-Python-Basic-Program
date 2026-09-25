'''
Create a function that squares every digit of a number.
Examples
square_digits(9119) 
➞ 811181
square_digits(2483) 
➞ 416649
square_digits(3212) 
➞ 9414
Notes
The function receives an integer and must return an integer.
'''
def square_digits(num):
    num_str = str(num)
    
    square_of_digit = ""
    
    for digit in num_str:
        square_digit = int(digit)**2
        square_of_digit += str(square_digit)
        
    return  int(square_of_digit)

print(square_digits(3223))
print(square_digits(4214))
print(square_digits(1234))