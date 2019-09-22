# Exercise 94: Random Password. solved 33 lines
#  Write a function that generates a random password. The password should have a random length of between 7 and 10
#  characters. Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function
#  will not take any parameters. It will return the randomly generated password as its only result. Display the randomly
#  generated password in your file’s main program. Your main program should only run when your solution has not been
#  imported into another file.
# Hint: You will probably find the chr function helpful when completing this exercise. Detailed information
# about this function is available online.
from random import randint

# this function generates random password from characters with positions 33 to 126 in the ASCII table
# with random length between 7 and 10 characters


def generate_random_password():
    password = ''
    password_lengh = randint(7, 10)  # randomly chosen length of the password from 7 to 10 characters
    # -- alternative solution --
    # for t in range(password_lengh):
    #     sign = chr(randint(33, 126))
    #     password = password + sign
    while len(password) < password_lengh:  # loop runs until number of characters in password equal to password length
        sign = chr(randint(33, 126))  # in loop it is generated random characters with positions 33 to 126 in ASCII
        password = password + sign  # randomly chosen character concatenated to the password
    return password  # function returns the password as string


def main():
    print("Your randomly generated password is: ", generate_random_password())


if __name__ == '__main__':
    main()
