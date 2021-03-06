import cards

class Odds():
    def __init__(self):
        # self.poss = [True,True,True,True,True,True,True,True,True,True]
        self.chances_hit = [1,1,1,1,1,1,1,1,1,1]
        self.chances_safe = [1,1,1,1,1,1,1,1,1,1]
        self.quads = False
        self.trips = False
        self.pair_one = False
        self.pair_two = False
        self.h = []
        self.d = []
    def update_rs(self): # separates h[] into (sorted) ranks[], unique ranks_u[], suits[], unique suits_u[]
        self.ranks = []
        self.suits = []
        for i in range(len(self.h)):
            self.ranks.append(self.h[i][0])
            self.suits.append(self.h[i][1])
        self.ranks = sorted(self.ranks)
        self.ranks_u = sorted(list(set(self.ranks)))
        self.suits_u = list(set(self.suits))
    def update(self, h, d):
        self.h = h
        self.d = d
        if len(h) <= 7:
            self.update_rs()        # separates h[] into (sorted) ranks[], unique ranks_u[], suits[], unique suits_u[]
            self.count_dups()       # updates bools self.pair_one, self.pair_two, self.trips, self.quads
            self.update_outs_hit()  # Creates list of cards to hit a hand on next card
            self.update_outs_safe() # Creates list of cards to stay safe for a hand on next card
            self.update_chances()   # Gets the probability to stay safe or hit on next card (2 separate lists)
            # self.combine_info()
        else:
            print('MAX CARDS REACHED')
    def combine_info(self):
        # print('Chances for hand: ' + str(self.h) + ' with ' + str(self.d.get_size()) + ' cards remaining in deck')
        o_hit = self.outs_hit[:]
        o_safe = self.outs_safe[:]
        c_hit = self.chances_hit[:]
        c_safe = self.chances_safe[:]
        for i in range(len(o_hit)):
            if i == 0:
                pass
            if i == 1:
                pass
            if i == 2:
                pass
            if i == 3:
                pass
            if i == 4:
                pass
            if i == 5:
                pass
            if i == 6:
                pass
            if i == 7:
                pass
            if i == 8:
                pass
            if i == 9:
                pass
    def update_chances(self):
        # print('Chances for hand: ' + str(self.h) + ' with ' + str(self.d.get_size()) + ' cards remaining in deck')
        # print('*** SAFE ***')
        for i in range(len(self.chances_safe)):
            self.chances_safe[i] = round(len(self.outs_safe[i]) / self.d.get_size(),2)
            # print('i: ' + str(i) + ' ... len(self.outs_safe[i]): ' + str(len(self.outs_safe[i])) + ' ... self.chances_safe[i]: ' + str(self.chances_safe[i]) )
        # print('*** HIT  ***')
        for i in range(len(self.chances_hit)):
            self.chances_hit[i] = round(len(self.outs_hit[i]) / self.d.get_size(),2)
            # print('i: ' + str(i) + ' ... len(self.outs_hit[i]):  ' + str(len(self.outs_hit[i])) + ' ... self.chances_hit[i]: ' + str(self.chances_hit[i]) )
    def update_outs_hit(self): # create a list of cards that would improve a hand for a given hand ranking 0 to 9 (high card to royal flush)
        self.outs_hit = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(self.outs_hit)):
            if i == 0: # High card
                # draw a better high card to hit
                best = self.ranks[(len(self.ranks)-1)]
                for j in range(self.d.get_size()):
                    if self.d.get_deck()[j][0] > best:
                        self.outs_hit[i].append(self.d.get_deck()[j])
            elif i == 1: # Pair
                if self.pair_one or self.pair_two or self.trips or self.quads:
                    # already hit
                    pass
                elif len(self.h) <= 6:
                    # pair up any card in hand
                    for j in range(len(self.ranks)):
                        for k in range(self.d.get_size()):
                            if self.ranks[j] == self.d.get_deck()[k][0]:
                                self.outs_hit[i].append(self.d.get_deck()[k])
            elif i == 2: # Two pair
                if self.pair_two or self.trips or self.quads:
                    # already hit
                    pass
                elif len(self.h) <= 6 and self.pair_one:
                    for j in range(len(self.ranks)):
                        for k in range(self.d.get_size()):
                            if self.d.get_deck()[k][0] == self.ranks[j] and self.d.get_deck()[k][0] != self.pair_compare:
                                self.outs_hit[i].append(self.d.get_deck()[k])
            elif i == 3: # Trips
                if self.trips or self.quads:
                    # already hit
                    pass
                elif self.pair_one or self.pair_two: 
                    # get trip on current pair (note that two pair actually gets overridden by FH...)
                    for j in range(self.d.get_size()):
                            if self.d.get_deck()[j][0] == self.pair_compare or self.d.get_deck()[j][0] == self.pair_compare_two:
                                self.outs_hit[i].append(self.d.get_deck()[j])
            elif i == 4: # Straight
                if len (self.h) == 6 and len(self.ranks_u) >= 4:
                    gap = 1
                    scale = [1,2,3,4,5,6,7,8,9,10]
                    for j in range(len(scale)):
                        sc_min = scale[j]
                        sc_max = scale[j] + 4
                        in_range = 0
                        for r in self.ranks_u:
                            if (r >= sc_min and r <= sc_max) or (sc_min == 1 and r == 14):
                                in_range += 1
                        if in_range >= (5 - gap):
                            for card in self.d.get_deck():
                                in_hand = False
                                for r in self.ranks_u:
                                    if card[0] == r:
                                        in_hand = True
                                if ((card[0] >= sc_min and card[0] <= sc_max) or (card[0] == 14 and sc_min == 1)) and not in_hand:
                                    self.outs_hit[i].append(card)
                    if len(self.outs_hit[i]) > 1:
                        self.outs_hit[i] = cards.remove_duplicates(self.outs_hit[i])
            elif i == 5: # Flush
                if len(self.h) >= 4 and len(self.suits_u) <= 3:
                    s_count = count_suits(self.h) # returns count in form [H,D,C,S]
                    s_max = max(s_count)
                    if s_max == 4:
                        for j in range(len(s_count)):
                            if s_count[j] == 4:
                                # Flush draw
                                if j == 0: # H
                                    for card in self.d.get_deck():
                                        if card[1] == 'H':
                                            self.outs_hit[i].append(card)
                                if j == 1: # D
                                    for card in self.d.get_deck():
                                            if card[1] == 'D':
                                                self.outs_hit[i].append(card)
                                if j == 2: # C
                                    for card in self.d.get_deck():
                                            if card[1] == 'C':
                                                self.outs_hit[i].append(card)
                                if j == 3: # S
                                    for card in self.d.get_deck():
                                            if card[1] == 'S':
                                                self.outs_hit[i].append(card)
            elif i == 6: # Full House
                if not self.quads and len(self.h) >= 4 and (self.pair_two or self.trips):
                    # Match either pair, or single card with trips
                    if self.pair_two or self.pair_three:
                        for card in self.d.get_deck():
                            if card[0] == self.pair_compare or card[0] == self.pair_compare_two or card[0] == self.pair_compare_three:
                                self.outs_hit[i].append(card)
                    elif self.trips:
                        for r in self.ranks_u:
                            if r != self.trip_compare:
                                for card in self.d.get_deck():
                                    if card[0] == r:
                                        self.outs_hit[i].append(card)
            elif i == 7: # Quads
                if not self.quads:
                    if self.trips:
                        # quad up trips
                        for card in self.d.get_deck():
                            if self.trip_compare == card[0]:
                                self.outs_hit[i].append(card)
            elif i == 8: # Straight Flush
                s_outs = self.outs_hit[4][:]
                f_outs = self.outs_hit[5][:]
                for s_out in s_outs:
                    for f_out in f_outs:
                        if s_out == f_out:
                            self.outs_hit[i].append(s_out)
            elif i == 9: # Royal Flush
                if len(self.h) >= 4:
                    h_royals = [[],[],[],[]] # sort royals by suit [[H],[D],[C],[S]]
                    for card in self.h:
                        if card[0] >= 10:
                            if card[1] == 'H':
                                h_royals[0].append(card)
                            elif card[1] == 'D':
                                h_royals[1].append(card)
                            elif card[1] == 'C':
                                h_royals[2].append(card)
                            elif card[1] == 'S':
                                h_royals[3].append(card)
                    s = ''
                    for j in range(len(h_royals)):
                        if len(h_royals[j]) == 4:
                            if j == 0:
                                s = 'H'
                            elif j == 1:
                                s = 'D'
                            elif j == 2:
                                s = 'C'
                            elif j == 3:
                                s = 'S'    
                    if s != '':
                        for card in self.d.get_deck():
                            if card[0] >= 10 and card[1] == s:
                                self.outs_hit[i].append(card)
    def update_outs_safe(self): # create a list of cards that would improve a hand for a given hand ranking 0 to 9 (high card to royal flush)
        self.outs_safe = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(self.outs_safe)):
            if i == 0: # High card
                # all cards are safe
                self.outs_safe[i] = self.d.get_deck()
            elif i == 1: # Pair
                if self.pair_one or self.pair_two or self.trips or self.quads or (len(self.h) < 6):
                    # already hit or more to come.  Everything is safe.
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 6:
                    # must hit on final card
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 2: # Two pair
                if self.pair_two or self.trips or self.quads or (len(self.h) < 5) or (self.pair_one and len(self.h) == 5):
                    # Already hit, or at least two more cards to come.  Everything safe.
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 5:
                    # must pair up two of the (unpaired) cards on board
                    for j in range(len(self.ranks)):
                        for k in range(self.d.get_size()):
                            if self.d.get_deck()[k][0] == self.ranks[j] and self.d.get_deck()[k][0] != self.pair_compare:
                                self.outs_safe[i].append(self.d.get_deck()[k])
                elif len(self.h) == 6:
                    # must hit on final card
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 3: # Trips
                if self.trips or self.quads or len(self.h) < 5 or (len(self.h) == 5 and self.pair_one):
                    # already hit, or sufficient cards to come
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 5:
                    # must pair up any single cards, or hit trip on current pair
                    for j in range(len(self.ranks_u)):
                        for k in range(self.d.get_size()):
                            if self.ranks_u[j] == self.d.get_deck()[k][0]:
                                self.outs_safe[i].append(self.d.get_deck()[k])
                elif len(self.h) == 6:
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 4: # Straight
                if len(self.h) == 6 and len(self.ranks_u) >= 4:
                    self.outs_safe[i] = self.outs_hit[i]
                elif len(self.h) <= 2 or self.quads: 
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) < 6:
                    if len(self.h) == 3:
                        gap = 4
                    elif len(self.h) == 4 and len(self.ranks_u) >= 2:
                        gap = 3
                    elif len(self.h) == 5 and len(self.ranks_u) >= 3:
                        gap = 2
                    elif len (self.h) == 6 and len(self.ranks_u) >= 4:
                        gap = 1
                    else:
                        gap = 0
                    if gap > 0:
                        scale = [1,2,3,4,5,6,7,8,9,10]
                        for j in range(len(scale)):
                            sc_min = scale[j]
                            sc_max = scale[j] + 4
                            in_range = 0
                            for r in self.ranks_u:
                                if (r >= sc_min and r <= sc_max) or (sc_min == 1 and r == 14):
                                    in_range += 1
                            if in_range >= (5 - gap):
                                for card in self.d.get_deck():
                                    in_hand = False
                                    for r in self.ranks_u:
                                        if card[0] == r:
                                            in_hand = True
                                    if ((card[0] >=sc_min and card[0]<=sc_max) or (card[0] == 14 and sc_min == 1)) and not in_hand:
                                        self.outs_safe[i].append(card)
                        if len(self.outs_safe[i]) > 1:
                            self.outs_safe[i] = cards.remove_duplicates(self.outs_safe[i])
                # if trips, getting the quad would be safe too.  Shouldn't matter though if you're combining safe cards from better hands in final output                    
            elif i == 5: # Flush
                if len(self.h) == 6: # Must hit on final card
                        self.outs_safe[i] = self.outs_hit[i]
                else:
                    s_count = count_suits(self.h) # returns count in form [H,D,C,S]
                    s_max = max(s_count)
                    to_flush = 5 - s_max
                    draws_left = 7 - len(self.h)
                    # print(f'IN SAFE: s_max: {s_max}, to_flush: {to_flush}, draws_left: {draws_left}')
                    if draws_left >= 5 or s_max >= 5 or (draws_left > to_flush): # enough cards to come, flush made, more draws than needed to hit
                            self.outs_safe[i] = self.d.get_deck()
                    elif draws_left == to_flush: # add only cards that can close flush gap
                        for j in range(len(s_count)):
                            if s_count[j] == s_max:
                                if j == 0: # H
                                    for card in self.d.get_deck():
                                        if card[1] == 'H':
                                            self.outs_safe[i].append(card)
                                if j == 1: # D
                                    for card in self.d.get_deck():
                                            if card[1] == 'D':
                                                self.outs_safe[i].append(card)
                                if j == 2: # C
                                    for card in self.d.get_deck():
                                            if card[1] == 'C':
                                                self.outs_safe[i].append(card)
                                if j == 3: # S
                                    for card in self.d.get_deck():
                                            if card[1] == 'S':
                                                self.outs_safe[i].append(card)
            elif i == 6: # Full House
                if len(self.ranks_u) <= 4: # FH impossible with more than 4 ranks in 7 cards
                    if len(self.ranks_u) <= 2 or len(self.h) <= 3 or self.quads or (self.pair_one and len(self.h) <= 4 ) or (self.trips and len(self.h) <= 5) or (self.pair_two and len(self.h) <= 5):
                        self.outs_safe[i] = self.d.get_deck()
                    elif len(self.h) == 6:
                        self.outs_safe[i] = self.outs_hit[i]
                    else: # 4 or 5 cards in hand, with 4 unique ranks.  Match any card
                        print('FH CARD MATCHING!!')
                        for r in self.ranks_u:
                            for card in self.d.get_deck():
                                if r == card[0]:
                                    self.outs_safe[i].append(card)
            elif i == 7: # Quads
                if len(self.ranks_u) <= 4: # quads impossible with more than 4 ranks in 7 cards
                    if self.quads or len(self.h) <= 3:
                        self.outs_safe[i] = self.d.get_deck()
                    elif len(self.h) == 6:
                        self.outs_safe[i] = self.outs_hit[i]
                    elif len(self.h) == 4:
                        # match any rank
                        for r in self.ranks_u:
                            for card in self.d.get_deck():
                                if card[0] == r:
                                    self.outs_safe[i].append(card)
                    elif len(self.h) == 5:
                        # match any pair or trip
                        for r in self.ranks_u:
                            if r == self.pair_compare or r == self.pair_compare_two or r == self.trip_compare:
                                for card in self.d.get_deck():
                                    if card[0] == r:
                                        self.outs_safe[i].append(card)
            elif i == 8: # Straight Flush
                if len(self.h) == 6:
                    self.outs_safe[i] = self.outs_hit[i]
                else:
                    s_outs = self.outs_safe[4][:]
                    f_outs = self.outs_safe[5][:]
                    for s_out in s_outs:
                        for f_out in f_outs:
                            if s_out == f_out:
                                self.outs_safe[i].append(s_out)
            elif i == 9: # Royal Flush
                draws_left = 7 - len(self.h)
                h_not_royal = 0
                for r in self.ranks:
                    if r < 10:
                        h_not_royal += 1 # this can never exceed 2. if == 2 you must draw royals.
                h_royals = [[],[],[],[]] # sort royals in hand by suit [[H],[D],[C],[S]]
                for card in self.h:
                    if card[0] >= 10:
                        if card[1] == 'H':
                            h_royals[0].append(card)
                        elif card[1] == 'D':
                            h_royals[1].append(card)
                        elif card[1] == 'C':
                            h_royals[2].append(card)
                        elif card[1] == 'S':
                            h_royals[3].append(card)
                remaining_H, remaining_D, remaining_C, remaining_S = 5 - len(h_royals[0]), 5 - len(h_royals[1]), 5 - len(h_royals[2]), 5 - len(h_royals[3])     # count royals remaining in deck by suit
                # print(f'draws_left: {}, remaining_H: {}, remaining_D: {}, ')
                if draws_left > remaining_H or draws_left > remaining_D or draws_left > remaining_C or draws_left > remaining_S:
                    self.outs_safe[i] = self.d.get_deck()
                elif draws_left == 1:
                    self.outs_safe[i] = self.outs_hit[i]
                elif h_not_royal <= 2:
                    d_royals = [] # extract royals from deck
                    for card in self.d.get_deck():
                        if card[0] >= 10:
                            d_royals.append(card)
                    if draws_left == 5:
                        self.outs_safe[i] = d_royals
                    else:  # check if there are enough draws left to close the gap in hand, and add cards that can close the gap
                        if draws_left >= remaining_H:
                            for card in d_royals:
                                if card[1] == 'H':
                                    self.outs_safe[i].append(card)
                        if draws_left >= remaining_D:
                            for card in d_royals:
                                if card[1] == 'D':
                                    self.outs_safe[i].append(card)
                        if draws_left >= remaining_C:
                            for card in d_royals:
                                if card[1] == 'C':
                                    self.outs_safe[i].append(card)
                        if draws_left >= remaining_S:
                            for card in d_royals:
                                if card[1] == 'S':
                                    self.outs_safe[i].append(card)
    def get_chances_safe(self):
        return self.chances_safe
    def get_chances_hit(self):
        return self.chances_hit
    def get_outs(self):
        return self.outs
    def count_dups(self): 
        self.quads = False
        self.trips = False
        self.pair_one = False
        self.pair_two = False
        self.pair_three = False # 3 pairs possible with 7 cards. Required for outs to hit FH.
        self.pair_compare = 0
        self.pair_compare_two = 0
        self.pair_compare_three = 0
        self.trip_compare = 0
        # self.two_pair_compare = [0,0]
        # quad_compare = []
        # fh_compare = [0,0]
        count = []
        # count duplicate cards
        for i in range(len(self.ranks_u)): 
            c = 0
            for j in range(len(self.ranks)):
                if self.ranks[j] == self.ranks_u[i]:
                    c += 1
            count.append(c)
        # Find quads / trips / pairs based on final count value
        for i in range(len(count)):
            if count[i] == 4:
                self.quads = True
                # quad_compare = self.ranks_u[i]
            elif count[i] == 3:
                self.trips = True
                # fh_compare[0] = self.ranks_u[i]
                self.trip_compare = self.ranks_u[i]
            elif count[i] == 2 and not self.pair_one:
                self.pair_one = True
                self.pair_compare = self.ranks_u[i]
                # fh_compare[1] = self.ranks_u[i]
            elif count[i] == 2 and self.pair_one and not self.pair_two:
                self.pair_two = True
                self.pair_compare_two = self.ranks_u[i]
                # self.two_pair_compare[0] = self.pair_compare
                # self.two_pair_compare[1] = self.ranks_u[i]
            elif count[i] == 2 and self.pair_one and self.pair_two:
                self.pair_three = True
                self.pair_compare_three = self.ranks_u[i]
                # update self.two_pair_compare if ever used!
    def print_outs(self):
        print('***   SAFE   ***')
        for i in range(len(self.outs_safe)):
            if i == 0:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('     High Card: All')
                else:
                    print('     High Card: ' + str(self.outs_safe[i]))
            elif i == 1:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('          Pair: All')
                else:
                    print('          Pair: ' + str(self.outs_safe[i]))
            elif i == 2:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('      Two Pair: All')
                else:
                    print('      Two Pair: ' + str(self.outs_safe[i]))
            elif i == 3:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('         Trips: All')
                else:
                    print('         Trips: ' + str(self.outs_safe[i]))
            elif i == 4:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('      Straight: All')
                else:
                    print('      Straight: ' + str(self.outs_safe[i]))
            elif i == 5:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('         Flush: All')
                else:
                    print('         Flush: ' + str(self.outs_safe[i]))
            elif i == 6:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('    Full House: All')
                else:
                    print('    Full House: ' + str(self.outs_safe[i]))
            elif i == 7:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('         Quads: All')
                else:
                    print('         Quads: ' + str(self.outs_safe[i]))
            elif i == 8:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('Straight Flush: All')
                else:
                    print('Straight Flush: ' + str(self.outs_safe[i]))
            elif i == 9:
                if len(self.outs_safe[i]) == len(self.d.get_deck()):
                    print('   Royal Flush: All')
                else:
                    print('   Royal Flush: ' + str(self.outs_safe[i]))
        print('***   HIT    ***')
        for i in range(len(self.outs_hit)):
            if i == 0:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('     High Card: All')
                else:
                    print('     High Card: ' + str(self.outs_hit[i]))
            elif i == 1:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('          Pair: All')
                else:
                    print('          Pair: ' + str(self.outs_hit[i]))
            elif i == 2:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('      Two Pair: All')
                else:
                    print('      Two Pair: ' + str(self.outs_hit[i]))
            elif i == 3:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('         Trips: All')
                else:
                    print('         Trips: ' + str(self.outs_hit[i]))
            elif i == 4:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('      Straight: All')
                else:
                    print('      Straight: ' + str(self.outs_hit[i]))
            elif i == 5:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('         Flush: All')
                else:
                    print('         Flush: ' + str(self.outs_hit[i]))
            elif i == 6:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('    Full House: All')
                else:
                    print('    Full House: ' + str(self.outs_hit[i]))
            elif i == 7:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('         Quads: All')
                else:
                    print('         Quads: ' + str(self.outs_hit[i]))
            elif i == 8:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('Straight Flush: All')
                else:
                    print('Straight Flush: ' + str(self.outs_hit[i]))
            elif i == 9:
                if len(self.outs_hit[i]) == len(self.d.get_deck()):
                    print('   Royal Flush: All')
                else:
                    print('   Royal Flush: ' + str(self.outs_hit[i]))

