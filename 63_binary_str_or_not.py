def check_binary_str(string):
    result = True
    for i in string:
        if i not in "01":
            result=False
    return result

binary_str = "101010"

if check_binary_str(binary_str):
    print(f"The given string {binary_str} is a binary string")
else:
    print(f"The given string {binary_str} is not a binary string")