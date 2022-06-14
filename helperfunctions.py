import random

# function to get a random card from a deck
def getCard(deckIn):
    randomcard = deckIn.pop()
    return randomcard

# function to return the deck shuffled
def shuffler(deckIn):  
    deckOut = deckIn.copy()
    random.shuffle(deckOut)
    return deckOut