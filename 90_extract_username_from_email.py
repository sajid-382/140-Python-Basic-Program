'''
Assuming that we have some email addresses in the
"
username@companyname.com
 (mailto:username@companyname.com)" format,
please write program to print the user name of a given email address. Both user
names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
 (mailto:john@google.com)
Then, the output of the program should be:
john
'''

def extract_user(email):
    parts = email.split('@')
    
    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email id"

try:
    email = input("Enter email id :")
    result = extract_user(email)
    print(result)

except ValueError:
    print("Please enter valid email id.........")