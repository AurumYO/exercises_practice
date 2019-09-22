# Exercise 104: Sorted Order. Solved in 21 lines.
# Write a program that reads integers from the user and stores them in a list. Your program should continue reading
# values until the user enters 0. Then it should display all of the values entered by the user (except for the 0)
# in order from smallest to largest, with one value appearing on each line. Use either the sort method or the sorted
# function to sort the list.


# This function prompts user to enter integers and displays all entered integers sorted in ascending order
def display_sorted():
    numbers_list = []
    num = int(input("Please enter your integer to your list or press '0' to finish: "))
    # function prompts to enter any number of integers and to quit the entering integers user must press 0
    # all integers inputted by user stored in list
    while num != 0:
        numbers_list.append(num)
        num = int(input("Please enter your integer to your list or press '0' to finish: "))

    # After user ended input of integers function display each integer from the list in ascending order
    print("The entered sorted numbers in ascending order are: ")
    for n in sorted(numbers_list):
        print(n)


if __name__ == '__main__':
    display_sorted()