# returns list of number of suits [H,D,C,S] for a given list of cards.
# counting outs for Flush depends on this function.  Take care if altering!  
def count_suits(H):
    h = H[:]
    suits = [0,0,0,0]
    for card in h:
        if card[1] == 'H':
            suits[0] += 1
        if card[1] == 'D':
            suits[1] += 1
        if card[1] == 'C':
            suits[2] += 1
        if card[1] == 'S':
            suits[3] += 1
    # print(f'count_suits HDCS: {suits}')
    return suits


# Evaluates a five card hand
# Takes list of ranks & suits [[r,s],[r,s],[r,s],[r,s],[r,s]]
# Returns evaluation code [hand_ranking, same_hand_comparison, kickers]
# Need to update to compare value of same hands
def evaluate_hand(hand):
    if not (len(hand) == 5):
        print('ERROR EVALUATING HAND for hand: ' + str(hand))
        return -1
    # Bool for making a hand
    quads = False
    trips = False
    pair_one = False
    pair_two = False
    flush = False
    straight = False
    # Values to compare same hand
    kickers = []
    fh_compare = [0,0]  # stores [trip,pair]
    quad_compare = 0   
    trip_compare = 0
    two_pair_compare = [0,0]
    pair_compare = 0
    # For counting duplicate cards
    count = []
    # Returning value
    value = [0]  

    ranks = set()    
    ranks_all = []
    suits = set()
    for i in range(len(hand)):
        ranks.add(hand[i][0])               # unordered ranks without duplicates
        ranks_all.append(hand[i][0])        # unordered ranks with duplicates
        suits.add(hand[i][1])               # unordered suits
    ranks_sorted = sorted(ranks)            # low to high ranks without duplicates
    ranks_sorted_all = sorted(ranks_all)    # low to high ranks with duplicates

    if len(suits) == 1:  # Check for flush
        flush = True
    if len(ranks) == 5:  # Check for straight
        if ranks_sorted[4] == 14 and ranks_sorted[3] == 5: # Ace is low
            ranks_sorted[4] = 1
            ranks_sorted = sorted(ranks_sorted)
        if ((ranks_sorted[0] + 1) == ranks_sorted[1]) and ((ranks_sorted[1] + 1) == ranks_sorted[2]) and ((ranks_sorted[2] + 1) == ranks_sorted[3]) and ((ranks_sorted[3] + 1) == ranks_sorted[4]):
            straight = True
        else: # High Card
            kickers = sorted(ranks, reverse=True)
    else: 
        # count duplicate cards
        for i in range(len(ranks_sorted)): 
            c = 0
            for j in range(len(ranks_sorted_all)):
                if ranks_sorted_all[j] == ranks_sorted[i]:
                    c += 1
            count.append(c)
        # Find quads / trips / pairs based on final count value
        for i in range(len(count)):
            if count[i] == 1: 
                kickers.append(ranks_sorted[i])
            elif count[i] == 4:
                quads = True
                quad_compare = ranks_sorted[i]
            elif count[i] == 3:
                trips = True
                fh_compare[0] = ranks_sorted[i]
                trip_compare = ranks_sorted[i]
            elif count[i] == 2 and not pair_one:
                pair_one = True
                pair_compare = ranks_sorted[i]
                fh_compare[1] = ranks_sorted[i]
            elif count[i] == 2 and pair_one:
                pair_two = True
                two_pair_compare[0] = pair_compare
                two_pair_compare[1] = ranks_sorted[i]

        kickers = sorted(kickers, reverse=True)
    # print('Contains ranks ' + str(ranks_sorted) + ' occurring ' + str(count) + ' times respectively.   Kickers: ' + str(kickers))
    # Determine value
    if flush and straight and (max(ranks_sorted) == 14):  # Royal Flush
        value[0] = 9
        value.append(max(ranks_sorted))
        return value
    if flush and straight: # Straight Flush
        value[0] =  8
        value.append(max(ranks_sorted)) # use sorted var to account for possible low Ace
        return value
    elif quads: # Four of a Kind
        value[0] =  7
        value.append(quad_compare)
        value.extend(kickers) 
        return value
    elif trips and (pair_one or pair_two): # Full House
        value[0] =  6
        value.extend(fh_compare)
        return value
    elif flush:  # Flush
        value[0] =  5
        value.extend(kickers)
        return value
    elif straight: # Straight
        value[0] =  4
        value.append(max(ranks_sorted)) # use sorted var to account for possible low Ace
        return value
    elif trips: # Three of a kind
        value[0] =  3
        value.append(trip_compare)
        value.extend(kickers)
        return value
    elif pair_one and pair_two: # Two Pair
        value[0] =  2
        two_pair_compare = sorted(two_pair_compare, reverse=True)
        value.extend(two_pair_compare)
        value.extend(kickers)
        return value
    elif pair_one or pair_two: # Pair
        value[0] =  1
        value.append(pair_compare)
        value.extend(kickers)
        return value
    else: # High Card
        value.extend(kickers)
        return value

