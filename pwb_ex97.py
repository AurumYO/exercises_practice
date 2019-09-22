# Ex. 97 Using your solutions to Exercises 94 and 96, write a program that generates a random good password and
# displays it. Count and display the number of attempts that were needed before a good password was generated.
# Structure your solution so that it imports the functions you wrote previously and then calls them from a function
# named main in the file that you create for this exercise.
from pwb_ex94 import generate_random_password
from pwb_ex96 import password_check

# Program generates good password with length at least 8 characters and password has
# at leas 1 upper case and lower case letter, and at least 1 digit.
# function use imported functions to generate randomly the password and to check if the password is good
# number of attempts to  generated is calculated. Function runs until good password is found


def generate_good_password():
    checked_password = False
    counter = 0
    while not checked_password:
        counter += 1
        generated_password = generate_random_password()
        checked_password = password_check(generated_password)
        if checked_password:
            return generated_password, counter                # function returns good password and number of attempts

# Main function runs the function to generate good password and displays the good password and
# number of attempts needed before generate of good password

def main():
    password, counter = generate_good_password()
    print("The good password is {} and it was generated after {} attempt.".format(password, counter))


if __name__ == '__main__':
    main()
