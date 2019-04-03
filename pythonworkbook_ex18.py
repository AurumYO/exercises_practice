#  Exercise 18:Volume of a Cylinder. The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one decimal place.

import math

print("This program calculates the volume of the cylinder!")
radius = float(input("Please enter radius of the cylinder: "))
height = float(input("Please enter height of the cylinder: "))

vol_cylinder: float = math.pi * pow(radius, 2)*height
print("the volume of cylinder with radius %1.2d and height %1.2d is %1.2f." % (radius, height, vol_cylinder))
