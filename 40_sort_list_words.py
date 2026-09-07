# Program to sort alphabetically the words form a string provided by the list input

string = input("Enter words :")

words = [word.capitalize() for word in string.split()]

for word in words:
    print(word)