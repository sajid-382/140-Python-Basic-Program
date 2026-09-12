# Method -1 using update() method 
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

print("Merging of two dictionary :",dict1)


# Method -2 using dictionary unpacking

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merg_dict= {**dict1, **dict2}

print("Merging of two dictionary :",merg_dict)