# Ex 90: Does a String Represent an Integer? solved 30 lines
# In this exercise you will write a function named isInteger that determines whether or not the characters in a string
# represent a valid integer. When determining if a string represents an integer you should ignore any leading or
# trailing white space. Once this white space is ignored, a string represents an integer if its length is at least 1
# and it only contains digits, or if its first character is either + or - and the first character is followed by one or
# more characters, all of which are digits.
# Write a main program that reads a string from the user and reports whether or not it represents an integer. Ensure
# that the main program will not run if the file ontaining your solution is imported into another program.
# Hint: You may find the lstrip, rstrip and/or strip methods for strings helpful when completing this exercise.
# Documentation for these methods is available online.


def isInteger(string):
    string = string.strip()
    if len(string) < 1:
        return False
    else:
        signs = ['+', '-']
        if string[0] in signs and string[1:].isdigit():
            return True
        elif string.isdigit():
            return True
        else:
            return False


def main():
    string = input("Please, enter your string: ")
    result_if_integer = isInteger(string)
    if result_if_integer:
        print('The given string {} represent an integer'.format(string, result_if_integer))
    else:
        print('The given string {} doe not represent an integer'.format(string, result_if_integer))


if __name__ == '__main__':
    main()
