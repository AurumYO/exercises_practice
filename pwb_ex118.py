# Ex 118: Shuffling a Deck of Cards. solved 48 lines.
# A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value. Suits are:
# normally spades, hearts, diamonds and clubs while the values are 2 through 10, Jack, Queen, King and Ace. Each playing
# card can be represented using two characters. The first character is the value of the card, with the values 2 through
# 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
# Queen, King and Ace respectively. The second character is used to represent the suit of the card. It is normally a
# lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs.
#Begin by writing a function named createDeck. It will use loops to create a complete deck of cards by storing the
# two-character abbreviations for all 52 cards into a list. Return the list of cards as the function’s only result.
# Your function will not take any parameters.
# Write a second function named shuffle that randomizes the order of the cards in a list. One technique that can be
# used to shuffle the cards is to visit each element in the list and swap it with another random element in the list.
# You must write your own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle function.
# Use both of the functions described in the previous paragraphs to create a main program that displays a deck of cards
# before and after it has been shuffled. Ensure main program only runs when your functions have not been imported into
# another file.


# this function creates deck of 52 cards from values of cards stored in list values and suits from list with suits
def create_deck():
    deck = []
    # loop through each suit value
    for s in ['s', 'h', 'd', 'c']:
        # loop through each value of the cards
        for v in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
            # add to set deck card value which consist from suit and value
            deck.append((s+v))
    # function return the deck of 52 cards
    return deck


# function takes deck of cards as arguments and returns shuffled deck of cards
def shuffle(deck):
    # import choice() function from random module
    from random import choice
    deck_shuffled = set()   # create new set which will contain shuffled cards
    # while loop will continue running until set contains 52 unique cards (length of set will be 52) from original deck
    while len(deck) > len(deck_shuffled):
        card = choice(deck)      # function choice takes randomly card from deck of cards
        deck_shuffled.add(card)  # if card not in set with shuffled cards, card is added to set of shuffled cards
    # when shuffled deck gets 52 unique cards while loop stops running and function returns shuffled deck of cards
    return deck_shuffled


# main function generates deck of cards and shuffle generated deck
def main():
    deck = create_deck()                                               # generate deck of cards
    print("The original deck of cards: \n {}".format(deck))            # display original deck of cards
    deck_shuffled = shuffle(deck)                                      # shuffle deck of cards
    print("The shuffled deck of cards: \n {}".format(deck_shuffled))   # display shuffled deck of cards


# demonstration of the function performance
if __name__ == '__main__':
    main()
