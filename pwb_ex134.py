# Ex. 134: Unique Characters. Solved—14 Lines.


# this function determains number of unique characters un a string.
def unique_char_counter(st):
    # set used to contain all characters which contains the string, as it is faster than dictionary and can
    # only contain unique characters
    char_dict = set()
    # loop through the string, if character has not previously found, it is added to the set
    for ch in st:
        if ch not in char_dict:
            char_dict.add(ch)
    # function returns as its result the lenght of the set with unique characters
    return len(char_dict)


# main function demonstrates the program performance
def main():
    assert unique_char_counter("Hello, World!") == 10
    assert unique_char_counter("zzzzz") == 1


if __name__ == '__main__':
    main()
