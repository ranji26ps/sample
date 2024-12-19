
import math

class Distance:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def rectangle(self, length, width):
        self.area = length * width
        self.perimeter = 2 * (length + width)
        return self.area, self.perimeter

    def circle(self, radius):
        self.area = math.pi * radius ** 2
        self.perimeter = 2 * math.pi * radius
        return self.area, self.perimeter
length = int(input("Enter length for rectangle: "))
width = int(input("Enter width for rectangle: "))
radius = int(input("Enter radius for circle: "))
gd = Distance()
area, perimeter = gd.rectangle(length, width)
print(f"Rectangle: Area = {area}, Perimeter = {perimeter}")
area, perimeter = gd.circle(radius)
print(f"Circle: Area = {area}, Perimeter = {perimeter}")
