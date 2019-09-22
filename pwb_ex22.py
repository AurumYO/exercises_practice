# Exercise 22:Area of a Triangle (Again).
# In the previous exercise you created a program that computed the area of a triangle when the length of its base and
# its height were known. It is also possible to compute the area of a triangle when lengths of all three sides known.
# Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle can be
# calculated using the following formula:
#                                   area = sqrt(s × (s − s1) × (s − s2) × (s − s3))
# Develop a program that reads the lengths of the sides of a triangle from the user and displays its area.

from math import sqrt


print("this program computes the area of the triangle given the size of 3 sides.")
print()

user_input = str(input("Please, enter the size of the sides of the triangle, using comma separator: "))

# s4 = int(input("Please, enter the size of the first side of the triangle: "))
# s5 = int(input("Please, enter the size of the second side of the triangle: "))
# s6 = int(input("Please, enter the size of the sites of the third side of the triangle: "))

# converting user input from string to list on numbers with sizes of sides
u_i = user_input.split(',')
# assign to each side the size from user input
s1, s2, s3 = int(u_i[0]), int(u_i[1]), int(u_i[2])

# computing sides perimeter
# sides1 = (s4 + s5 + s6)/2    # alternative version
sides = (s1 + s2 + s3)/2

# calculating the area of the triangle
area = sqrt(sides * (sides - s1) * (sides - s2) * (sides - s3))
# area1 = sqrt(sides1 * (sides1 - s4) * (sides1 - s5) * (sides1 - s6))  # alternative version

print("The area of the triangle with sides {0} is {1}".format(user_input, area))
# print("The area of the triangle with sides {0}, {1},{2} is {3}".format(s4, s5, s6, area1)) # alternative output
