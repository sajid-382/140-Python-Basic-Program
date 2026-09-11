# Method - 1
def uncommon_word(str1,str2):
    word1 = str1.split()
    word2 = str2.split()
    result = []
    for i in word1:
        for j in word2:
            if i not in word2:
                result.append(i)
                
            elif j not in word1:
                result.append(j)
    return result

string1 = "This is the first string"
string2 = "This is the second string"
# Find uncommon words between the two strings
uncommon = set(uncommon_word(string1, string2))
# Print the uncommon words
print("Uncommon words:", list(uncommon))


# Method -2 

def uncommon_words(str1, str2):
# Split the strings into words and convert them to sets
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    # Find uncommon words by taking the set difference
    uncommon_words_set = words1.symmetric_difference(words2)
    
    # Convert the set of uncommon words back to a list
    uncommon_words_list = list(uncommon_words_set)
    return uncommon_words_list

# Input two strings
string1 = "This is the first string"
string2 = "This is the second string"

# Find uncommon words between the two strings
uncommon = uncommon_words(string1, string2)

# Print the uncommon words
print("Uncommon words:", uncommon)