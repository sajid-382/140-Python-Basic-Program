
def is_happy(num):
    seen=set()
    while num != 1 and num not in seen:
        seen.add(num)
        
        num=sum(int(i)**2 for i in str(num) )
    
    return num == 1
a,b = map(int, input("enter range for displaying happy number : ").split(' '))
happy = []
for num in range(a,b+1):    
    if is_happy(num):
        happy.append(num)


print(happy)