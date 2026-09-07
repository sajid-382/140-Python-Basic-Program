# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter string:")
no_pun=""
for char in string:
    if char not in punctuations:
        no_pun = no_pun + char

print("Punctuation removed : ", no_pun)
