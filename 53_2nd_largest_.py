# Method 1

def find_second_largest(list):
    largest = list[0]
    second_largest = float('-inf')
    
    for i in range(len(list)):
        if list[i] > largest:
            second_largest=largest
            largest=list[i]
        elif list[i] > second_largest and list[i] < largest:
            second_largest = list[i]
        
    return second_largest

list = [23,43,12,54,32]

second_larg = find_second_largest(list)

print("Second Largest number : ",second_larg)



# Method 2

list1 = [23,43,12,54,32]

list1.sort(reverse=True)

if len(list1) >= 2:
    print("The second largest number in the list is:",list1[1])
else:
    print("The list does not contain a second largest number.")
    

# Method 3

list2 = [23,43,12,54,32]

unique_num = set(list2)

unique_num.remove(max(unique_num))

print("Second Largest number :", max(unique_num))