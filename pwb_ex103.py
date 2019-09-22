# Ex 103: Magic Dates. Solved 26 lines.
# A magic date is a date where the day multiplied by the month is equal to the two digit year. For example,
# June 10, 1960 is a magic date because June is the sixth month, and 6 times 10 is 60, which is equal to the two digit
# year. Write a function that determines whether or not a date is a magic date.
# Use your function to create a main program that finds and displays all of the magic dates in the 20th century.
# You will probably find your solution to Exercise 100 helpful when completing this exercise.
from pwb_ex100 import days_in_month
from datetime import date


# this function defines if provide date is magic or not
# magic date is when month * day  == Y'60 (of the Y1960) else the date is not magic
def magic_dates(year, month, day):
    if month * day == year - 1900:
        return True
    return False


# This function finds and displays all magi date of the 20th century
def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days_in_month(month,year)+1):
                magic_date = magic_dates(year, month, day)
                if magic_date:
                    print("{} is magic date.".format(date(year, month, day)))


main()
