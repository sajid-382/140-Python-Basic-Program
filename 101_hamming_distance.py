'''
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"
Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") 
➞ 5
hamming_distance("abcde", "abcde") 
➞ 0
hamming_distance("strong", "strung") 
➞ 1
'''

def hamming_distance(str1,str2):
    if len(str1) != len(str2):
        raise ValueError("Input string must have same length")
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

print("Hamming Distance :",hamming_distance("abcde", "abcde"))
print("Hamming Distance :",hamming_distance("strong", "strung"))
print("Hamming Distance :",hamming_distance("abcde", "bcdef"))
