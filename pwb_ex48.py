# Exercise 48: Chinese Zodiac. Solved—35 Lines) The Chinese zodiac assigns animals to years in a 12 year cycle. One 12
# year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon,
# and 1999 being another year of the hare.
# Write a program that reads a year from the user and displays the animal associated with that year. Your program
# should work correctly for any year greater than or equal to zero, not just the ones listed in the table.
print("This program defines what Chinese zodiac year is.")
# Ask for user input
year = int(input("Please enter the year here: "))
# Define the year according to Chinese zodiac sign
base = (year - 2000) % 12
if base == 0:
    sign = 'Dragon'
elif base == 1:
    sign = 'Snake'
elif base == 2:
    sign = 'Horse'
elif base == 3:
    sign = 'Sheep'
elif base == 4:
    sign = 'Monkey'
elif base == 5:
    sign = 'Rooster'
elif base == 6:
    sign = 'Dog'
elif base == 7:
    sign = 'Pig'
elif base == 8:
    sign = 'Rat'
elif base == 9:
    sign = 'Oax'
elif base == 10:
    sign = 'Tiger'
elif base == 11:
    sign = 'Hare'
# Print out the resule
print("The year {0:d} is year of the {1:s} according to Chinese zodiac.".format(year, sign))
