def check_monotonic(arr):
    increasing = decreasing = True
    

    for x in range(1,len(arr)):
        if arr[x] > arr[x-1]:
            increasing=False
        elif arr[x] < arr[x-1]:
            decreasing=False

    return increasing or decreasing

arr1=[2,4,6,7]
arr2=[8,6,5,3]
arr3=[3,5,2,3]

print("Array is Monotonic : ",check_monotonic(arr1))
print("Array is Monotonic : ",check_monotonic(arr2))
print("Array is Monotonic : ",check_monotonic(arr3))