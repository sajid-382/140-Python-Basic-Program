def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

num=int(input("Enter number for factorial : "))
if num ==0:
    print("Factorial is 0")
else:
    print(f'Facorial of {num} = {fact(num)}')