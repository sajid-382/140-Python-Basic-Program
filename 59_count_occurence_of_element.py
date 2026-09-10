def count_occurence(list,k):
    count = list.count(k)
    return count

my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
n=int(input("Enter element from list :"))

count = count_occurence(my_list,n)
print(f"Number {n} Occurence in the list {count} times.")