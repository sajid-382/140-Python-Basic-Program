def n_largest_elemnt(list,n):
    
    list.sort(reverse=True)
    n_larger = list[:n]
    
    return n_larger

numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

n= int(input("Enter Number of elemnents you want largest : "))
n_largest = n_largest_elemnt(numbers,n)

print(n_largest)
