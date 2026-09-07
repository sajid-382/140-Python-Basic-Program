# Using sum() function

arr1 =[2,3,4,5,6]
sum = sum(arr1)
print("sum of array = ",sum)

# using function and loop

def sum_of_array(arr):
    total = 0
    for x in arr:
        total=total+x
    return total

arr = eval(input("Enter an array value :"))

print(f"Sum of array = {sum_of_array(arr)}")