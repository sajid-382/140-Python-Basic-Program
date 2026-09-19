'''
Write a function that stutters a word as if someone is struggling to read it. The first
two letters are repeated twice with an ellipsis ... and space after each, and then the
word is pronounced with a question mark ?.
Examples
stutter("incredible") 
➞ "in... in... incredible?"
stutter("enthusiastic") 
➞ "en... en... enthusiastic?"
stutter("outstanding") 
➞ "ou... ou... outstanding?"
Hint :- Assume all input is in lower case and at least two characters long.
'''

def stutter_word(word):
    if len(word) < 2:
        return "Word must be atleast two characte..."
    
    stutter = f"{word[:2]}....{word[:2]}....{word}"
    
    return stutter

print(stutter_word("incredible"))  
print(stutter_word("enthusiastic"))  
print(stutter_word("outstanding"))