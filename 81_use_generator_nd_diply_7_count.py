'''
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n
'''

class DivisibleBySeven:
    def __init__(self,n):
        self.n = n
    
    
    def divide_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

n = int(input("Enter range :"))

# Create Object
d = DivisibleBySeven(n)

divideby_seven = d.divide_by_seven()

for x in divideby_seven:
    print(x)