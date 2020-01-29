# Ex. 148: Sum a List of Numbers. Solved in 26 lines.

# program that sums all of the numbers entered by the user while ignoring any
# lines entered by the user that are not valid numbers.
number = input("Please enter your number here: ")

total_sum = 0
# program until the user enters a blank line, checks if string is number, and ands number to total sum
# after it prompts user to enter new number, and displays error if entered value is not number
while number != '':
    # check is entered line is valid number
    try:
        # ensure that program works correctly for both integers and floating point numbers
        num = float(number)
        # add entered number to total sum
        total_sum += num
        # display the current sum after each number is entered.
        print("Currently the total sum of entered numbers is {}".format(total_sum))
    # display an appropriate error message after any invalid input, and then continue to ask for user input
    except ValueError:
        print("The entered value is not a number!!!")
    # prompt user to enter new number or blank line
    number = input("Please enter your number here or blank line to exit: ")
# display total sum of all entered lines
print("The total sum for all enterred numbers is {]!".format(total_sum))
