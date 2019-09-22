# Exercise 36: Vowel or Consonant. In this exercise you will create a program that reads a letter of the alphabet from
# the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered
# letter is a vowel. If the user enters y then program should display a message indicating that sometimes y is a vowel,
# and sometimes y is a consonant. Otherwise program should display a message indicating that the letter is a consonant.
import string

print("this program will tel if the letter is vowel or consonant.")
print()

# Prompt user to input a letter from alphabet
letter = str(input("Please enter any letter from alphabet: "))
print()

# Create list of wowels and separate 'y' character
alphabet = list(string.ascii_lowercase)
vowels = ['a', 'e', 'u', 'i', 'i', 'o']
letter_y = 'y'

# Generate list with consonant letters
consonant = alphabet.copy()
consonant.remove('y')
for l in consonant:
    if l in vowels:
        consonant.remove(l)

while letter not in alphabet:
    print("The value you have entered is not alphabetical value! Please try again.")
    letter = str(input("Please enter any letter from alphabet: "))

if letter in vowels:
    print(f"The letter {letter} is vowel.")
elif letter in consonant:
    print(f"The letter {letter} is consonant.")
elif letter == letter_y:
    print(f"The letter {letter} sometimes is a vowel, and sometimes is a consonant.")
else:
    print(f"The {letter} is not in English alphabet.")
