'''
Create a function that takes a string and returns a string with its letters in
alphabetical order.
Examples
alphabet_soup("hello") 
➞ "ehllo"
alphabet_soup("edabit") 
➞ "abdeit"
alphabet_soup("hacker") 
➞ "acehkr"
alphabet_soup("geek") 
➞ "eegk"
alphabet_soup("javascript") 
➞ "aacijprstv"
'''
def sort_str(string):
    return ''.join(sorted(string))

print(sort_str('sajid'))