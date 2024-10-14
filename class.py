
#Python Classes and Objects
#Create a class called Rectangle with two methods
#intance variables: length, width
#area: calculate area of Rectangle
#perimeter: calculate perimeter of Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
       return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an instance of the Rectangle class
rect = Rectangle(length, width)

# Call the area and perimeter methods
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an instance of the Rectangle class
b = Rectangle(length, width)

# Call the area and perimeter methods
print("Area:", b.area())
print("Perimeter:", b.perimeter())


    
        
