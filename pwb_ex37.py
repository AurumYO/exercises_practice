# Exercise 37: Name that Shape. Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of a meaningful message.
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside
# of this range is entered then your program should display an appropriate error message.

print("This program will tell the name depending on the number of sides bewtween 3 and 10 sides")
print()

# Prompt user to give number of the sides of the figure
while True:
    sides = int(input("Plese enter the number of sides of your figure (between 3 and 10): "))
    print()
    if 3 <= sides <= 10:
        break
    else:
        print("Your input out of range from 3 to 10. Please try again!")

# create distionary with names of figures as keys and number of sides as values
figure_dict = {'triangle': 3, 'tetragon': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octogon': 8, 'enneagon': 9,
               'decagon': 10}

# Define name of the figure (alternatively we cound name each as separate variable and display as if/elif/else)
for k, v in figure_dict.items():
    if v == sides:
        print(f"The shape with {sides} sides is called {k}.")
