# Exercise 101: Reduce a Fraction to Lowest Terms. Solved in 47 lines.
# Write a function that takes two positive integers that represent the numerator and denominator of a fraction as its
# only two parameters. The body of the function should reduce the fraction to lowest terms and then return both the
# numerator and denominator of the reduced fraction as its result. For example, if the parameters passed to the function
# are 6 and 63 then the function should return 2 and 21. Include a main program that allows the user to enter
# a numerator and denominator. Then your program should display the reduced fraction.


# This function finds greatest common divisor for two integers n and m
def common_divisor(n, m):
    if n > m:
        divisor = m
    else:
        divisor = n
    # function divides n and m by divisor and decreases divisor by 1 until find greatest common divisor is found
    while True:
        if m % divisor == 0 and n % divisor == 0:
            break
        else:
            divisor -= 1
    # function returns greatest common divisor
    return divisor


# This function finds lowest fraction for two given numbers
def reduced_fraction(numerator, denominator, divisor):
    return int(numerator/divisor), int(denominator/divisor)


# Main function calls user to input two numbers and displays the reduced fraction for two numbers
def main():
    numerator = int(input("Please, enter your first integer as numerator here: "))
    denominator = int(input("Please, enter your seconr integer ans denominator here: "))
    # function finds common divisor for numerator and denominator
    divisor = common_divisor(numerator, denominator)
    # function finds reduced fractions for two numbers with common divisor
    reduced = reduced_fraction(numerator, denominator, divisor)
    # display the result of computations
    print("The reduced fraction of {} and {} are {} and {}.".format(numerator, denominator, reduced[0], reduced[1]))


if __name__ == '__main__':
    main()
