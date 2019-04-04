# Ex 66: Compute a Grade Point Average. solved 62 lines.
# Exercise 51 included a table that shows the conversion from letter grades to grade points at a particular academic
# institution. In this exercise you will compute the grade point average of an arbitrary number of letter grades
# entered by the user. The user will enter a blank line to indicate that all of the grades have been provided. For
# example, if the user enters A, followed by C+, followed by B, followed by a blank line then your program should
# report a grade point average of 3.1. You may find your solution to Exercise 51 helpful when completing this exercise.
# Your program does not need to do any error checking. It can assume that each value entered by the user will always be
# a valid letter grade or a blank line.
print("This program shows average Grade points.")
# Prompt for user input
counter = 0
total_grades = 0
average_grade = None

while True:
    letter_grade = str(input("Please, enter the Letter grade for conversion to points (in range from A+ to F) here: "))
    if letter_grade == '':
        break
    elif letter_grade != '':
        letter_grade = letter_grade.upper()
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
        total_grades += point_grade
        counter += 1
# print(total_grades)
average_grade = total_grades / counter
# Display the of the program
if average_grade:
    print('The Average Grade points is equal to {0:.1f} Grade points.'.format(average_grade))
