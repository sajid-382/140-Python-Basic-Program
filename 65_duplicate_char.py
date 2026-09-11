def duplicate_char(my_str):
    char_count = {}
    duplicate = []
    
    for i in my_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i , count in char_count.items():
        if count>1:
            duplicate.append(i)
    return duplicate

my_str = "sheikh sajid"

result = duplicate_char(my_str)

print(f"Duplicate Characters from string '{my_str}' is : {result}")