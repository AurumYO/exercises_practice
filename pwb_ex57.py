# Ex.57: Is it a Leap Year? The rules for determining whether or not a year is a leap year follow:
# Any year that is divisible by 400 is a leap year.
# Of the remaining years, any year that is divisible by 100 is not a leap year.
# Of the remaining years, any year that is divisible by 4 is a leap year.
# All other years are not leap years.
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.
print("This program defines if the year s a leap year or not.")
year = None
while not year:
    try:
        year = int(input("Please enter the year here: "))
    except ValueError:
        print("The value of the year you have entered is of the wrong format. Try again!")

if year % 400 == 0 or year % 4 == 0:
    name_year = 'a leap'
else:
    name_year = 'not a leap'
print("The year {0} is {1} year.".format(year, name_year))
