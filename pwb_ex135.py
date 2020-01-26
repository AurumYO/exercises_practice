# Ex 135.: Anagrams. Solved in 39 Lines.


# This function defines if two words are anagrams (if they contain all of the same letters, but in a different order.
# Program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.
def anagram_definer(f_str, s_str):
    # program use two dictionary to compare two strings
    f_dict, s_dict = {}, {}
    # go through each string, and add each character to dictionary as key and number that it is occurred as value
    for ch in f_str:
        if ch not in f_dict:
            f_dict[ch] = 1
        if ch in f_dict:
            f_dict[ch] += 1
    for ch in s_str:
        if ch not in s_dict:
            s_dict[ch] = 1
        if ch in s_dict:
            s_dict[ch] += 1
    # if in result both dictionaries for each string is equal program returns appropriate message
    if f_dict == s_dict:
        return True
    else:
        return False


# Main function demonstrates function performance
def main():
    assert anagram_definer('evil', 'live') == True
    assert anagram_definer('banana', 'kiwi') == False
    # prompt user to enter two strings and display result with approprita message
    user_first = input("Please enter your first string here: ")
    user_second = input("Please enter your second string here: ")
    res = anagram_definer(user_first, user_second)
    if res:
        print("Strings '{}' and '{}' are anagrams.".format(user_first, user_second))
    else:
        print("Strings '{}' and '{}' are not anagrams.".format(user_first, user_second))

if __name__ == '__main__':
    main()
