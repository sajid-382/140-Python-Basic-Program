def remove_char(string,n):
    if n < 0 and n>len(string):
        return "Index Out Of Range"
    result = string[:n]+string[n+1:]
    
    return result
my_str = "Hello Sajid"
n=int(input("Enter index which element want to remove :"))

new_str = remove_char(my_str,n)
print(f"Removed {n} elemnt from string : ",new_str)