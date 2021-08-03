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
    def update_rs(self): # called by find_outs() separates h[] into (sorted) ranks[], unique ranks_u[], suits[], suits_set{}
        self.ranks = []
        self.suits = []
        for i in range(len(self.h)):
            self.ranks.append(self.h[i][0])
            self.suits.append(self.h[i][1])
        self.ranks = sorted(self.ranks)
        self.ranks_u = sorted(list(set(self.ranks)))
        self.suits_set = set(self.suits)
    def update(self, h, d):
        self.h = h
        self.d = d
        if len(h) < 5:
            self.update_rs()    # separates h[] into (sorted) self.ranks[], self.suits[], self.ranks_set{}, self.suits_set{}
            self.count_dups()   # updates bools self.pair_one, self.pair_two, self.trips, self.quads
            self.update_outs_hit()  
            self.update_outs_safe()
            # self.update_poss()
            self.update_chances()
            self.update_outs_count()
    # def update_poss(self):
    #     for i in range(len(self.poss)):
    #         if self.chances[i] > 0:
    #             self.poss[i] = True
    #         else:
    #             self.poss[i] = False
    def update_chances(self):
        print('CALCULATING CHANCES for hand: ' + str(self.h) + ' with ' + str(self.d.get_size()) + ' cards remaining in deck')
        print('*** SAFE ***')
        for i in range(len(self.chances_safe)):
            self.chances_safe[i] = round(len(self.outs_safe[i]) / self.d.get_size(),2)
            print('i: ' + str(i) + ' ... len(self.outs_safe[i]): ' + str(len(self.outs_safe[i])) + ' ... self.chances_safe[i]: ' + str(self.chances_safe[i]) )
        print('*** HIT  ***')
        for i in range(len(self.chances_hit)):
            self.chances_hit[i] = round(len(self.outs_hit[i]) / self.d.get_size(),2)
            print('i: ' + str(i) + ' ... len(self.outs_hit[i]):  ' + str(len(self.outs_hit[i])) + ' ... self.chances_hit[i]: ' + str(self.chances_hit[i]) )
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
                elif len(self.h) <= 4:
                    # pair up any card in hand
                    for j in range(len(self.ranks)):
                        for k in range(self.d.get_size()):
                            if self.ranks[j] == self.d.get_deck()[k][0]:
                                self.outs_hit[i].append(self.d.get_deck()[k])
            elif i == 2: # Two pair
                if self.pair_two or self.trips or self.quads:
                    # already hit
                    pass
                elif len(self.h) <= 4 and self.pair_one:
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
                if len(self.h) == 4:
                    ''
                    ace_low = False
                    max_r = self.ranks[(len(self.ranks) - 1)]
                    min_r = self.ranks[0]
                    if self.ranks[(len(self.ranks) - 1)] == 14 and self.ranks[(len(self.ranks) - 2)] <= 5:
                        # consider Ace low
                        self.ranks[(len(self.ranks) - 1)] = 1
                        self.ranks = sorted(self.ranks)
                        max_r = self.ranks[(len(self.ranks) - 1)]
                        min_r = self.ranks[0]
                        ace_low = True
                    # check range and unique values
                    if len(self.ranks_u) == len(self.ranks) and (max_r - min_r) < 5:
                        upper = min_r + 4
                        lower = max_r - 4
                        j = lower
                        while j <= upper:
                            found = False
                            for k in range(len(self.ranks)):
                                if self.ranks[k] == j:
                                    found = True
                            if not found:
                                for c in range(self.d.get_size()):
                                    if self.d.get_deck()[c][0] == j:
                                        self.outs_hit[i].append(self.d.get_deck()[c])
                            j += 1
                    # Convert Ace back to high for other functions
                    if ace_low:
                        self.ranks[0] = 14
                        self.ranks = sorted(self.ranks)

    def update_outs_safe(self): # create a list of cards that would improve a hand for a given hand ranking 0 to 9 (high card to royal flush)
        self.outs_safe = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(self.outs_safe)):
            if i == 0: # High card
                # all cards are safe
                self.outs_safe[i] = self.d.get_deck()
            elif i == 1: # Pair
                if self.pair_one or self.pair_two or self.trips or self.quads or (len(self.h) < 4):
                    # already hit.  Everything is safe.
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 4:
                    # must hit on final card
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 2: # Two pair
                if self.pair_two or self.trips or self.quads or (len(self.h) < 3) or (self.pair_one and len(self.h) == 3):
                    # Already hit, or at least two more cards to come, .  Everything safe.
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 3:
                    # must pair up two of the (unpaired) cards on board
                    for j in range(len(self.ranks)):
                        for k in range(self.d.get_size()):
                            if self.d.get_deck()[k][0] == self.ranks[j] and self.d.get_deck()[k][0] != self.pair_compare:
                                self.outs_safe[i].append(self.d.get_deck()[k])
                elif len(self.h) == 4:
                    # must hit on final card
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 3: # Trips
                if self.trips or self.quads or len(self.h) < 3 or (len(self.h) == 3 and self.pair_one):
                    self.outs_safe[i] = self.d.get_deck()
                elif len(self.h) == 3:
                    # must pair up any single cards, or hit trip on current pair
                    for j in range(len(self.ranks_u)):
                        for k in range(self.d.get_size()):
                            if self.ranks_u[j] == self.d.get_deck()[k][0]:
                                self.outs_safe[i].append(self.d.get_deck()[k])
                elif len(self.h) == 4:
                    # must hit trip
                    self.outs_safe[i] = self.outs_hit[i]
            elif i == 4: # Straight
                if len(self.h) == 1:
                    # 5 up and down
                    lower = self.ranks[0] - 4
                    upper = self.ranks[0] + 4
                    # print('STRAIGHT CHECK\nOnly one card dealt')
                    # print('lower: ' + str(lower) + ' upper: ' + str(upper) + ' for ranks ' + str(self.ranks))
                    for j in range(self.d.get_size()):
                        r = self.d.get_deck()[j][0]
                        if r >= lower and r <= upper and r != self.ranks[0] or (lower <= 1 and r == 14):
                            self.outs_safe[i].append(self.d.get_deck()[j])
                    if self.ranks[0] == 14:
                        for j in range(self.d.get_size()):
                            if self.d.get_deck()[j][0] <= 5:
                                self.outs_safe[i].append(self.d.get_deck()[j])
                elif len(self.h) > 1:
                    print('STRAIGHT CHECK\n' + str(len(self.h)) +  ' cards dealt')
                    ace_low = False
                    max_r = self.ranks[(len(self.ranks) - 1)]
                    min_r = self.ranks[0]
                    if self.ranks[(len(self.ranks) - 1)] == 14 and self.ranks[(len(self.ranks) - 2)] <= 5:
                        # consider Ace low
                        print('Ace is low')
                        self.ranks[(len(self.ranks) - 1)] = 1
                        self.ranks = sorted(self.ranks)
                        max_r = self.ranks[(len(self.ranks) - 1)]
                        min_r = self.ranks[0]
                        ace_low = True
                    # check range and unique values
                    if len(self.ranks_u) == len(self.ranks) and (max_r - min_r) < 5:
                        print('Cards are within a valid straight range')
                        upper = min_r + 4
                        lower = max_r - 4
                        print('lower: ' + str(lower) + ' upper: ' + str(upper) + ' for ranks ' + str(self.ranks))
                        j = lower
                        while j <= upper:
                            # print('looking for rank j = ' + str(j))
                            found = False
                            for k in range(len(self.ranks)):
                                if self.ranks[k] == j:
                                    # print(str(j) + ' has been found in hand ' + str(self.ranks) + ' at k = ' + str(k))
                                    found = True
                            if not found:
                                # print('rank j = ' + str(j) + ' is not in the hand ... adding to outs_safe')
                                for c in range(self.d.get_size()):
                                    if self.d.get_deck()[c][0] == j:
                                        self.outs_safe[i].append(self.d.get_deck()[c])
                            j += 1
                    # Convert Ace back to high for other functions
                    if ace_low:
                        print('Setting Ace high again')
                        self.ranks[0] = 14
                        self.ranks = sorted(self.ranks)

            # elif i == 5: # Flush
            #     if len(self.suits_set) != 1:
            #         self.chances[i] = 0
            #         self.outs[i] = [0]
            #     else:
            #         self.chances[i] = (13 - len(h)) / len(d)
            # elif i == 6: # Full House
            #     if len(h) < 3:
            #         self.chances[i] = 1
            #     elif len(h) == 3:
            #         if self.trips:
            #             self.chances[i] = 1
            #             self.outs[i] = d
            #         elif self.pair_one:
            #             pass
            #         else:
            #             self.chances[i] = 0
            #             self.outs[i] = 0
            #     elif len(h) == 4:
            #         if self.quads:
            #             self.chances[i] = -1
            #             self.outs[i] =  [-1]
            #         elif self.trips:
            #             pass
            #         elif self.pair_two:
            #             pass
            #         else:
            #             self.chances[i] = 0
            #             self.outs[i] = [0]
            # elif i == 7: # Quads
            #     if len(h) <= 1:
            #         self.chances[i] = 1
            #         self.outs[i] = d[:]
            #     elif len(self.ranks_set) >= 3:
            #         self.chances[i] = 0
            #         self.outs[i] = [0]
            #     elif self.quads: 
            #         self.chances[i] = 0
            #         self.outs[i] = [0]
            #     elif len(h) == 2:
            #         pass
            #     elif len(h) == 3:
            #         pass
            #     elif len(h) == 4:
            #         pass
            # elif i == 8: # Straight Flush
            #     if len(self.suits_set) != 1:
            #         self.chances[i] = 0
            #     else:
            #         pass
            # elif i == 9: # Royal Flush
            #     royal_ranks = True
            #     for j in range(len(self.ranks)):
            #         if self.ranks[j] < 10:
            #             royal_ranks = False
            #             break
            #     if royal_ranks and len(self.suits_set) == 1:
            #         self.chances[i] = (5 - len(h)) / d.get_size()
            #     else:
            #         self.chances[i] = 0
    def update_outs_count(self):
        pass
    # def get_possible(self):
    #     return self.poss
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
        self.pair_compare = 0
        # quad_compare = []
        # fh_compare = [0,0]
        self.pair_compare_two = 0
        count = []
        # count duplicate cards
        for i in range(len(self.ranks_u)): 
            c = 0
            for j in range(len(self.ranks)):
                if self.ranks[j] == self.ranks_u[i]:
                    c += 1
            count.append(c)
        # print('count: ' + str(count))
        # Find quads / trips / pairs based on final count value
        for i in range(len(count)):
            if count[i] == 4:
                # print('quads made')
                self.quads = True
                # quad_compare = self.ranks_u[i]
            elif count[i] == 3:
                # print('trips made')
                self.trips = True
                # fh_compare[0] = self.ranks_u[i]
                # trip_compare = self.ranks_u[i]
            elif count[i] == 2 and not self.pair_one:
                # print('one pair made: ' + str(self.ranks_u[i]))
                self.pair_one = True
                self.pair_compare = self.ranks_u[i]
                # fh_compare[1] = self.ranks_u[i]
            elif count[i] == 2 and self.pair_one:
                # print('two pair made')
                self.pair_two = True
                self.pair_compare_two = self.ranks_u[i]
                # two_pair_compare[0] = pair_compare
                # two_pair_compare[1] = self.ranks_u[i]
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


# Evaluates a five card hand
# Takes list of ranks & suits [[r,s],[r,s],[r,s],[r,s],[r,s]]
# Returns evaluation code [hand_ranking, same_hand_comparison, kickers]
# Need to update to compare value of same hands
def evaluate_hand(hand):
    if not (len(hand) == 5):
        print('ERROR COMPARING HANDS for hand: ' + str(hand))
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

