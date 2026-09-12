import re
def check_special_char(my_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    
    if re.search(pattern,my_str):
        return True
    else:
        return False
my_str = input("Enter any string :")

if check_special_char(my_str):
    print("String contains special character")
else:
    print("String not contains any hespecial character")