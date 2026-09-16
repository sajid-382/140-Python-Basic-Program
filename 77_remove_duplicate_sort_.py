'''
Program 77
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

# Accept input from the user
input_sequence = input("Enter a sequence of whitespace-separated words : ")

sequence = set(input_sequence.split())

sorted_sequence  = sorted(sequence)

print("Soerted sequence and removed duplicate : "," ".join(sorted_sequence))