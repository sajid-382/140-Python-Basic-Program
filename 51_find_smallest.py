def find_smallest(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] <= smallest:
            smallest=arr[i]
    
    return smallest

arr = [23,32,15,34,111,25]

smallest = find_smallest(arr)

print("Smallest number in the array :",smallest)