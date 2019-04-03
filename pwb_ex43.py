# Exercise 43: Faces on Money. It is common for images of a country’s previous leaders, or other individuals of his-
# torical significance, to appear on its money. The individuals that appear on banknotes in the United States are
# listed in Table 2.1. Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the banknote of the entered amount.
# An appropriate error message should be displayed if no such note exists.
print("This program reads the denomination of a $ banknote and tells who is pictured at the banknote.")

# Create dictionary with denomination as key and personality as values
banknotes = {'1': 'George Washington', '2': 'Thomas Jefferson', '3': 'Abraham Lincoln', '20': 'Andrew Jackson',
             '10': 'Alexander Hamilton', '50': 'Ulysses S. Grant', '100': 'Benjamin Franklin'}

# Prompt user to enter the denomination of the banknote
banknote = str(input("Please enter the denomination of the $ banknote as numer here: "))

# If entered value corresponds to $ banknote denomination program prints out the person on the banknote
if banknote in banknotes.keys():
    personality = banknotes[banknote]
    print(f'On the ${int(banknote)} banknote {personality} is pictured.')
else:
    print("The value you have entered does not corresponds to any $ banknote denomination.")
