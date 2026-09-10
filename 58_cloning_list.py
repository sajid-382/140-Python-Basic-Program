#Method -1 using slice operator
original_list1=[1,2,3,4,5]
clone_list=original_list1[:]
print(clone_list)


# Method -2 using list constructor
original_list2=[1,2,3,4,5,6]
clone_list = list(original_list2)
print(clone_list)

# Method -3 using list comprehension
original_list3=[1,2,3,4,5,6,7]
clone_list=[i for i in original_list3]
print(clone_list)