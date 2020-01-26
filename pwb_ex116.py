# Ex 116. Improved Pig latin. solved 51 lines.
# Extend your solution to Exercise 115 so that it correctly handles uppercase letters and punctuation marks such as
# commas, periods, question marks and exclamation marks. If an English word begins with an uppercase letter then its
# Pig Latin representation should also begin with an uppercase letter and the uppercase letter moved to the end of
# the word should be changed to lowercase. For example, Computer should become Omputercay. If a word ends in a
# punctuation mark then the punctuation mark should remain at the end of the word after the transformation has been
# performed. For example, Science! should become Iencescay!

print("This program makes translation from English to Pig Latin.\n")

CONSONANT = ('q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
             'Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')
VOWEL = ('e', 'u', 'i', 'o', 'a', 'E', 'U', 'I', 'O', 'A')
# Program prompts user to enter the string in English
user_string = str(input("Please enter your string in English here: "))
user_string = user_string.strip()  # formats string entered by user to lowercase format and strips spaces if any
user_list = user_string.split()  # create list of words entered by user in string
# program loops through each word in list and makes translation
pig_latin_list = []

# This function finds punctuation in the end of each  word
def ending_finder(word):
    ending = ''
    for l in word:
        if l in (',', '.', '!', '?'):
            ending = ending + l
    return ending

for word in user_list:
    # if wor starts with vowel the program just adds to the end of the words ending '-way'
    if word.startswith(VOWEL):
        ending = ending_finder(word)          # looks if punctuation is in the end of the word
        word = word.rstrip(r'?,.!') + 'way'
        pig_latin_list.append(word + ending)  # translated word added to the list of translated words
    # if words starts with consonant
    if word.startswith(CONSONANT):
        # program translates the words, first finding the beginning of the translated words
        # stripping all consonants from the beginning of the word
        ending = ending_finder(word)         # looks if punctuation is in the end of the word
        word = word.rstrip(r'?,.!')
        if word[0].isupper():
            word_beginning = word.lstrip(r'q, w, r, t, y, p, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m,  Q, W, R, T, '
                                         r'Y, P, S, D, F, G, H, J, K, L, Z, X, C, V, B, N, M').capitalize()
        else:
            word_beginning = word.lstrip(r'q, w, r, t, y, p, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m,  Q, W, R, T,'
                                         r' Y, P, S, D, F, G, H, J, K, L, Z, X, C, V, B, N, M')
        # than program finds the middle part of the word, which will be added after the begging of the translated word
        # this part contains all stripped consonants from the beginning  of the word in English
        word_middle = ''
        for l in word:
            if l in CONSONANT and l not in (',', '.', '!', '?'):      # if the letter is consonant
                word_middle += l    # this letter added to the middle part of the translated word
            if l not in CONSONANT:  # if program finds first vowel in the word it stops the iteration and adding letters
                break
        # program defines translated word by adding the translated beginning, middle of the wors and ending '-ay'
        word = word_beginning + word_middle.lower() + 'ay' + ending
        # translated word added to the list of the translated words
        pig_latin_list.append(word)

# display the result of translation from entered by user string to English
print("\nYour string translated to Pig Latin is reads as: \n {}".format(' '.join(pig_latin_list)))
