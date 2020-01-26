# Ex.115: Pig Latin. Solved 32 lines.
# Pig Latin is a language constructed by transforming English words. While the origins of the language are unknown,
# it is mentioned in at least two documents from the nineteenth century, suggesting that it has existed for more than
# 100 years. The following rules are used to translate English into Pig Latin:
# - If the word begins with a consonant (including y), then all letters at the beginning of the word, up to the first
#   vowel (excluding y), are removed and then added to the end of the word, followed by ay. For example, computer
#   becomes omputercay and think becomes inkthay.
# - If the word begins with a vowel (not including y), then way is added to the end of the word. For example,
#   algorithm becomes algorithmway and office becomes officeway.
# Write a program that reads a line of text from the user. Then your program should translate the line into Pig Latin
# and display the result. You may assume that the string entered by the user only contains lowercase letters and spaces.
print("This program makes translation from English to Pig Latin.\n")

CONSONANT = ('q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
VOWEL = ('e', 'u', 'i', 'o', 'a')
# Program prompts user to enter the string in English
user_string = str(input("Please enter your string in English here: "))
user_string = user_string.lower().strip()  # formats string entered by user to lowercase format and strips spaces if any
user_list = user_string.split()  # create list of words entered by user in string

# program loops through each word in list and makes translation
pig_latin_list = []
for word in user_list:
    # if wor starts with vowel the program just adds to the end of the words ending '-way'
    if word.startswith(VOWEL):
        word = word + 'way'
        pig_latin_list.append(word)  # translated word added to the list of translated words
    # if words starts with consonant
    if word.startswith(CONSONANT):
        # program translates the words, first finding the beginning of the translated words
        # stripping all consonants from the beginning of the word
        word_beginning = word.lstrip(r'q, w, r, t, y, p, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m')
        # than program finds the middle part of the word, which will be added after the begging of the translated word
        # this part contains all stripped consonants from the beginning  of the word in English
        word_middle = ''
        for l in word:
            if l in CONSONANT:      # if the letter is consonant
                word_middle += l    # this letter added to the middle part of the translated word
            if l not in CONSONANT:  # if program finds first vowel in the word it stops the iteration and adding letters
                break
        # program defines translated word by adding the translated beginning, middle of the wors and ending '-ay'
        word = word_beginning + word_middle + 'ay'
        # translated word added to the list of the translated words
        pig_latin_list.append(word)

# display the result of translation from entered by user string to English
print("\nYour string translated to Pig Latin is reads as: \n {}".format(' '.join(pig_latin_list)))
