# Ex. 137: ScrabbleTM Score. Solved in 18 Lines.


# This program computes and displays the ScrabbleTM score for a word.
def scrabble_score(word):
    # program works with uppercase letters, therefore word is transferred to uppercase
    word = word.upper()
    # total score will be stored in corresponding variable
    score = 0
    # dictionary contains letter as key and number os scores each letter wins as value
    score_dict = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'T': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}
    # loop through each letter in word, use the dictionary to compute the score, if letter found in dicitonary
    for l in word:
        score += score_dict[l]
    # function returns number of scored earned by the provided word
    return score


# main function makes demonstration of function performance
def main():
    assert scrabble_score('zip') == 14
    word = str(input("Please enter your word: "))
    print("Word '{}' earns you {} scores!".format(word, scrabble_score(word)))


if __name__ == '__main__':
    main()
