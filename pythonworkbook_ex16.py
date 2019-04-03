#Exercise 16:Area and Volume. Write a program that begins by reading a radius, r , from the user.
# The program will continue by computing and displaying the area of a circle with radius r and the
#volume of a sphere with radius r . Use the pi constant in the math module in your calculations.
#Hint: The area of a circle is computed using the formula area = pi r2. The
#volume of a sphere is computed using the formula volume = 4/3 (pi * r3).
import math
r = float(input("Please enter radius here: "))
#calculates the area of the circle
area = math.pi * (r**2)
sphere_vol = 4/3 * math.pi * (r **3)
print("The area of a circle with radius %8.2f equals to %8.2f." % (r, area), sep=" ")
print("The volume of a sphere with radius %8.2f equals to %8.2f." % (r, sphere_vol), sep=" ")