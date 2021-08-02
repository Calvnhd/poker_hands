# Description
Deal five cards, one at a time.  
At each deal, check...
* if you have made a hand
* which hands are still possible to hit
* which cards you would need to make each hand
* what your chances of hitting those cards are

# Need...
* Cards -- full deck of 52, split into cards dealt (up to five) and cards yet to deal

# Classes
## Deck
* Cards dealt []
* Cards yet to deal []

Each card represented as [rank, suit] with rank 2 to 14 and suit C S H D

## Hands
For possible hands 0 to 9: [high card, pair, two pair, trips, straight, flush, full house, quads, straight-flush, royal flush]...
* List True / False if possible
* List of list of cards that could make the hand
* List of chances to make each hand

## Dealer (main)
* draws a card from deck.  Uses that cards to update hands.