# takes code from evaluate_hand and returns its meaning in a string
def interpret_eval(hand):
    if hand == [0,0,0]:
        return 'FOLDED'
    x = hand[:] 
    for i in range(1, len(x)):
        if x[i] == 11:
            x[i] = 'J'
        elif x[i] == 12:
            x[i] = 'Q'
        elif x[i] == 13:
            x[i] = 'K'
        elif x[i] == 14:
            x[i] = 'A'
        
    #Output message
    if x[0] == 9:
        output = 'Royal Flush!'
    elif x[0] == 8 and len(x) == 2:
        output = 'Straight Flush, ' + str(x[1]) + ' high'
    elif x[0] == 7 and len(x) == 3:
        output = 'Four of a Kind, ' + str(x[1]) + 's with ' + str(x[2]) + ' kicker'
    elif x[0] == 6 and len(x) == 3:
        output = 'Full House, ' + str(x[1]) + 's full of ' + str(x[2]) + 's'
    elif x[0] == 5 and len(x) == 6:
        output = 'Flush, ' + str(x[1]) + ' high followed by ' + str(x[2]) + ' ' + str(x[3]) + ' ' +  str(x[4]) + ' ' +  str(x[5])
    elif x[0] == 4 and len(x) == 2:
        output = 'Straight, ' + str(x[1]) + ' high'
    elif x[0] == 3 and len(x) == 4:
        output = 'Three of a Kind, ' + str(x[1]) + 's with ' + str(x[2]) + ' ' + str(x[3]) + ' kickers'
    elif x[0] == 2 and len(x) == 4:
        output = 'Two Pair, ' + str(x[1]) + 's and ' + str(x[2]) + 's with ' + str(x[3]) + ' kicker'
    elif x[0] == 1  and len(x) == 5:
        output = 'Pair of ' + str(x[1]) + 's, with '+ str(x[2]) + ' ' + str(x[3]) + ' ' + str(x[4]) + ' kickers'
    elif x[0] == 0 and len(x) == 6:
        output = str(x[1]) + ' High, followed by ' + str(x[2]) + ' ' + str(x[3]) + ' ' + str(x[4]) + ' ' + str(x[5])
    else:
        output = 'ERROR INTERPRETTING HAND EVALUATION CODE'
    return output

