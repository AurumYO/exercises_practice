# Exercise 60: Roulette Payouts. A roulette wheel has 38 spaces on it: 18 are black, 18 are red, and two are green.
# The green are 0 and 00, red are (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34, 36), remaining
# between 1 and 36 are black. Many different bets can be placed in roulette. We will only consider the following
# subset of them in this exercise:
# • Single number (1 to 36, 0, or 00); Red versus Black; Odd versus Even (0 and 00 not pay out for even);
# 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using Python’s random number generator. Display number
# that was selected and all of the bets that must be payed. For example, if 13 is selected -  program should display:
# The spin resulted in 13...
# - Pay 13
# - Pay Black
# - Pay Odd
# - Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or 00 without any further output.
import random
print("This program indicates Roulette Payouts.")
red = ('Red', [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
black = ('Black', [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])
green = ('Green', [0, '00'])
spin = random.choice(red[1] + black[1] + green[1])
print("The spin resulted in {}...".format(spin))

# Print the winning point
if spin in green[1]:
    print("Pay", spin)
    exit()
else:
    print("Pay", spin)

# Define if Odd or Even
if spin % 2 == 0:
    num = 'Even'
elif spin % 2 != 0:
    num = 'Odd'

# Print our color, Odd or Even
if spin in red[1]:
    color = red[0]
    print("Pay " + color)
    print("Pay", num)
elif spin in black[1]:
    color = black[0]
    print("Pay " + color)
    print("Pay", num)

# Define range of winning spin
if spin <= 18:
    print("Pay 1 to 18")
if spin > 18:
    print("Pay 19 to 36")
