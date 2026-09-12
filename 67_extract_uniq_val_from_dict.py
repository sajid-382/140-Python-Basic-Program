# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}
# initialize set for unique
uniq_val = set()

for i in my_dict.values():
    uniq_val.add(i)
    
unique_value = list(uniq_val)

print("Unique value from dictionary :", unique_value)