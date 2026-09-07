def find_hcf(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
num1=int(input('Enter first number :'))
num2=int(input('Enter second number :'))

print(f"HCF of {num1} and {num2} is: \nHCF = {find_hcf(num1,num2)}")