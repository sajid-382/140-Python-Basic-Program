num=int(input("Enter Number : "))

if num<2:
    print(f"The number {num} given is not a prime number ")
else:
    for x in range(2,num):
        if num%x==0:
            print(f"This is not a prime number")
            break
    else:
        print(f"this number {num} is prime number")