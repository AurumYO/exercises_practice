# Ex. 146:xercise 146: Letter Frequencies. Solved in 43 Lines.
# This analysis examines the encrypted text to determine which characters are most common.
# Write a program that initiates this process by determining and displaying the
# frequencies of all letters in a file.

# The user will provide the file name as a command line parameter.
user_file = input("Please, enter the name of your file here to read: ")
# open the provided by user file
try:
    f = open(user_file, 'r')
    # read lines in file, all letters will be stored in dictionary with letters as keys and their occurrences as values
    letters = {}
    lines = f.readlines()
    # program goes through each line in text, making each letter uppercase treating a and A as equivalent
    for line in lines:
        line = line.upper()
        # than goes through each line in file
        for ch in line:
            # check if character is letter, ignore spaces, punctuation marks, and numbers while performing this analysis
            # is already in dictionary, programs increases the occurrence by 1
            if ch.isalpha() and ch in letters.keys():
                letters[ch] += 1
            # and if character not in dictionary adding the letter as key and occurrence as 1
            if ch.isalpha() and ch not in letters.keys():
                letters[ch] = 1
    # find most common character in the file, and find occurrence of the most common letters in English, such as E and T
    most_common_times = 0
    # e_occurrence, t_occurrence, most_common_letter = 0, 0, 0
    for k, v in letters.items():
        # displaying the frequencies of all letters in a file
        print("- letter {} occurred in file {} times,".format(k, v))
        if v > most_common_times:
            most_common_letter = k
            most_common_times = v
        if k == 'E':
            e_occurrence = v
        if k == 'T':
            t_occurrence = v
    # Display most common letters in file and occurence of English E and T in file
    print("The occurrence of the most common letters in English 'E' an 'T' is {} and {} times respectively."
          .format(e_occurrence, t_occurrence))
    print("The most common letter in file {} is {} occurring {} times in file.".format(user_file, most_common_letter,
                                                                                       most_common_times))
# report the problem if no such file or any errors with accessing the file
except IOError:
    print("No such file or error while accessing the file with name!!!")
