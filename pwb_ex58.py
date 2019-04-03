# Exercise 58: Next Day. Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2013-11-18 then your program should display a message
# indicating that the day immediately after 2013-11-18 is 2013-11-19. If the user enters values that represent
# 2013-11-30 then the program should indicate that the next day is 2013-12-01. If the user enters values that represent
# 2013-12-31 then the program should indicate that the next day is 2014-01-01. The date will be entered in numeric form
# with three separate input statements; one for the year, one for the month, and one for the day. Ensure that your
# program works correctly for leap years.
print("This program reads the date line by line and computs its immediate successor.")
year, month, date = None, None, None
month_30days = [4, 6, 9, 11]
month_31days = [1, 3, 5, 7, 8, 10]
while not date:
    try:
        year = int(input("Please enter the year here : "))  # year input and define
        if year % 400 == 0 or year % 4 == 0:
            name_year = 'leap'
        else:
            name_year = 'not leap'
        month = int(input("Please enter the number of the month here: "))  # month input and define
        if 13 <= month < 0:
            month = None
            raise ValueError
        date = int(input("Please enter the date here: "))  # date input and logic description for each month
        if month == 2 and name_year == 'leap' and 0 < date < 29:
            new_month = month
            new_date = date + 1
        elif month == 2 and name_year == 'leap' and date == 29:
            new_month = month + 1
            new_date = 1
        elif month == 2 and name_year == 'not leap' and 0 < date < 28:
            new_month = month
            new_date = date + 1
        elif month == 2 and name_year == 'not leap' and date == 28:
            new_month = month + 1
            new_date = date + 1
        elif month in month_31days and 0 < date < 31:
            new_month = month
            new_date = date + 1
        elif month in month_31days and date == 31:
            new_month = month + 1
            new_date = 1
        elif month in month_30days and 0 < date < 30:
            new_month = month
            new_date = date + 1
        elif month in month_30days and date == 30:
            new_month = month + 1
            new_date = date + 1
        elif month == 12 and date == 31:
            year += 1
            new_date = 1
            new_month = 1
        else:
            date = None
            raise ValueError
    except ValueError:
        print("The entered values by you are of wrong format. Please try again.")
#print(year, month, date, 'new', new_month, new_date)
if month < 10:
    name_month = '0' + str(month)
if month >= 10:
    name_month = month
if new_month < 10:
    new_month = '0' + str(new_month)
if date < 10:
    date = '0' + str(date)
if new_date < 10:
    new_date = '0' + str(new_date)

print("After the date {}-{}-{} the immediate date is {}-{}-{}.".format(year, name_month, date, year, new_month,
                                                                       new_date))
