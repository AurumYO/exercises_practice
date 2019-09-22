# Ex 81: Compute the Hypotenuse. solved 27 lines.
# Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the
# hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result. Include a main program that
# reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of
# the hypotenuse, and displays the result.
print("This program calculates the length of the hypotenuse of the triangle.")
print()


# this function takes as parameters lengths of two sides of the triangle and computes the hypotenuse of the triangle
def pythagorean_hypotenus(a, b):
    from math import sqrt
    return sqrt(a ** 2 + b ** 2)


# this functions prompts user to give two sides of the triangle and computes the hypotenuse of the triangle, rounded
def main():
    a = float(input("Please, enter the length of the first shortest side of the triangle: "))
    b = float(input("Please, enter the length of the second shortest side of the triangle: "))
    hypotenus = round(pythagorean_hypotenus(a, b), 4)  # rounds value of the hypotenuse to the 4 decimal points
    print("The length of the hypotenuse with length of sides {} and {} is equal to {}".format(a, b, hypotenus))


# function demonstration
if __name__ == '__main__':
    main()
