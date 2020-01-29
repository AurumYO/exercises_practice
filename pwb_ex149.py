# Ex. Both Letter Grades and Grade Points. Solved in 106 lines.
print('This program converts from letter grades to grade points and vice-versa.')

# prompt user to enter grade value
user_grade = input("Please enter your Letter or Points Grade here or blank line to  exit: ")

# program will convert multiple values entered by the user, with one value entered on each line.
# program continues performing conversions until the user enters a blank line.
while user_grade != '':

    # Set values of point grades and letter grades to None, to disregard previous results of conversion
    point_grade, letter_grade = None, None
    # dictionary will contain letter grades as keys and their point equivalents in values
    point_grades = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                    'D+': 1.3, 'D': 1.0, 'F': 0}

    try:
        # first, try to convert each value entered by the user from a number of grade points to a letter grade.
        if user_grade.isdigit():
            user_grade = float(user_grade)
            if user_grade > 4.0:
                letter_grade = 'A+'
            elif ((3.70 + 4.0) / 2) <= user_grade <= 4.0:
                letter_grade = 'A'
            elif ((3.3 + 3.7) / 2) <= user_grade <= ((3.70 + 4.0) / 2):
                letter_grade = 'A-'
            elif ((3.0 + 3.3) / 2) <= user_grade <= ((3.3 + 3.7) / 2):
                letter_grade = 'B+'
            elif ((2.7 + 3.0) / 2) <= user_grade <= ((3.0 + 3.3) / 2):
                letter_grade = 'B'
            elif ((2.3 + 2.7) / 2) <= user_grade <= ((2.7 + 3.0) / 2):
                letter_grade = 'B-'
            elif ((2.0 + 2.3) / 2) <= user_grade <= ((2.3 + 2.7) / 2):
                letter_grade = 'C+'
            elif ((1.7 + 2.0) / 2) <= user_grade <= ((2.0 + 2.3) / 2):
                letter_grade = 'C'
            elif ((1.3 + 1.7) / 2) <= user_grade <= ((1.7 + 2.0) / 2):
                letter_grade = 'C-'
            elif ((1.0 + 1.3) / 2) <= user_grade <= ((1.3 + 1.7) / 2):
                letter_grade = 'D+'
            elif ((0 + 1.0) / 2) <= user_grade <= ((1.0 + 1.3) / 2):
                letter_grade = 'D'
            elif user_grade == 0:
                letter_grade = 'F'

        # If exception occurs during the attempt then, program attempts to convert the user's value
        # from a letter grade to a number of grade point
        if user_grade in point_grades.keys():
            point_grade = point_grades[user_grade]

    # If both conversions fail then program provide a message indicating that the supplied input is invalid.
    except ValueError:
        print("The entered value is not a Letter or Points Grade!!!")

    # If program succeeded to make conversion, the appropriate display of the value of the corresponding grade appear
    if point_grade:
        print("Your grade {} is Letter Grade and is equal to {} in Point Grades.".format(user_grade, point_grade))
    if letter_grade:
        print("Your grade {} is Point Grade and is equal to {} in Letter Grades.".format(user_grade, letter_grade))
    # and program continues to prompt user for another input of grade
    user_grade = input("Please enter your Letter or Points Grade here or blank line to  exit: ")
