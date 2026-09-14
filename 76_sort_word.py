'''
Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world
'''



words = map(str, input("Enter word sepereted by ',' :").split(','))

sorted_word= sorted(words)

sequence = ','.join(sorted_word)
print("Soerted words :", sequence)