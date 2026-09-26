'''
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") 
vow_replace("cheese casserole", "o") 
➞ "upplus und bununus"
➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") 
➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.
'''
def vow_replace(string, vow):
    vowels = "aeiou"
    result = ""
    
    for char in string:
        if char in vowels:
            result += vow
        else:
            result += char
    return result
            
print(vow_replace('sajid','i'))