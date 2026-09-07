def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y
def division(x,y):
    if y==0:
        print("Can't divide by zero")
    else:
        return x/y

print("Welcome to the Calculator : ")

while True:
    print("\n1 - Addition")
    print("2 - Substractio")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")
    option = int(input("Please choose option which operation wants to perform : "))

    if option==1:
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        sum=add(num1,num2)
        print("Sum = ",sum)
    elif option==2:
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        subs=sub(num1,num2)
        print("subtract = ",subs)
    elif option==3:
        num1 = int(input("Enter 1st number :"))
        num2 = int(input("Enter 2nd number :"))
        product=multi(num1,num2)
        print("Product = ",product)
    elif option==4:
            num1 = int(input("Enter 1st number :"))
            num2 = int(input("Enter 2nd number :"))
            div=division(num1,num2)
            print("Division = ",div)
    elif option==5:
        print("Thanks for using calculator...")
        exit()
    else:
        print("Please enter valid option.....")