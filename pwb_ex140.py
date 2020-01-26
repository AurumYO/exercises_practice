# Ex 140. Play BINGO. solved 88 lines.

# In this exercise you will write a program that simulates a game of Bingo for a single card.
# Generating a list of all of the valid Bingo calls (B1 through O75).
def generate_list_cards():
    list_cards = []
    number = 1
    for l in ['B', 'I', 'N', 'G', 'O']:
        for t in range(15):
            list_cards.append(l + str(number))
            number += 1
    # randomize the order of its elements by calling the shuffle function in the random module
    from random import shuffle
    shuffle(list_cards)
    return list_cards


# Then your program should consume calls out of the list, crossing out numbers on the card, until the card contains
# a crossed out line (horizontal, vertical or diagonal).
def game_card(new_card):
    from pwb_ex139 import bingo_check_win
    from random import choice
    list_of_cards = generate_list_cards()
    counter = 0
    win = False
    while not win:
        counter += 1
        cross = choice(list_of_cards)
        searched_k, searched_v = cross[0], int(cross[1:])
        for k, v in new_card.items():
            if searched_k == k:
                for l in range(len(v)):
                    if searched_v == v[l]:
                        v[l] = 0

        win = bingo_check_win(new_card)
    # function returns
    return new_card, counter


# Simulate 1,000 games and report the min., max. and average number of calls that must be made before the card wins
def game_simulation():
    from pwb_ex138 import cards_generator, display_cards
    winning_calls_number = []
    for n in range (1000):
        new_card = cards_generator()
        game = game_card(new_card)
        winning_calls_number.append(game[1])

    min_calls = min(winning_calls_number)
    max_calls = max(winning_calls_number)
    average = int(sum(winning_calls_number)/1000)
    # report the min., max. and average number of calls that must be made before the card wins
    print("Within 10000 BINGO card calls, it took: ")
    print(" - minimum", min_calls, "number of calls for card to win.")
    print(" - maximum", max_calls, "number of calls for card to win.")
    print(" - in average it took", average, "number of calls for card to win.")

game_simulation()



