def split_array(arr,d):
    if d<=0 or d>= len(arr):
        return arr

    # split array in two parts 

    first_part = arr[:d]
    second_part = arr[d:]

    return second_part + first_part

array = [1,2,3,4,5]
d=2

print(f"Original array = {array}")
print(f"Array after spliting and adding = {split_array(array,d)}")