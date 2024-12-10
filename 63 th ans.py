class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def area(self):
        return self.length * self.width


s1 = Rectangle(5, 4)


print("Area of the rectangle:", s1.area())
