# Exercise 151: Two Word Random Password. Solved in 37 lines.
# program that reads a file containing a list of words, randomly selects two of them, and concatenates them to produce
# a new password. Name of the file is read from user, than program reads all words from file line by line
from random import randint, choice
user_file = input("Please, enter the name of your file with words: ")
user_file = 'words.txt'
f = open(user_file, 'r')
list_words = []
lines = f.readlines()
for line in lines:
    line = line.strip()
    # split line by space
    line_words = line.split(' ')
    for word in line_words:
        # adds words which starts from letter and which length greater than 3 to list of words and capitalize the words
        if word not in list_words and len(word) >= 3 and word[0].isalpha():
            # Capitalize each word in so the user can easily see where one word ends and the next one begins
            word = word.capitalize()
            list_words.append(word)
# Define the length of the future password, ensure that the total length is between 8 and 10 characters
length_password = randint(8, 10)
password = ''
first_word = choice(list_words)
#  program continues to generate random words until random password with random length generated, concatenate two
# random words and checking that each word used is at least three letters long.
while len(password) < length_password:
    second_word = choice(list_words)
    if len(first_word) == 3:
        password = first_word + second_word[:length_password-3]
    elif length_password == 9:
        f_r = randint(4, 6)
        password = first_word[:f_r] + second_word[:9-f_r]
    else:
        password = first_word[:int(length_password/2)] + second_word[:(int(length_password/2))]

# Display the password for the user.
print("Your randomly generated password is: {} ".format(password))
