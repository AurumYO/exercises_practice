# Exercise 99: Arbitrary Base Conversions. Solved 61 lines.
# Write a program that allows the user to convert a number from one base to another. Your program should support bases
# between 2 and 16 for both the input number and the result number. If the user chooses a base outside of this range
# then an appropriate error message should be displayed and the program should exit. Divide your program into several
# functions, including a function that converts from an arbitrary base to base 10, a function that converts from
# base 10 to an arbitrary base, and a main program that reads the bases and input number from the user. You may find
# your solutions to Exercises 77, 78 and 98 helpful when completing this exercise.


# This function converts binary number to decimal.
def bin2decimal(n):
    binary = int(n)
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# This function converts decimal number to binary
def decimal2binary(n):
    decimal = int(n)
    return bin(decimal)


# This function converts decimal to octal
def decimal2oct(n):
    decimal = int(n)
    return oct(decimal)


# This function converts octal to decimal
def oct2decimal(n):
    return int(n, 8)


# This function converts hexadecimal number to base 10 integers
def hex2decimal(string):
    return int(string, 16)


# This function converts base 10 integers to hexadecimal number
def decimal2hex(number):
    hex_number = hex(number)
    return hex_number


# This function makes check that entered base value is of the valid format
def base_check(base):
    if base not in [2, 8, 10, 16]:
        print("The entered value of base is of the wrong format!!!!")
        quit()


# Main functions prompts input from user, checks the validity of the entered bases, converts entered number to decimal
def main():
    from_base = int(input("Please, enter base from which to convert: "))
    base_check(from_base)
    number = str(input("Please enter your number in chosen base here: "))
    if from_base == 2:
        decimal_number = bin2decimal(number)
    elif from_base == 8:
        decimal_number = oct2decimal(number)
    elif from_base == 10:
        decimal_number = number
    elif from_base == 16:
        decimal_number = hex2decimal(number)
    # decimal number than converted to chosen base
    to_base = int(input("Please enter the base you want to convert your number to: "))
    base_check(to_base)
    if to_base == 2:
        converted_number = decimal2binary(decimal_number)
    if to_base == 8:
        converted_number = decimal2oct(decimal_number)
    if to_base == 10:
        decimal_number = converted_number
    if to_base == 16:
        converted_number = decimal2hex(decimal_number)
    print("Number {} in base {} converted to base {} will be {}.".format(number, from_base, to_base, converted_number))


if __name__ == '__main__':
    main()
