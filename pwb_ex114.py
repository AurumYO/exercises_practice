# Exercise 114: Random Lottery Numbers. Solved 28 lines
# In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket to the 6
# numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection
# of 6 numbers for a lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
# Display the numbers in ascending order.

# import from random module the generator of random integers
from random import randint

# create empty list for storing lottery numbers
lottery_numbers = []
# program will be generating random integers in range between 1 and 49 and adding them to the lottery list and will
# avoid adding duplicates to the lottery list
while len(lottery_numbers) < 6:
    n = randint(1, 49)
    if n not in lottery_numbers:
        lottery_numbers.append(n)

# after program generated 6 random non-duplicating integers, program sort the integers in ascending order
lottery_numbers = sorted(lottery_numbers)

# program displays the winning numbers of the lottery in string readable format
print("The  winning numbers for a lottery ticket are: {}!".format(str(lottery_numbers)[1:-1]))
