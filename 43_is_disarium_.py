def is_disarium(number):
    num_str = str(number)
    
    digit_sum = sum(int(i)**(index+1) for index,i in enumerate(num_str))
    
    return digit_sum==number

try:
    num=int(input("Enter a number :"))
    
    if is_disarium(num):
        print("The number is Disarium ",num)
    else:
        print("The number is not Disarium ",num)
        
        
except ValueError:
    print("Please enter valid input......")
    
