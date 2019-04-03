# Exercise 38: Month Name to Number of Days. The length of a month varies from 28 to 31 days. In this exercise you will
# create a program that reads the name of a month from the user as a string. Then your  program should display the
# number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

print("This program will name number of days in month by the name of the month.")

# Prompting user to name the month
month = str(input("Please, ener the month's name here: "))
m = month.lower()

# initilase the lists with names
long_months = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
short_months = ['april', 'june', 'september', 'november']

# define what time of months the input and number of days
if m in long_months:
    print(f"{month} has 31 days.")
elif m in short_months:
    print(f"{month} has 30 days.")
elif m == 'february':
    print(f"{month} has 28 or 29 days, depending if it is a leap year or not.")
else:
    print(f"{month} that's ain't a month!!!")
