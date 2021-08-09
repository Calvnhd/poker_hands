import random

# Deck of cards class
# 52 Cards of [rank,suit] in a nested list [[r,s],[r,s],[r,s]...]
class Deck:
    def __init__(self):
        self.deck = []      # Track cards in deck
        self.removed = []   # Track cards pulled from deck (in play and discarded)

        # Build deck
        suit = 'H'
        for card in range(2,15):
            self.deck.extend([[card, suit]])
        suit = 'D'
        for card in range(2,15):
            self.deck.extend([[card, suit]])
        suit = 'C'
        for card in range(2,15):
            self.deck.extend([[card, suit]])
        suit = 'S'
        for card in range(2,15):
            self.deck.extend([[card, suit]])
    def get_size(self):         # Get number of cards (remaining) in deck
        return len(self.deck)
    def get_removed_size(self): # Get number of cards removed from deck
        return len(self.removed)
    def shuffle(self):          # Recombine all cards into deck and shuffle
        shuffled = []
        if len(self.removed) > 0:
            self.deck.extend(self.removed)
            self.removed = []
        for card in range(len(self.deck)):
            shuffled.append(self.deck.pop(random.randint(0, len(self.deck)-1)))
        self.deck = shuffled[:]
        if len(self.deck) != 52:
            print("WARNING: something has gone wrong with your shuffling") # Figure out how to throw proper error messages and update this
    def take_card(self):        # Take card from top of deck (removed card tracked in removed[])
        card = self.deck.pop(0)
        self.removed.append(card)
        return card
    def get_deck(self):        # Cards (remaining) in deck
        return self.deck
    def get_removed(self):     # Cards removed from deck
        return self.removed
    def info(self):             # Print number of cards remaining & removed
        info = 'Number of cards...\nRemaining: ' + str(len(self.deck)) + '\nRemoved: ' + str(len(self.removed))
        return info
    def bias_deck(self, n): # Get specific cards to the front of the deck to get a desired hand quicker for testing.  A bit buggy.
        self.shuffle()
        h = []
        i = 0
        suit = 'x' 
        if n == 9:
            r = [14, 11, 12, 13, 10]
            suit = 'H'
        elif n == 8:
            suit = 'H'
            r = [14,  4,  5,  2,  3] 
        i = 0
        while len(h) < 5:
            if i == len(self.deck):
                i = 0
            if self.deck[i][1] == suit or suit == 'x':
                for j in range(len(r)):
                    if self.deck[i][0] == r[j]:
                        h.append(self.deck.pop(i))
            i += 1
        h.extend(self.deck)
        self.deck = h[:]

# takes a list of cards, removes all real duplicates (same in rank AND suit), sorts, and returns list.
# Used in special cases e.g. avoid recounting outs 
def remove_duplicates(H):
    h = H[:]
    # clean up by marking duplicates as []
    for i in range(len(h)):
        for j in range(i+1,len(h)):
            if h[i] == h[j] and h[i] != 0:
                h[j] = []
    h.sort() # all [] to front
    done = False
    while not done:
        if h[0] == []:    
            h.pop(0)
        else:
            done = True
    return h




