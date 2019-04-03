# Exercise 51: Letter Grade to Grade Points. Write a program that begins by reading a letter grade from the user. Then
# your program should compute and display the equivalent number of grade points. Ensure that your program generates an
# appropriate error message if the user enters an invalid letter grade.
print("This program converts Letter grade to Grade points.")
# Prompt for user input
letter_grade = str(input("Please, enter the Letter grade for conversion to points (in range from A+ to F) here: "))
letter_grade = letter_grade.upper()
# Solution proposes to assign the value to the points grade only when condition is met, not preliminary
# assigning the Grade points to Letter points to avoid unnecessary memory usage and creation of unused variables
point_grade = None
if letter_grade == 'A+' or letter_grade == 'A':
    point_grade = 4.0
elif letter_grade == 'A-':
    point_grade = 3.7
elif letter_grade == 'B+':
    point_grade = 3.3
elif letter_grade == 'B':
    point_grade = 3.0
elif letter_grade == 'B-':
    point_grade = 2.7
elif letter_grade == 'C+':
    point_grade = 2.3
elif letter_grade == 'C':
    point_grade = 2.0
elif letter_grade == 'C-':
    point_grade = 1.7
elif letter_grade == 'D+':
    point_grade = 1.3
elif letter_grade == 'D':
    point_grade = 1.0
elif letter_grade == 'F':
    point_grade = 0
else:
    print("Wrong input!!! The Letter grade you have inputted is not valid!")
# Display the of the program
if point_grade:
    print('The Letter grade of "{0}" equals to {1} Grade points.'.format(letter_grade, point_grade))
