# Ex 46: Season from Month and Day. The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the way that the calendar is
# constructed, we will use the following dates for this exercise:
# Spring - March 20; Summer - June 21; Fall - September 22; Winter - December 21.
# Create a program that reads a month and day from the user. The user will enter the name of the month as a string,
# followed by the day within the month as an integer. Then your program should display the season associated with
# the date that was entered.
print("This program defines the seasons.")
# Ask for user input with small extra feature - check of the date input
while True:
    month = str(input('Please enter the name of the month here: '))
    date = int(input('Please enter the day of the month  here: '))
    if int(date) > 31:
        continue
    if month == "February" and date > 29:
        print("February has only up to 29 days, please enter correct value!")
        continue
    if 0 < int(date) < 32:
        date = int(date)
        break
# Define the season
if month == 'January' or month == 'February':
    print("It will be a winter on the %s %s." % (month, date))
elif (month == 'March' and date < 20) or (month == 'December' and date >= 21):
    print("It will be a winter on the %s %s." % (month, date))
elif month == 'April' or month == 'May':
    print("It will be a spring on the %s %s." % (month, date))
elif (month == 'March' and date >= 20) or (month == 'June' and date < 21):
    print("It will be a spring on the %s %s." % (month, date))
elif month == 'July' or month == 'August':
    print("It will be a summer on the %s %s." % (month, date))
elif (month == 'June' and date >= 21) or (month == 'September' and date < 22):
    print("It will be a summer on the %s %s." % (month, date))
elif month == 'October' or month == 'November':
    print("It will be a fall on the %s %s." % (month, date))
elif (month == 'September' and date >= 22) or (month == 'December' and date < 21):
    print("It will be a fall on the %s %s." % (month, date))
else:
    print("The date you have entered is not a date!")
