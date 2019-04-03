# Exercise 41: Note To Frequency. The following dictionary lists an octave of music notes, beginning with middle C,
# along with their frequencies. Begin by writing a program that reads the name of a note from the user and displays the
# note’s frequency. Your program should support all of the notes listed previously.
notes = { 'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88}

# Create list with names of all notes for further check if entered value is note
note_names = list()
for n in notes:
    note_names.append(n[0])

#  Prompt user to enter the note
ent_note = str(input("Please enter the name of the note: "))

# Define name of the note and octave range
note, octave = ent_note[0], int(ent_note[1])

if note not in note_names:
    print("The name of the music note you have entered does not exists.")

# Print out the frequency of the inputted note in Hz
for n in notes:
    if ent_note in notes.keys() and ent_note == n:
        frequency = notes[n]
        print("The frequency of your note {} is {} Hz.".format(ent_note, frequency))
    elif ent_note not in notes.keys():
        if note == n[0]:
            base_frequency = notes[n]
            frequency = base_frequency / 2 ** (4 - octave)
            print("The frequency of your note {} is {} Hz.".format(note, frequency))






