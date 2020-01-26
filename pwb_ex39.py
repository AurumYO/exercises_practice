# Exercise 39: Sound Levels. The following table lists the sound level in decibels for several common noises.
# Noise (Decibel level (dB)): Jackhammer (130), Gas lawnmower (106), Alarm clock(70), Quiet room (40).
# Write a program that reads a sound level in decibels from the user. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a value larger than the
# loudest noise in the table.

print("This program defines the level of moise in dB.")

# Prompring for the user input of noise level in dB
noise = int(input("Please enter the level of noise in dB here: "))
# display a message containing only that noise which is entered by user in dB
if noise > 130:
    print("The level of sound is louder than Jackhammer!")
if noise == 130:
    print("The level of sound is described as Jackhammer!")
if 106 < noise < 130:
    print("The level of sound is louder than as Gas lawnmower but lower than Jackhammer!")
if noise == 106:
    print("The level of sound is described as Gas lawnmower!")
if 70 < noise < 106:
    print("The level of sound is louder than as Alarm clock but lower than Gas lawnmower!")
if noise == 70:
    print("The level of sound is described as Alarm clock!")
if 40 < noise < 70:
    print("The level of sound is louder than as Quiet room but lower than Alarm clock!")
if noise == 40:
    print("The level of sound is as in Quiet room!")
if 40 < noise < 70:
    print("The level of sound is even quieter than in Quiet room!")
