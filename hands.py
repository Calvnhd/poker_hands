import cards

class Odds():
    def __init__(self):
        self.poss = [True,True,True,True,True,True,True,True,True,True]
        self.chances = [1,1,1,1,1,1,1,1,1,1]
        self.outs = []
    def update_rs(self, h):
        self.ranks = []
        self.suits = []
        for i in range(len(h)):
            self.ranks.append(h[i][0])
            self.suits.append(h[i][1])
        self.ranks.sort()
        self.ranks_set = set(self.ranks)
        self.suits_set = set(self.suits)
    def update(self, h, d):
        self.update_chances(h,d)
        self.update_poss(h,d)
    def update_chances(self,h,d):
        # check that we still have more cards to come?? (len(h) < 5)
        self.update_rs(h) # separates h[] into ranks[], suits[], ranks_set{}, suits_set{} 
        for i in range(len(self.chances)):
            if i == 0: # High card is always possible
                self.chances[i] = 1
            elif i == 1: # Pair
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    # check length of set(ranks) for duplicates
                    # Either the pair is made, or theres a (3*4)/remaining chance of hitting the pair 
                    pass
            elif i == 2: # Two pair
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    # check that a pair has been hit
                    # if yes, (2*3)/remaining chance to hit two pair
                    if len(self.ranks_set) == 4: # no pairs made
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 3: # one pair made
                        self.chances[i] = (3 * 2) / d.get_size()
                    elif len(self.ranks_set) <= 2:
                        # hand might be made, or 3 of a kind made...
                        pass
            elif i == 3: # Trips
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    if len(self.ranks_set) > 3:
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 3:
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 2:
                        pass # maybe made, maybe get outs
                    elif len(self.ranks_set) == 1: # hand made
                        self.chances[i] = 1
            elif i == 4: # Straight
                if len(h) <= 1:
                    self.chances[i] = 1
                elif len(h) > 1:
                    if len(self.ranks_set) != len(h):
                        self.chances[i] = 0
                    else:
                    # check straight range
                    # open or inside
                    # count missing values
                        pass
            elif i == 5: # Flush
                if len(self.suits_set) != 1:
                    self.chances[i] = 0
                else:
                    self.chances[i] = (13 - len(h)) / d.get_size()
            elif i == 6: # Full House
                if len(h) < 3:
                    self.chances[i] = 1
                elif len(h) == 3:
                    pass
                elif len(h) == 4:
                    pass
            elif i == 7: # Quads
                if len(h) <= 1:
                    self.chances[i] = 1
                elif len(self.ranks_set) >= 3:
                    self.chance[i] = 0
                else: 
                    pass
            elif i == 8: # Straight Flush
                if len(self.suits_set) != 1:
                    self.chances[i] = 0
                else:
                    pass
            elif i == 9: # Royal Flush
                royal_ranks = True
                for j in range(len(self.ranks)):
                    if self.ranks[j] < 10:
                        royal_ranks = False
                        break
                if royal_ranks and len(self.suits_set) == 1:
                    self.chances[i] = (5 - len(h)) / d.get_size()
                else:
                    self.chances[i] = 0
    def update_poss(self, h, d):
        for i in range(len(self.poss)):
            if self.chances[i] > 0:
                self.poss[i] = True
            else:
                self.poss[i] = False
    def update_outs_count(self, h, d):
        for i in range(len(self.chances)):
            if i == 0: # High card is always possible
                self.chances[i] = 1
            elif i == 1: # Pair
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    # check length of set(ranks) for duplicates
                    # Either the pair is made, or theres a (3*4)/remaining chance of hitting the pair 
                    pass
            elif i == 2: # Two pair
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    # check that a pair has been hit
                    # if yes, (2*3)/remaining chance to hit two pair
                    if len(self.ranks_set) == 4: # no pairs made
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 3: # one pair made
                        self.chances[i] = (3 * 2) / d.get_size()
                    elif len(self.ranks_set) <= 2:
                        # hand might be made, or 3 of a kind made...
                        pass
            elif i == 3: # Trips
                if len(h) < 4:
                    self.chances[i] = 1
                elif len(h) == 4:
                    if len(self.ranks_set) > 3:
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 3:
                        self.chances[i] = 0
                    elif len(self.ranks_set) == 2:
                        pass # maybe made, maybe get outs
                    elif len(self.ranks_set) == 1: # hand made
                        self.chances[i] = 1
            elif i == 4: # Straight
                if len(h) <= 1:
                    self.chances[i] = 1
                elif len(h) > 1:
                    if len(self.ranks_set) != len(h):
                        self.chances[i] = 0
                    else:
                    # check straight range
                    # open or inside
                    # count missing values
                        pass
            elif i == 5: # Flush
                if len(self.suits_set) != 1:
                    self.chances[i] = 0
                else:
                    self.chances[i] = (13 - len(h)) / d.get_size()
            elif i == 6: # Full House
                if len(h) < 3:
                    self.chances[i] = 1
                elif len(h) == 3:
                    pass
                elif len(h) == 4:
                    pass
            elif i == 7: # Quads
                if len(h) <= 1:
                    self.chances[i] = 1
                elif len(self.ranks_set) >= 3:
                    self.chance[i] = 0
                else: 
                    pass
            elif i == 8: # Straight Flush
                if len(self.suits_set) != 1:
                    self.chances[i] = 0
                else:
                    pass
            elif i == 9: # Royal Flush
                royal_ranks = True
                for j in range(len(self.ranks)):
                    if self.ranks[j] < 10:
                        royal_ranks = False
                        break
                if royal_ranks and len(self.suits_set) == 1:
                    self.chances[i] = (5 - len(h)) / d.get_size()
                else:
                    self.chances[i] = 0
    def get_possible(self):
        return self.poss
    def get_chances(self):
        return self.chances
    def get_outs(self):
        return self.outs



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

