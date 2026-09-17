'''
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically. Suppose the following input is
supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.

Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

input_word = input("Enter swquence of word : ").split()

word_frq = {}

for word in input_word:
    word = word.strip('.,?')
    word = word.lower()
    
    if word in word_frq:
        word_frq[word] += 1
    else:
        word_frq[word] = 1


for key,value in word_frq.items():
    print(f"{key} = {value}")