num=int(input("Enter number for factorial : "))

# method 1
factorial=1
for x in range(1,num+1):
    factorial =factorial*x

# method 2
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1

print("The factorial is ",factorial)
print("The factorial is ",fact)