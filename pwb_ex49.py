# Exercise 49: Richter Scale. The table contains earthquake magnitude ranges on the Richter scale and
# their descriptors. Write a program that reads a magnitude from the user and displays the appropriate descriptor
# as part of a meaningful message. For example, if the user enters 5.5 then your program should indicate that a
# magnitude 5.5 earthquake is considered to be a moderate earthquake.
print("This program reads the earthquake magnitude and displays the appropriate descriptor by Richter scale.")
# Read the input from user
magnitude = float(input("Please, enter the magnitude of the earthquake value here: "))
# Define the magnitude through if/elif
if magnitude < 2.0:
    earthquake = "Micro"
elif 2.0 <= magnitude < 3.0:
    earthquake = 'Very'
elif 3.0 <= magnitude < 4.0:
    earthquake = 'Minor'
elif 4.0 <= magnitude < 5.0:
    earthquake = 'Light'
elif 5.0 <= magnitude < 6.0:
    earthquake = 'Moderate'
elif 6.0 <= magnitude < 7.0:
    earthquake = 'Strong'
elif 7.0 <= magnitude < 8.0:
    earthquake = 'Major'
elif 8.0 <= magnitude < 10.0:
    earthquake = 'Great'
elif magnitude >= 10.0:
    earthquake = 'Meteoric'
print("The earthquake with marnitude %0.1f it is %s minor earthquake." % (magnitude, earthquake))
