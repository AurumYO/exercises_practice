# Exercise 119: Dealing Hands of Cards. (solved 44 Lines)
# In many card games each player is dealt a specific number of cards after the deck has been shuffled. Write function,
# deal, which takes the number of hands, the number of cards per hand, and a deck of cards as its three parameters. Your
# function should return a list containing all of the hands that were dealt. Each hand  represented as a list of cards.
# When dealing the hands, function should modify the deck of cards passed to it as a parameter, removing each card from
# the deck as it is added to a player’s hand. When cards are dealt, it is customary to give each player a card before
# any player receives additional card. Function should follow this custom when constructing the hands for the players.
# Use your solution to Exercise 118 to help you construct a main program that creates and shuffles a deck of cards,
# and then deals out four hands of five cards each. Display all of the hands of cards, along with the cards remaining
# in the deck after the hands have been dealt.

# import from ex. 118 function which creates deck of cards and shuffles them randomly
from pwb_ex118 import create_deck, shuffle


# function deal takes as its arguments number of players, number of cards per each player and deck of cards
# as output functions provides list of cards for each player and deck with remaining cards
def deal(hand, number, deck):
    hands = {}                      # dictionary hands will be used to store player name as key and his cards as values
    # function first generates number of players - keys in dictionary depending on the function's input
    # for reading purpose name of player starts from 1st to n-th,
    for h in range(1, hand + 1):      # loop starts from 1 to range of players + 1 (since range() func starts from 0
        hand_name = 'hand_' + str(h)  # name of player will be "hand_" + positional number of the player (1st, 2nd...)
        hands[hand_name] = []         # name of the player added to the dictionary and as key added empty list
    # while loop gives each player a cards depending on the quantity of cards per player depending on the input
    # loop runs until each user will receives defined number of cards, user will not get new card until all players
    # have same quantity of cards
    while number > 0:
        for k, v in hands.items():  # go through each player (dictionary key) and his cards (dictionary value with key)
            card = deck.pop()       # take cards from top of the deck
            v.append(card)          # cards added to the list of values
            hands[k] = v            # players list of card updated with new card
        number -= 1                 # after each players is given with card, number of cards to give decreased by one
        # when number of cards per user is equal to zero no more cards to give
        # function returns dict with cards for each player and remaining deck of cards
    return hands, deck


# main function takes from user number of players for game, number of cards per player and performs cards give
def main():
    deck = create_deck()
    shuffled_deck = shuffle(deck)
    hand = int(input("Please enter number of hands to pass the cards to: "))
    number = int(input("Please enter number of cards per each hand: "))
    gamers,  remaining_deck = deal(hand, number, shuffled_deck)
    for gamer, cards_in_hand in gamers.items():
        print("Gamer {} has following cards in his hands: {} .".format(gamer, cards_in_hand))
    print("\nIn deck remain following cards:\n {}".format(remaining_deck))


if __name__ == '__main__':
    main()