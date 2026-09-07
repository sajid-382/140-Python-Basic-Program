def find_largest(arr):
    if not arr:
        return "Array is empty!"

    largest = arr[0]
    for x in arr:
        if x > largest:
            largest= x
    return largest

array = eval(input("enter an array :"))

print(f"Largest element = {find_largest(array)}")