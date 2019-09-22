# Exercise 34: Even or Odd. Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

print("This program will tel if your number is even or odd.")

# Ask input of the number from user
number = int(input("Please enter your number: "))

# define if number is even or odd
if number % 2 == 0 or number == 0:
    print(f"Entered number '{number}' is even.")
elif number % 2 != 0:
    print(f"Entered number '{number}' is odd.")

# solution form book
if number % 2 == 1:
    print(f"By book the entered number '{number}' is odd.")
else:
    print(f"By book the entered number '{number}' is even.")