# Compares hands h1 and h2.  5 cards in each.
# h1 and h2 must be output from evaluate_hand
# returns the best of h1 or h2 in the same format as input, or 0 if they are equal
def compare_hands(h1, h2, i=0):
    if i == 7: # Base case
        print('ERROR COMPARING HANDS for h1 and h2: ' + str(h1) + ' ... ' + str(h2) + ' ... i == 7')
        return -1
    if h1 == h2:
        return 0
    if h1[i] > h2[i]:
        return h1
    elif h1[i] < h2[i]:
        return h2
    else:
        if h1[i] == h2[i] and len(h1) == len(h2):
            i += 1
            return compare_hands(h1,h2,i)
        if h1 == [0,0,0] and h2 != [0,0,0]:
            return h2
        if h2 == [0,0,0] and h1 != [0,0,0]:
            return h1
        else:
            print('ERROR COMPARING HANDS for h1 and h2: ' + str(h1) + ' ... ' + str(h2))
            return -1

# Finds the best hand a player can make with their 2 cards
# takes 2 cards from hand, 3 to 5 cards from board, and returns the best hand in the form of eval code
def make_hands(H, B):
    if len(H) + len(B) < 5:
        print('ERROR! Not enough cards on board to make_hands')
        return -1
    h = []
    b = []
    best = []
    test = []

    # Ensure correct inputs and initialize best
    if len(H) == 2 and len(B) > len(H):
        h = H[:]
        b = B[:]
    elif len(B) == 2 and len(H) > len(B): 
        h = B[:]
        b = H[:]
    else:
        print('ERROR:  Incorrect input.')
        return -1
    # initialize best 5 to hand and flop
    best.extend(h)
    best.extend([b[0], b[1], b[2]])
    el_best = evaluate_hand(best)

    # Find best 5 card combination
    if (len(h) + len(b)) == 5: # 3 cards on board (flop)
        return el_best
    elif (len(h) + len(b)) == 6: # 4 cards on board (turn)
        for i in range(6):
            test = []
            if i < 2:
                test.append(h[i]) # using just one card from hand
                test.extend(b)
                el_test = evaluate_hand(test)
                comp = compare_hands(el_test, el_best) # returns eval of best, or 0 if equal 
                if comp != 0:
                    el_best = comp
            else:
                test.extend(h)  # using both cards in hand
                hold = b[:]     # copy data to keep original board info b[] intact
                hold.pop(i-2)   # select three of the four cards on board by removing one
                test.extend(hold)
                el_test = evaluate_hand(test)
                comp = compare_hands(el_test, el_best)
                if comp != 0:
                    el_best = comp
        return el_best
    elif (len(h) + len(b)) == 7: # 5 cards on board (river)
        for i in range(4):
            for j in range(5):
                test = []   # reset test hand
                if i < 2:   # use one card in hand
                    test.append(h[i])   # one card from hand (i = 0 or 1)
                    hold = b[:]
                    hold.pop(j)         # pop off one of 5 (j = 0 to 4) on board, to select 4 remaining cards 
                    test.extend(hold)   # test hand built
                    el_test = evaluate_hand(test)
                    comp = compare_hands(el_test, el_best)
                    if comp != 0:
                        el_best = comp
                if i == 2:  # use both cards in hand 
                    for k in range(5):
                        test = []
                        test.extend(h)  # both cards
                        hold1 = b[:]
                        hold2 = []
                        if k > j : # use j and k to select cards to pop
                            # i j k
                            # where i == both from hand, and j k indicate which cards from board NOT to include
                            # print('ijk: ' + str(i) + ' ' + str(j) + ' ' + str(k))
                            # find unwanted cards
                            for x in range(len(hold1)):
                                if x == k or x == j:
                                    hold1[x] = -1
                            # rebuild without unwanted cards
                            for x in range(len(hold1)):
                                if hold1[x] != -1:
                                    hold2.append(hold1[x])
                            if len(hold2) != 3:
                                print('ERROR CHOOSING CARDS FROM BOARD')
                            test.extend(hold2)
                            el_test = evaluate_hand(test)
                            comp = compare_hands(el_test, el_best)
                            if comp != 0:
                                el_best = comp
                        else:
                            pass
                if i == 3:  # no cards from hand
                    test.extend(b)
                    el_test = evaluate_hand(test)
                    comp = compare_hands(el_test, el_best)
                    if comp != 0:
                        el_best = comp
        return el_best            
    else:
        print('ERROR B:  Incorrect input.')
        return -1

# Takes a list of evaluated hands, and returns the best one
# Try different sorting algorithms?
def find_best_hand(hands):
    best = hands[0]
    if len(hands) > 1:
        for h in range(1, len(hands)):
            comp = compare_hands(best, hands[h])
            if comp != 0:
                best = comp
    return best

