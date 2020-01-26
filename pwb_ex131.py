# Ex 131. Morse code. solved 15 lines.


# This function accepts the text message as string and translates it to morse code. Translated only letters and digits
def morse_translate(message):
    # create dictionary with morse code alphabet
    morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    # in new variable save message in uppercase to mach morse alphabet
    up_message = message.upper()
    # message in morse format will be stored in morse_message string variable
    morse_message = ''
    # loop through the uppercase message. if character matches the key in dictionary, corresponding translated
    # value in morse appended to the end of string in morse code + space character
    for ch in up_message:
        if ch in morse_alphabet:
            morse_message += morse_alphabet[ch] + ' '
    # message translated to morse language return as the result of the function
    return morse_message


# Main function makes demonstration of the morse code translation function.
def main():
    message = "Hello World!\n"
    print("The message : \n", message, 'translated to morse code as:')
    print(morse_translate(message))


if __name__ == '__main__':
    main()
