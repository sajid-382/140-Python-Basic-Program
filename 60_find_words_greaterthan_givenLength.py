def find_words(word,k):
    list =[]
    for item in word:
        if len(item)>k:
            list.append(item)
    return list

word_list = ["apple", "banana", "cherry","cat" "date", "elderberry", "dragon","Mumbai","Umbrella","knite","Zebraa"]
k = 5
long_words= find_words(word_list,k)
print(f"words longer than {k} are :\n",long_words)