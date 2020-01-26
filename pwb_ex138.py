# Ex.: Create a Bingo Card .Solved 58 lines.


# this function creates a random Bingo card and stores it in a dictionary. The keys will be the letters B, I, N, G
# and O. The values will be the lists of five numbers that appear under each letter: B (1 to 15), I(16 to 30),
# N(31 to 45), G (46 to 65) and O (66 to 80). Bingo card consists of 5 columns of 5 numbers.
def cards_generator():
    # import from random module randint method
    from random import randint
    # create start point for lowest number and upper range of points for each letter
    lower, upper = 1, 16
    # create dictionary which will store all bingo cards
    bingo_dict = {"B": [], "I": [], "N": [], "G": [], "O": []}
    # loop through each key and generate 5 cards
    for k, v in bingo_dict.items():
        while len(v) < 5:
            # value of card is from lowest point to greatest + 1
            create_card = randint(lower, upper)
            # if card is not in list of numbers for card, we add number to list of 5 numbers for each card
            if create_card not in v:
                v.append(create_card)
        # increase value of start and end number for next key with letter  by 15
        lower = lower + 15
        upper = upper + 15
    # function returns dictionary with pack of cards
    return bingo_dict


# This function that displays the Bingo card with the columns labeled appropriately.
def display_cards(cards):
    print(' B  I  N  G  O')

    for n in range(5):
        for l in ['B', 'I', 'N', 'G', 'O']:
            print("%2d " % cards[l][n], end='')
        print()


# Use these functions to write a program that displays a random Bingo card. Main program only runs when the
# file containing solution has not been imported into another program. Main function demonstrates program performance
def main():
    x = cards_generator()
    display_cards(x)


if __name__ == '__main__':
    main()
