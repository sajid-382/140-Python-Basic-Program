'''
An isogram is a word that has no duplicate letters. Create a function that takes a
string and returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") 
➞ True
is_isogram("PasSword") 
➞ False- Not case sensitive.
is_isogram("Consecutive") 
➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings.
'''

def isogram(word):
    word = word.lower()
    uniq_letter = set()
    
    for letter in word:
        if letter in uniq_letter:
            return False
        
        uniq_letter.add(letter)
    
    return True

print(isogram('Algorithm'))
print(isogram('Consecutive'))
print(isogram('PasSword'))