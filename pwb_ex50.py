# Exercise 50: Roots of a Quadratic Function. A univariate quadratic function has the form f(x) = ax **2 + bx + c,
# where a, b and c are constants, and a is non-zero. The roots of a quadratic function can be found by finding the
# values of x that satisfy the quadratic equation ax 2 + bx + c = 0. A quadratic function may have 0, 1 or 2 real roots.
# These roots can be computed using the quadratic formula, shown below:
# root = (-b +/- b**2 -4ac)/2a
# The portion of the expression under the square root sign is called the discriminant. If the discriminant is negative
# then the quadratic equation does not have any real roots. If the discriminant is 0, then the equation has one real
# root. Otherwise the equation has two real roots, and the expression must be evaluated twice, once using a plus
# sign, and once using a minus sign, when computing the numerator. Write a program that computes the real roots of a
# quadratic function. Your program should begin by prompting the user for the values of a, b and c. Then it should
# display a message indicating the number of real roots, along with the values of the real roots (if any).
import math
print("This programm computes the roots of quadratic function.")
a = None
while not a:
    a = int(input("Please enter value of 'a' ('a' can not be '0') here: "))
b = int(input("Please enter value of 'b' here: "))
c = int(input("Please enter value of 'c' here: "))
discriminant = (b ** 2) - (4 * a * c)
if discriminant < 0:
    print("The quadratic equation of {0}, {1} and {2} does not have any roots.".format(a, b, c))
else:
    root1 = (-b - math.sqrt(discriminant)) / (2 * a)
    root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print("The first value of the quadratic function of {0}, {1}, and {2} is {3:0.4f}".format(a, b, c, root1))
    print("The second value of the quadratic function of {0}, {1}, and {2} is {3:0.4f}".format(a, b, c, root2))
