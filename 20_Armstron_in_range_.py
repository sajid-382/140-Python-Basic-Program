lower=int(input("Enter lower order :"))
upper=int(input("Enter upper order :"))


for num in range(lower,upper+1):
    num_str=str(num)
    num_digit=len(num_str)
    tem_num=num
    sum=0
    while tem_num >0:
        digit=tem_num%10
        sum=sum+digit**num_digit
        tem_num //= 10
    if sum==num:
        print(num)