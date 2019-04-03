# Exercise 42: Frequency To Note. In the previous question you converted from note name to frequency. In this question
# you will write a program that reverses that process. Begin by reading a frequency from the user. If the frequency
# is within one Hertz of a value listed in the table in the previous question then report the name of the note.
# Otherwise report that the frequency does not correspond to a known note. In this exercise you only need to consider
# the notes listed in the table. There is no need to consider notes from other octaves.
C4, D4, E4, F4, G4, A4, B4 = 261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88

# Ask user to input frequency of the note in Hz
frequency = round(float(input("Please, enter the frequency of the note in Hz: ")), 2)
if D4 > frequency >= C4:
    print("Your frequency is in range of note 'C4'.")
if E4 > frequency >= D4:
    print("Your frequency is in range of note 'D4'.")
if F4 > frequency >= E4:
    print("Your frequency is in range of note 'E4'.")
if G4 > frequency >= F4:
    print("Your frequency is in range of note 'F4'.")
if A4 > frequency >= G4:
    print("Your frequency is in range of note 'G4'.")
if B4 > frequency >= A4:
    print("Your frequency is in range of note 'A4'.")
if A4 < frequency <= B4:
    print("Your frequency is in range of note 'B4'.")
if frequency < C4 or frequency > B4:
    print("The not are not in rango of first octav.")

