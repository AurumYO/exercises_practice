# Exercise 117: Line of Best Fit. Solved 41 lines. A line of best fit is a straight line that best approximates
# a collection of n data points. Each point in the collection has an (x, y) coordinate. ̄x and ȳ are average value.
# The line of best fit is represented by the equation y = mx + b where m and b are calculated using formulas:
# quation y = mx + b where m and b are calculated using
# the following formulas:
# m = (sum(x * y) - (sum(x) * sum(y)) / n) / (sum(x**2) - sum(x**2)/n)
# b = ȳ − m x̄
# program accepts input from user for x and for y from separate line
# program takes input until user enters blank line for x
# if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) the program should display y = 0.95x + 0.1

# define variables which will be used for calculations: list_x and list_y will contain values of x and y bases
list_x, list_y = [], []
# prompt user to input first coordinate on x base
x = input("Please, enter point for x coordinate: ")
# if entered x value by user is not  blank line, program will prompt user enter y and x coordinates,
# until blank line for x point is entered. each point added to the list with x or y points
while x != '':
    list_x.append(float(x))
    y = float(input("Please, enter point for y coordinate: "))
    list_y.append(y)
    x = input("Please, enter point for x coordinate: ")
# second stem, find m
# to calculate 'm' value we find n for the quantity of points on the line
n = len(list_y)
# find sum of all x and y points, sum of square x values, and sum of all x * y points
sum_x = sum(x for x in list_x)
sum_y = sum(y for y in list_y)
sum_square_x = sum(x ** 2 for x in list_x)
sum_xy = sum(x * y for x, y in zip(list_x, list_y))
# now we ready calculate m with formula given in task
m = (sum_xy - ((sum_x * sum_y) / n)) / (sum_square_x - (sum_x ** 2) / n)
# third step, we find meaning of 'b' by formula given in conditions, finding first average of all x and y points
# average of x and y points calculated as division of sum of all x or y points by number of points in line 'n'
av_x = sum_x / n
av_y = sum_y / n
b = av_y - av_x * m
# finally, forth step is display of the output
print("\nThe line of best fit is equal to: ")
print("y = {:.2f}x + {:.2f}".format(m, b))
