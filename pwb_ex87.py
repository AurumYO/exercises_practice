# Exercise 87: Center a String in the Terminal. (Solved—31 Lines)
# Write a function that takes a string of characters as its first parameter, and the width of the terminal in characters
# as its second parameter. Your function should return a new string that consists of the original string and
# the correct number of leading spaces so that the original string will appear centered within the provided width when
# it is printed. Do not add any characters to the end of the string.
# Include a main program that demonstrates your function.


def centered_string(string, width):
    # search for empty spaces in the terminal as width of the terminal - length of the string
    free_length = width - len(string)

    if free_length % 2 == 0:
        right_side = free_length // 2
        left_side = free_length // 2
    if free_length % 2 != 0:
        right_side = free_length // 2
        left_side = free_length // 2 - 1
    return ''.join(' ' * right_side + string + ' ' * left_side)  # returns centered string by the width of the terminal


def main():
    string = str(input("Please enter your string here: "))
    width = int(input("Please enter the width of your terminal here: "))
    new_string = centered_string(string, width)
    print(new_string)


main()

