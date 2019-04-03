# Exercise 52: Grade Points to Letter Grade. In the previous exercise you created a program that converts a letter
# grade into the equivalent number of grade points. In this exercise you will create a program that reverses the
# process and converts from a grade point value entered by the user to a letter grade. Ensure that your program handles
# grade point values that fall between letter grades. These should be rounded to the closest letter grade. Your program
# should report A+ for a 4.0 (or greater) grade point average.
import math
print("This program converts Grade points to Letter grade.")
# Prompt for user input
point_grade = float(input("Please, enter the Grade points for conversion to Letters grade (from 0 to 4) here: "))
# Solution proposes to assign the letter grade to the points grade only when condition is met, not preliminary
# assigning the Grade points to Letter points to avoid unnecessary memory usage and creation of unused variables
letter_grade = None
if point_grade > 4.0:
    letter_grade = 'A+'
elif ((3.70 + 4.0)/2) <= point_grade <= 4.0:
    letter_grade = 'A'
elif ((3.3 + 3.7) / 2) <= point_grade <= ((3.70 + 4.0)/2):
    letter_grade = 'A-'
elif ((3.0 + 3.3) / 2) <= point_grade <= ((3.3 + 3.7) / 2):
    letter_grade = 'B+'
elif ((2.7 + 3.0) / 2) <= point_grade <= ((3.0 + 3.3) / 2):
    letter_grade = 'B'
elif ((2.3 + 2.7) / 2) <= point_grade <= ((2.7 + 3.0) / 2):
    letter_grade = 'B-'
elif ((2.0 + 2.3) / 2) <= point_grade <= ((2.3 + 2.7) / 2):
    letter_grade = 'C+'
elif ((1.7 + 2.0) / 2) <= point_grade <= ((2.0 + 2.3) / 2):
    letter_grade = 'C'
elif ((1.3 + 1.7) / 2) <= point_grade <= ((1.7 + 2.0) / 2):
    letter_grade = 'C-'
elif ((1.0 + 1.3) / 2) <= point_grade <= ((1.3 + 1.7) / 2):
    letter_grade = 'D+'
elif ((0 + 1.0) / 2) <= point_grade <= ((1.0 + 1.3) / 2):
    letter_grade = 'D'
elif point_grade == 0:
    letter_grade = 'F'
else:
    print("Wrong input!!! The Grade point you have entered is not valid!")
# Display the of the program
if letter_grade:
    print('The Grade point of {0} equals to "{1}" Letter grade.'.format(point_grade, letter_grade))
