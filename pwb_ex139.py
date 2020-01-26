# Ex. 139. Checking for a Winning Card. (102 Lines)


# This function takes a dictionary representing a Bingo card as its only parameter. If the card contains a line of
# five zeros (vertical, horizontal or diagonal) then function should return True (the card has won). Otherwise
# the function should return False. In implementation marked that a number has been called by replacing it with a 0 in
# the Bingo card dictionary.
def bingo_check_win(card):
    sum_horizontal, sum_vertical = 0, 0
    # check if card has vertical lines of zeros
    for k, v in card.items():
        for l in range(len(v)):
            sum_vertical += card[k][l]
        if sum_vertical == 0:
            return True
        sum_vertical = 0

    # check if card has horizontal lines of zeros.
    for t in range(len(card.values())):
        for k in card.keys():
            sum_horizontal += card[k][t]
        if sum_horizontal == 0:
            return True
        sum_horizontal = 0

    # check if card has lines of zeros in diagonal
    if card['B'][0] == 0 and card['I'][1] == 0 and card['N'][2] == 0 and card['G'][3] == 0 and card['O'][4] == 0:
        return True
    if card['B'][4] == 0 and card['I'][3] == 0 and card['N'][2] == 0 and card['G'][1] == 0 and card['O'][0] == 0:
        return True

    return False


# Main program demonstrates function bingo_check_win(card) by creating several Bingo cards, displaying them,
# and indicating whether or not they contain a winning line. In demonstration function should be used card with a
# horizontal line, at least one card with a vertical line, at least one card with a diagonal line, and at
# least one card that has some numbers crossed out but does not contain a winning line.
def main():
    # import functions from Ex 138 wich will generate random BINGO card and will display the card
    from pwb_ex138 import cards_generator, display_cards
    # cards_list will contain all cards which will be checked by bingo_check_win() function
    bingo_cards_list = []
    # create BINGO card with all zeros in third horizontal line
    horizontal_card = cards_generator()
    for k, v in horizontal_card.items():
        if horizontal_card[k][2]:
            horizontal_card[k][2] = 0
    bingo_cards_list.append(horizontal_card)

    # create BINGO card with all zeros in vertical line under key letter 'G'
    vertical_card = cards_generator()
    for k, v in vertical_card.items():
        for i in range(len(v)):
            if k == 'G':
                vertical_card[k][i] = 0
    bingo_cards_list.append(vertical_card)

    # create regular BINGO card with no zeros anywhere
    bingo_cards_list.append(cards_generator())

    # create BINGO card where all zeros in diagonal, manually assign zero to values in diagonal order
    diagonal_card = cards_generator()
    diagonal_card['B'][0] = 0
    diagonal_card['I'][1] = 0
    diagonal_card['N'][2] = 0
    diagonal_card['G'][3] = 0
    diagonal_card['O'][4] = 0
    bingo_cards_list.append(diagonal_card)
    rev_diagonal_card = cards_generator()
    rev_diagonal_card['B'][4] = 0
    rev_diagonal_card['I'][3] = 0
    rev_diagonal_card['N'][2] = 0
    rev_diagonal_card['G'][1] = 0
    rev_diagonal_card['O'][0] = 0
    bingo_cards_list.append(rev_diagonal_card)

    # Check all created cards in loop and display the result of check
    for card in bingo_cards_list:
        display_cards(card)
        play = bingo_check_win(card)
        if play:
            print('This bingo card has won!\n')
        else:
            print('This bingo card has lost!\n')


if __name__ == '__main__':
    main()
