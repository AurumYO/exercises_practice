# Exercise 61: Average. In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate that no further values will
# be provided. Your program should display an appropriate error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the average.
print("This program computes the average in collection.")
stop = None
collection = []
while not stop:
    try:
        value = int(input("Please enter your number here or enter 0 to finish enter the numbers: "))
        if value == 0:
            stop = 1
        else:
            collection.append(value)
    except ValueError:
        continue
# calculation of the average number in the collection
sum_col = 0
for i in collection:
    sum_col += i
avg = sum_col / len(collection)
print('The average in the collection {0} is {1:.2f}.'.format(collection, avg))