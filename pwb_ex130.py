# Exercise 130: Text Messaging (21 Lines)
# Pressing the number once generates the first letter on the key. Pressing the number 2, 3, 4 or 5 times generates
# the second, third, fourth or fifth character listed for that key.


# This function translates message from text to numeric keypad. program handles both uppercase and lowercase letters.
# semicolons and brackets are ignored
def numeric_to_readable(text_message):
    # dictionary that maps from each letter or symbol to the key presses
    key_dictionary = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ',
                      0: ' '}
    # unify all letters to uppercase for adjusting to the phone keyboard
    upper_message = text_message.upper()
    # empty string numeric_message will contain all numeric presses which user need to press to enter the message
    numeric_message = ''
    # loop through each character in the user's massage
    for ch in upper_message:
        # loop through dictionary with letter or symbol to the key presses
        for k, v in key_dictionary.items():
            # if character in the value of the dictionary
            if ch in v:
                # define the key in the dictionary where character occur and position of the character in the value + 1
                position = key_dictionary[k].index(ch) + 1
                # numeric press will be correspondent to the key where character occurred multiplied by its position
                numb = str(k) * position
                # add numeric press to string with all numeric presses which user need to press to enter the message
                numeric_message = numeric_message + numb
                # stop sear in the dictionary if we found numeric press for searched character
                break
    # return the numeric presses for the user’s message
    return numeric_message


# main function prompts user to enter the numeric message and display the message in text format
def main():
    # TEST, if the user enters Hello, World! then program should output 4433555555666110966677755531111.
    assert numeric_to_readable('Hello, World!') == '4433555555666110966677755531111', 'Test passed'
    # prompt user to enter the text message
    user_message = input("Please enter letter or enter for new letter:")
    # display the numeric presses for the user’s message
    print("The numeric presses for entering the message on the phone are: {}".format(numeric_to_readable(user_message)))


if __name__ == '__main__':
    main()
