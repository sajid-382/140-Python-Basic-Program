'''
The "Reverser" takes a string as input and returns that string in reverse order, with
the opposite case.
Examples
reverse("Hello World") 
reverse("ReVeRsE") 
➞ "DLROw OLLEh"
➞ "eSrEvEr"
reverse("Radar") 
➞ "RADAr"
'''
def reverse_str(string):
    result = string[::-1].swapcase()
    return result

print(reverse_str('sajiD'))