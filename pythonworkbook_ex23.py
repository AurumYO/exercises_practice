# Exercise 23:Area of a Regular Polygon. A polygon is regular if its sides are all the same length and the angles
# between all of the adjacent sides are equal. The area of a regular polygon can be computed using the following
# formula, where s is the length of a side and n is the number of sides:
#                                    area = ((n * s)2 ) / (4 * tan(pi/n)
# Write a program that reads s and n from the user and then displays the area of a regular polygon
# constructed from these values.
import math

print("This program calculates the area of the regular polygon.")
print()

# prompting user to enter the length of a side
s = int(input("Please, enter the length of the side of the regular polygon: "))
# prompting the user to enter number of sides
n = int(input("Please, enter the number of sides of the regular polygon: "))
area = (n * s ** 2)/(4*math.tan((math.pi/n)))

print("The area of the regular polygon with side's length {0} and {1} sides is {2}".format(s, n, round(area, 3)))
