# Ex 136. Anagrams Again. solved in 48 Lines.


# This function defines if two strings with multiple words are anagrams (if they contain all of the same letters, but
# in a different order. Capitalization, punctuation marks and spacing are ignored
# Program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.
def anagram_definer(f_str, s_str):
    # both strings reverted to lowercase and spaces removed
    f_str = f_str.lower().replace(' ', '')
    s_str = s_str.lower().replace(' ', '')
    # program use two dictionary to compare two strings
    f_dict, s_dict = {}, {}
    # go through each string, and add each character to dictionary as key and number that it is occurred as value
    # if character is not letter or number, it is disregarded and not added to the dictionary
    for ch in f_str:
        if ch not in f_dict and ch.isalnum():
            f_dict[ch] = 1
        if ch in f_dict and ch.isalnum():
            f_dict[ch] += 1
    for ch in s_str:
        if ch not in s_dict and ch.isalnum():
            s_dict[ch] = 1
        if ch in s_dict and ch.isalnum():
            s_dict[ch] += 1
    # if in result both dictionaries for each string is equal program returns True if strings are anagrams or
    # it returns False if the two strings are not anagrams
    if f_dict == s_dict:
        return True
    else:
        return False


# Main function demonstrates function performance
def main():
    assert anagram_definer('William Shakespeare', 'I am a weakish speller') == True
    assert anagram_definer('banana', 'kiwi') == False
    user_first = input("Please enter your first string here: ")
    user_second = input("Please enter your second string here: ")
    res = anagram_definer(user_first, user_second)
    if res:
        print("Strings '{}' and '{}' are anagrams.".format(user_first, user_second))
    else:
        print("Strings '{}' and '{}' are not anagrams.".format(user_first, user_second))


if __name__ == '__main__':
    main()
