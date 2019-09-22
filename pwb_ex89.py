# Ex 89: Capitalize It. solved 48 lines.
# Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this
# exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be
# replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string
# should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the
# function is provided with the string “what time do i have to be there? what’s the address?” then it should return the
# string “What time do I have to be there? What’s the address?”. Include a main program that reads a string from the
# user, capitalizes it using your function, and displays the result.
print("This program makes proper letter capitalization.")


def capitalization_maker(string):
    cap_string = str()                       # create new string to which correctly capitalized letters will be added
    signs = ['.', '!', '?']                  # create list with punctuation signs for check if new sentence started
    counter = 0
    for i in string:                         # program loops through each character of the string
        counter += 1                         # counter introduced to count the position of each looped character
        if counter == 1:                     # if first character than the letter must be capitalized
            cap_string += i.upper()          # add to our new string correctly capitalized letter
        elif i == ' ':
            cap_string += i
        elif i == 'i' and string[counter] == ' ' and string[counter - 2] == ' ':  # if character is 'i' with ' ' around
            cap_string += i.upper()                                               # 'i' letter should be capitalized
        elif string[counter-2] == ' ' and string[counter-3] in signs:  # if before letter is sign and whitespace
            cap_string += i.upper()                                    # letter is capitalized since it is new sentence
        else:
            cap_string += i                  # in all other cases characters added without modification
    return cap_string                        # program returns correctly capitalized sentence


def main():
    string = 'whati time do i ihave to be there? what’s the address?'
    print('\n Making program execution...\n The inserted string is: {}\n'.format(string))
    print(capitalization_maker(string))


main()
