# Exercise 21:Area of a Triangle.
# The area of a triangle can be computed using the following formula, where b is the length of the base of the triangle,
# and h is its height:
#                 area = (b * h)/2
# Write a program that allows the user to enter values for b and h. The program
# should then compute and display the area of a triangle with base length b and height h.

print("This program calculates the area of the triangle.")
print()

# prompting the user to enter the base and height of the triangle
base = int(input("Please, enter the length of the triangle's base: "))
height = int(input('Please enter the height of the triangle: '))

triangle_area = (base * height) / 2

print("The area of the triangle with base {0} and height {1} is {2}.".format(base, height, triangle_area))
