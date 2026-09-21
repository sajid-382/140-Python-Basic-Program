'''
Create a function that takes a string and returns a string in which each character is
repeated once.
Examples
double_char("String") 
➞ "SSttrriinngg"
double_char("Hello World!") 
➞ "HHeelllloo WWoorrlldd!!"
double char("1234! ") 
➞ "11223344!! "
'''
def double_char(string):
    doubled_char = ""
    
    for char in string:
        doubled_char += char*2
    return doubled_char

print(double_char("Hello World!"))
print(double_char("1234!_"))