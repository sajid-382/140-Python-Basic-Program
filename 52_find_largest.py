arr = [6,12,32,45,61,11]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] >= largest:
        largest = arr[i]
        
print("Largest number in the list : ",largest)