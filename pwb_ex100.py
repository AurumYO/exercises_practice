# Exercise 100: Days in a Month. Solved in 47 lines.
# Write a function that determines how many days there are in a particular month. Your function will take two
# parameters: The month as an integer between 1 and 12, and the year as a four digit integer. Ensure that your function
# reports the correct number of days in February for leap years. Include a main program that reads a month and year
# from the user and displays the number of days in that month. You may find your solution to Exercise 57 helpful
# when solving this problem.


# This function defines the number of days in month
def days_in_month(month, year):
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:  # checks if the months is among the months with 31 days
        days = 31
    if month in [4, 6, 9, 11]:            # checks if the months is among the months with 30 days
        days = 30
    if month == 2:                            # if the month is February function checks is the year is a leap year
        if year % 400 == 0 or year % 4 == 0:  # if it is a leap year, than February of that year has 29 days
            days = 29
        else:                                 # if it is not a leap year, than in February of that year is 28 days
            days = 28
    return days                               # function returns number of days in the chosen month of the year


# Main function asks input of month and year in number format from user and displays the number of days in that month
def main():
    month = int(input("Please enter your month as an integer between 1 and 12: "))
    year = int(input("Please enter your year here: "))
    # Manin program runs function defining number in days of teh given month
    number_days = days_in_month(month, year)
    # and prints out the result of computations
    print("In month {} of the year {} there is {} days.".format(month, year, number_days))


if __name__ == '__main__':
    main()
