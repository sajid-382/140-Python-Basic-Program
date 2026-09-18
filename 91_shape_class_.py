'''
Define a class named Shape and its subclass Square. The Square class has an init
function which takes a length as argument. Both classes have an area function which
can print the area of the shape where Shape's area is 0 by default.
'''
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

S = Shape()   
sq = square(5)
print("Area of shape by default :", S.area())
print("Area of Square :", sq.area())
