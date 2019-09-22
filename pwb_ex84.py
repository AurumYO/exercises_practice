# Exercise 84: Median of Three Values. solved 42 lines
# Write a function that takes three numbers as parameters, and returns the median value of those parameters as its
# result. Include a main program that reads three values from the user and displays their median. Hint: The median value
# is the middle of the three values when they are sorted into ascending order. It can be found using if statements, or
# with a little bit of mathematical creativity.
print("This program finds median of three values")


# function median_finder defines median integer of three given integers
def median_finder(a, b, c):
    if b <= a <= c or c <= a <= b:
        return a
    if a <= b <= c or c <= b <= a:
        return b
    if a <= c <= b or b <= c <= a:
        return c


# main function which calls for user input and computes the result of computations
def main():
    i = int(input("Please enter first number here: "))
    j = int(input("Please enter second number here: "))
    k = int(input("Please enter third number here: "))

    print("The median of numbers {}, {}, {} is {}.".format(i, j, k, median_finder(i, j, k)))


main()
