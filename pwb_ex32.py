# Exercise 32: Sort 3 Integers. Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest and largest values.
# The middle value can be found by computing the sum of all three values, and then subtracting the minimum value and
# the maximum value.

print("This program that reads 3 integers and displays them in sorted order.")
print()

# Ask for user input of three integers
integers_str = str(input("Please enter your three integers, using comma separator: "))
print()

# convert the result of input into iterable list of integers
integers = integers_str.split(',')

# Look for minimal integer with min(), max() function
min_int = int(min(integers))
max_int = int(max(integers))

# Looking for midle value according to the terms of the excersize: computing the sum - minimum value - maximum value
sum_integers = 0
for i in integers:
    sum_integers += int(i)
middle_value = sum_integers - min_int - max_int

# display the results
print("The minimal value of three integers is ", min_int, ".")
print("The middle value of three integers is ", middle_value, ".")
print("The minimal value of three integers is ", max_int, ".")
