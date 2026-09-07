a,b= map(int , input("Enter a range for displaying disarium number :").split(' '))

print("Disarium number : ")
for num in range(a,b+1):
    num_str=str(num)
    digit_sum=sum(int(i)**(indx+1) for indx,i in enumerate(num_str))
    
    if digit_sum==num:
        print(num)