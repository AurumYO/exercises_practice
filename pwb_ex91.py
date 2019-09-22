# Ex 91: Operator Precedence. (solved 30 lines)
# Write a function named precedence that returns an integer representing the precedence of a mathematical operator.
# A string containing the operator will be passed to the function as its only parameter. Your function should return
# 1 for + and -, 2 for * and /, and 3 for ˆ. If the string passed to the function is not one of these operators
# then the function should return -1. Include a main program that reads an operator from the user and either displays
# the operator’s precedence or an error message indicating that the input was not an operator.
# Your main program should only run when the file containing your solution has not been imported into another program.
print("This program displays the operator precedence.")


def operator_finder(string):
    if string == "+" or string == "-":
        return 1
    if string == "/" or string == "*":
        return 2
    if string == "^":
        return 3
    else:
        return -1


if __name__ == "__main__":
    operator = "+"
    result = operator_finder(operator)
    if 1 <= result <= 3:
        print("There is operator in the string {}.".format(operator))
    if result == -1:
        print("There is no operator in the string {}.".format(operator))
