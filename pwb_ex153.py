# Exercise 153: A Book with No “e” ... (Solved—49 Lines)

# The name of the input file will be read from the user
from typing import Any, Union

name_file = input("Please enter the name of the file to open: ")
# program reads a list of words from a file and determines what proportion of the words use each letter of the alphabet
try:
    # open file and read lines from file
    f = open(name_file, 'r')
    lines = f.readlines()
    # create dictionary with letters of English alphabet as keys and number of words in which letter occurred as values
    letters_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
    # program ignores any punctuation marks and treat uppercase and lowercase letters as equivalent
    for line in lines:
        line = line.strip().lower()
        words = line.split(' ')
        # if program finds that letter occurred in word it increases number of letter occurrence oin word by 1
        for k in letters_dict.keys():
            for word in words:
                if k in word:
                    letters_dict[k] += 1
    f.close()

    # Display the result for all 26 letters
    for k, v in letters_dict.items():
        print("The letter {} occured {} times in file.".format(k, v))

    # least common letters will be stored in list in case they are more than one
    least_common_letter = []
    # Identifying the letter that is used in the smallest proportion of the words.
    least_common = min(letters_dict.values())
    # find letters which occurred the less time in file
    for l, v in letters_dict.items():
        if v == least_common:
            least_common_letter.append(l)
    # Display the letter which occurred in least words and number of such words
    print("The least common letter(s) in file {} occurred in {} words.".format(least_common_letter, least_common))
# raising exception if was error with accessing the file or no file found
except IOError:
    print("Error occurred while accessing the file with such name!!!")
