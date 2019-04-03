# Ex45: What Color is that Square? Positions on a chess board are identified by a letter and a number. The letter
# identifies the column (a-h), while the number identifies the row (1-8).
# Write a program that reads a position from the user. Use an if statement to determine if the column begins with a
# black square or a white square. Then use modular arithmetic to report the color of the square in that row. F
# or example, if the user enters 'a1' then your program should report that the square is black. If the user enters 'd5'
# then your program should report that the square is white. Your program may assume that a valid position will always
# be entered. It does not need to perform any error checking.
print("This program say the color of the position on a chess board of size a1-h8.\n")

# Generate chess board as list with items as combination of letters and numbers
board = list()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for l in letters:
    for c in range(1, 9):
        position = l + str(c)
        board.append(position)

# Prompt user to enter the user's position
user_position = str(input("Please enter your position of the chess board: "))

# Define is position of the user is black or white
if user_position in board:
    user_posit_index = board.index(user_position)
    if user_posit_index == 0 or user_posit_index % 2 == 0:
        print("The color of %s position is black." % user_position)
    elif user_posit_index % 2 != 0:
        print("The color of %s position is black." % user_position)
