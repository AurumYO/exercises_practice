# Ex. 80: Coin Flip Simulation (47 Lines)
# Create a program that uses Python’s random number generator to simulate flipping a coin several times.
# The simulated coin should be fair, meaning that the probability of heads is equal to the probability of tails.
# Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur.
# Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes shown
# on the same line. Then display the number of flips needed to reach 3 consecutive flips with the same outcome.
# When your program is run it should perform the simulation 10 times and report the average number of flips needed.
from random import choice
print("This program performs coins flip simulation.")
sequence, counter_flips = 0, 0
previous_flip = None
flips_counter = 0
# perform 10 sets of flips until 3 consecutive heads of 3 consecutive tails occur
for x in range(10):
    # while loop makes flips until 3 occurrences appear
    while sequence < 2:  # make flips until 3 consecutive heads of 3 consecutive tails occur
        flip = choice(['H', 'T'])
        counter_flips += 1
        print(flip, end=' ')
        if flip == previous_flip:
            sequence += 1
        if flip != previous_flip:
            sequence = 0
        previous_flip = flip
    print((counter_flips, 'flips'))
    # after 3 occurrences appear we add total amount of flips in set to total flips counter and reset counters
    flips_counter += counter_flips
    previous_flip = None
    sequence, counter_flips = 0, 0

average_flips = flips_counter / 10  # calculate average number of flips to get  consecutive occurrences
print("On average,", average_flips, "flips were needed.")  # display the output of the program
