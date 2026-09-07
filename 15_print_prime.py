a,b=map(int,input("Enter a range you want to print prime number b/w : ").split())

for i in range(a,(b+1)):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
2