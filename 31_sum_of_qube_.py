def sum_of_qube(n):
    sum =0
    for x in range(1,n+1):
        sum= sum + x**3
    return sum

num=int(input("Enter any Natural number :"))

if num <= 0:
    print('Please enter a number grater than zero......')
else:
    print(f"Sum of qube of first {num} natural number = {sum_of_qube(num)}")