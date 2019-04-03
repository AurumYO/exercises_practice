# Exercise 59: Is a License Plate Valid? In a particular jurisdiction, older license plates consist of three uppercase
# letters followed by three numbers. When all of the license plates following that pattern had been used, the format was
# changed to four numbers followed by three uppercase letters.
# Write a program that begins by reading a string of characters from the user. Then your program should display a
# message indicating whether the characters are valid for an older style license plate or a newer style license plate.
# Your program should display an appropriate message if the string entered by the user is not valid for either
# style of license plate.
print("This program detects if the licence is valid, and if it is of old or new style plate.")
license_plate = None
while not license_plate:
    try:
        license_plate = str(input("Please enter number of your license plate (letters  - uppercase) here: "))
        if len(license_plate) == 6:
            if license_plate[:3].isalpha() and license_plate[:3].isupper() and license_plate[3:].isdigit():
                license_type = 'an old'
            else:
                license_plate = None
                raise ValueError
        elif len(license_plate) == 8:
            if license_plate[:4].isalpha() and license_plate[:4].isupper() and license_plate[4:].isdigit():
                license_type = 'a new'
            else:
                license_plate = None
                raise ValueError
        else:
            license_plate = None
            raise ValueError
    except ValueError:
        print("The entered license number is not valid!!! Please check and try again...")

print("The License Plate NO.{} is valid license of {} style.".format(license_plate, license_type))
