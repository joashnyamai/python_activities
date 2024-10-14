# Python Classes and Objects
# Create a class called circle with two methods
# instance variables: radius, diameter
# area: calculate area of circle
# circumference: calculate circumference of circle
class circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)

radius = float(input("Enter the radius of the circle: "))
circ = circle(radius)
print("Area:", circ.area())
print("Circumference:", circ.circumference())