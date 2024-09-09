#Program to Compute Surface Area of a cylinder
radius = float(input("Enter the radius of the cylinder:"))
height = float(input("Enter the height of the cylinder:"))
surface_area = 2*(3.142*radius*radius) + 2*(3.142*radius*height)
print("The surface area of the cylinder is:", surface_area)