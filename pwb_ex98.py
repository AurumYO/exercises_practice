# Exercise 98: Hexadecimal and Decimal Digits. Solved 41 lines
# Write two functions, hex2int and int2hex, that convert between hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A
# , B, C, D, E and F) and base 10 integers. The hex2int function is responsible for converting a string containing
# a single hexadecimal digit to a base 10 integer, while the int2hex function is responsible for converting an integer
# between 0 and 15 to a single hexadecimal digit. Each function will take the value to convert as its only parameter
# and return the converted value as the function’s only result. Ensure that the hex2int function works correctly for
# both uppercase and lowercase letters. Your functions should end the program with a meaningful error message if an
# invalid parameter is provided.


def hex2int(string):
    integer = int(string, 16)
    return integer


def int2hex(number):
    hex_number = hex(number)
    return hex_number


def main():
    try:

        hex_string = str(input("Please enter hexadecimal number here: "))
        number = hex2int(hex_string)
        print("The hexadecimal number {} in decimal format will be {}".format(hex_string, number))

        int_number = int(input("Please enter integer here: "))
        hexadecimal = int2hex(int_number)
        print("The decimal number {} in hexadecimal format will be {}".format(int_number, hexadecimal))

    except ValueError:
        print("Provided by you value is in wrong format!!!!")


if __name__ == '__main__':
    main()
