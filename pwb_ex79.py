# Ex 79: Maximum Integer. (Solved—34 Lines)
# This exercise examines the process of identifying the maximum value in a collection
# of integers. Each of the integers will be randomly selected from the numbers between 1 and 100.
# Create a program that begins by selecting a random integer between 1 and 100. Save this integer as the maximum number
# encountered so far. After the initial integer selected, generate 99 additional random integers between 1 and 100.
# Check each integer as it is generated to see if it is larger than the maximum number encountered so far. If it is
# then your program should update the maximum number encountered and count the fact that you performed an update.
# Display each integer after you generate it. Include a notation with those integers which represent a new maximum.
# After you have displayed 100 integers your program should display the maximum value encountered, along with the number
# of times the maximum value was updated during the process.
from random import randint
print("This program examines and finds maximum integer of random sequence.")
# first generate first random number, initiate counter of generated numbers, calculator for updates and max number
number = randint(1, 100)
counter = 1
update = 0
max_number = number
# through while generate new numbers and compare generated value with previous one
while counter < 100:
    number = randint(1, 100)
    if number > max_number:
        max_number = number
        print(number, '<== Update')
        update += 1
        counter += 1
    elif number <= max_number:
        print(number)
        counter += 1
# print out the result of program's computations
print("The maximum number found is", max_number)
print("The maximum number has been updated", update, "times.")
