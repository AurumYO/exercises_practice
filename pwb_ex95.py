# Ex 95: Random License Plate. Solved 45 lines.
# In a particular jurisdiction, older license plates consist of three letters followed by three numbers. When all of
# the license plates following that pattern had been used, the format was changed to four numbers followed by
# three letters.
# Write a function that generates a random license plate. Your function should have approximately equal odds of
# generating a sequence of characters for an old license plate or a new license plate. Write a main program that calls
# your function and displays the randomly generated license plate.
from random import choice, randint

# function generates randomly type of license and its number


def random_license_plate():
    license_plate = ''  # create empty variable for License plate number
    license_type = choice(['old', 'new'])  # the type of license selected randomly

    if license_type == 'old':  # if randomly selected type is old for license
        letter_plate = ''.join(chr(randint(65, 90)) for x in range(3))  # than first randomly selected 3 letters
        number_plate = ''.join(chr(randint(48, 57)) for x in range(3))  # secondly randomly selected 3 numbers
        # number of license formed by adding randomly chosen 3 letters and 3 numbers
        license_plate = letter_plate + number_plate

    if license_type == 'new':  # if randomly selected type is new for license
        number_plate = ''.join(chr(randint(48, 57)) for x in range(3))  # than first randomly selected 3 numbers
        letter_plate = ''.join(chr(randint(65, 90)) for x in range(3))  # secondly randomly selected 3 letters
        # number of license formed by adding randomly chosen 3 numbers  and 3 letters
        license_plate = number_plate + letter_plate

    return license_plate  # funcition returns rndomly generates number of the license


def main():
    # main function when called generates random number of the License plate
    print("Your randomly chosen License Plate is {}.".format(random_license_plate()))


if __name__ == '__main__':
    main()
