def rotate_arr(arr,d):
    n=len(arr)
    if d <= 0 or d >= n:
        return arr

    rotate_array = [0]*n

    for i in range(n):
        rotate_array[i]=arr[(i+d)%n]
    return rotate_array


array=[1,2,3,4,5]
d=2 # steps for rotation

print(f"Original array = {array}")
print(f"Rotated array = {rotate_arr(array,d)}")