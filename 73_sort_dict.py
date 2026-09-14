# Sort by Keys:
sample_dict = {'apple': 3, 'cherry': 1, 'banana': 2, 'date': 4}

sorted_dict = dict(sorted(sample_dict.items()))

print("Sorted dict :")

for key , value in sorted_dict.items():
    print(f"{key} : {value}")