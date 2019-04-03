# Exercise 40: Name that Triangle. A triangle can be classified based on the lengths of its sides as equilateral,
# isosceles or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene. Write a program that reads the
# lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.
print("This program defines the type of triangle.")
# Prompt user to input the size of three sides of the tirangle
try:
    first_side, second_side, third_side = map(float, input("Please enter the length of the the sides of triangle, "
                                                          "using coma separator: ").split(','))
except ValueError:
    print("You have made a mistake in input format, please try one more time!")
# Define the type of triangle and print out the result
if first_side == second_side == third_side:
    print("Your triangle is equilateral.")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("Your triangle is isosceles.")
else:
    print("Your tirangle is scalene.")
