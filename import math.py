import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

radius = float(input("Enter the radius of the circle: "))
circ = Circle(radius)
print("Area: {:.2f}".format(circ.area()))
print("Circumference: {:.2f}".format(circ.circumference()))
