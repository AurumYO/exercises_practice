# Ex 105: Reverse Order. Solved 20 lines.
# Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the
# end of the input. Once all of the values have been read your program should display them (except for the 0)
# in reverse order, with one value appearing on each line.


# This function prompts user to enter any number of integers and displays those integers in sorted reverse order
def reversed__user_list():
    numbers_list = []
    num = int(input("Please enter your integer to your list or press '0' to finish: "))
    # function prompts to enter any number of integers and to quit the entering integers user must press 0
    # all integers inputted by user stored in list
    while num != 0:
        numbers_list.append(num)
        num = int(input("Please enter your integer to your list or press '0' to finish: "))

    # After user ended input of integers function display each integer from the list in ascending order
    print("The entered sorted numbers in descending order are: ")
    for n in sorted(numbers_list, reverse=True):
        print(n)


if __name__ == '__main__':
    reversed__user_list()