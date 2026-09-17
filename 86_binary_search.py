'''
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
[1,2,3,4,5,6,7,8,9]
'''

def binary_search(arr,target):
    left , right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

arr = [12,23,34,45,56,67,78,89]
print(arr)
target = int(input("Enter number you want to search :"))

print(f"The index of {target} element is : {binary_search(arr,target)}")