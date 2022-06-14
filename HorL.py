import random
from helperfunctions import *

# Sample cards
suitTuple = ('Diamonds', 'Spades', 'Clubs', 'Hearts')
rankTuple = ('Ace', '2', '3', '4', '5', '6,', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

numoftries = 8

# Main
print('------------------------------------')
print('Welcome to Higher or Lower card game')
print('------------------------------------')
print('In this game, you have to choose whether the next card shown')
print('is going to be higher or lower than the selected card')
print('Right answer will provide 20 points while wrong answer will take away 15.')
print('You will start with 50 points')
print('')

deckList = []
for suit in suitTuple:
    for value, rank in enumerate(rankTuple):
        cardDict = {'rank': rank, 'suit': suit, 'value': value+1}
        deckList.append(cardDict)

points = 50

# game loop (unlimited games)
while True:
    print('')
    gameDeckList = shuffler(deckList)
    currentDeckList = getCard(gameDeckList)
    currentrank = currentDeckList['rank']
    

