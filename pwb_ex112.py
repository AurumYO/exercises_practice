# Ex 112: Below and Above Average. Solved 44 Lines.
# Write a program that reads numbers from the user until a blank line is entered. Your program should display the
# average of all of the values entered by the user. Then the program should display all of the below average values,
# followed by all of the average values (if any), followed by all of the above average values. An appropriate
# label should be displayed before each list of values.

# first, program will ask user to enter the numbers or blank like to stop input. entered by user numbers stored in list
user_numbers = []
num = input("Please enter your number here or blank line to stop entering numbers: ")
while num != '':
    user_numbers.append(int(num))
    num = input("Please enter your number here or blank line to stop entering numbers: ")

# secondly, program calculates average from entered by user numbers
sum_user_numbers = 0
for dig in user_numbers:
    sum_user_numbers += dig    # program sums each entered number to variable 'sum_user_numbers'
# rpogram finds average by divide of sum of all entered numbers by quantity of all entered numbers by user
average = int(sum_user_numbers / len(user_numbers))
print("The average of all entered numbers is {:d}".format(average))  # display of the average number

# thirdly, program sorts all entered by user numbers and adds each number to the corresponding string
# string type of tada was chosen to make display more readable
less_than_average, equal_to_average, bigger_than_average = '', '', ''
for num in user_numbers:
    if num < average:                          # if number in user's list is less than average
        less_than_average += str(num) + ' '    # such number added to string, containing numbers less than average
    elif num == average:                       # if number in user's list is equal to average
        equal_to_average += str(num) + ' '    # such number added to string, containing numbers equal to average number
    elif num > average:                        # if number in user's list is bigger than average
        bigger_than_average += str(num) + ' '  # such number added to string, containing numbers bigger than average
# fourthly, at each separate line displayed numbers smaller, than equal and then bigger than average
print("Within entered, {} less than average.".format(less_than_average))
print("From entered, numbers {} equal to average.".format(equal_to_average))
print("And within entered numbers {} bigger than average.".format(bigger_than_average))
