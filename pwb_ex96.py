# Exercise 96: Check a Password. Solved 40 lines.
# In this exercise you will write a function that determines whether or not a password is good. We will define a good
# password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one
# lowercase letter, and at least one number. Your function should return true if the password passed to it as
# its only parameter is good. Otherwise it should return false. Include a main program that reads a password from
# the user and reports whether or not it is good. Ensure that your main program only runs when your solution
# has not been imported into another file.


def password_check(string):  # function takes password as string and verifies if it is good or not
    number = 0               # variable number to count if there is a digit in the password
    small_letter = 0         # variable small_letter to count if there is a lower case letter in the password
    upper_letter = 0         # variable upper_letter to count if there is a upper case letter in the password

    for char in string:      # with for loop function check each character in the given password
        if char.isdigit():   # if character in password is a digit
            number += 1      # counter of numbers increased by 1
        if char.islower():     # if character in password is a lower case letter
            small_letter += 1  # counter of lower case letters increased by 1
        if char.isupper():     # if character in password is a upper case letter
            upper_letter += 1  # counter of upper case letters increased by 1
    # function check if length of the password is >= 8 and if there is at least 1 digit, 1 lower case and 1 upper case
    # in the password and returns True, which means the password is good and False is password is bad
    if len(string) >= 8 and number > 0 and small_letter > 0 and upper_letter > 0:
        return True
    else:
        return False


def main():
    password = str(input("Please enter your password here: "))  # prompt user to input the password for check
    password_check_result = password_check(password)            # call of the password check function
    if password_check_result:
        print("Your password is good.")                         # if password is good displayed appropriate message
    else:
        print("your password is bad.")                          # otherwise the password is bad and appropriate message


if __name__ == '__main__':
    main()
