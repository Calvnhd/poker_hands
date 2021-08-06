# for testing straight out calculations in isolation

import cards

def test_straight(h):
    ranks_u = sorted(list(set(h)))
    outs_safe = []
    r_safe = []
    d = cards.Deck()
    d.shuffle()
    print('\nh: '+str(sorted(h)))
    print('ranks_u: ' + str(ranks_u))
    if len(h) == 3:
        gap = 4
    elif len(h) == 4 and len(ranks_u) >= 2:
        gap = 3
    elif len(h) == 5 and len(ranks_u) >= 3:
        gap = 2
    elif len (h) == 6 and len(ranks_u) >= 4:
        gap = 1
    else:
        gap = 0
    if gap > 0:
        scale = [1,2,3,4,5,6,7,8,9,10]
        for j in range(len(scale)):
            min = scale[j]
            max = scale[j] + 4
            in_range = 0
            for r in ranks_u:
                if (r >= min and r <= max) or (min == 1 and r == 14):
                    in_range += 1
            if in_range >= (5 - gap):
                for card in d.get_deck():
                    in_hand = False
                    for r in ranks_u:
                        if card[0] == r:
                            in_hand = True
                    if ((card[0] >=min and card[0]<=max) or (card[0] == 14 and min == 1)) and not in_hand:
                        outs_safe.append(card)
                        r_safe.append(card[0])

        if len(outs_safe) > 1:
            outs_safe = cards.remove_duplicates(outs_safe)
            r_safe = list(set(r_safe))

        print(str(int(len(outs_safe)/4)) + ' safe ranks, ' + str(len(outs_safe)) + ' cards total')
        print('safe ranks: ' + str(r_safe))
        r_safe.extend(ranks_u)
        r_safe.sort()
        print('full list: ' + str(r_safe) )

# test_straight(h=[2,8,9,14])
# test_straight(h=[6,7,8,9])
# test_straight(h=[7,7,7,8])
# test_straight(h=[7,8,7,8])
# test_straight(h=[3,3,4,10])
# test_straight(h=[5,5,11,11])
# test_straight(h=[7,7,9,9])
# test_straight(h=[7,7,7,8,9])
# test_straight(h=[7,7,7,12])
# test_straight(h=[5,7,8,9,11])
# test_straight(h=[4,7,8,9,12])
# test_straight(h=[2,7,8,9,10])
# test_straight(h=[7,8,10,11,14])
# test_straight(h=[3,4,11,14])
# test_straight(h=[7,7,7])
# test_straight(h=[7,8,9])
# test_straight(h=[7,7,8])
# test_straight(h=[7,9,9])
# test_straight(h=[2,8,11])
# test_straight(h=[2,4,14])
# test_straight(h=[2,14,14])
# test_straight(h=[2,11,14])
# test_straight(h=[7,7,7])
# test_straight(h=[2,2,2])
# test_straight(h=[13,13,13])

test_straight(h=[ 5, 7, 8, 9,11,14])
test_straight(h=[ 4, 7, 8, 9,12,13])
test_straight(h=[ 2, 7, 8, 9,10,10])
test_straight(h=[ 7, 8,10,11,14,14])
test_straight(h=[ 3, 4,11,14,10,13])
test_straight(h=[ 7, 7, 7, 6, 9,10])
test_straight(h=[ 7, 8, 9, 5, 4, 3])
test_straight(h=[ 7, 7, 8, 5, 4, 3])
test_straight(h=[ 7, 9, 9,10,11,13])
test_straight(h=[ 2, 8,11, 2, 8,11])
test_straight(h=[ 2, 4,14, 5,11, 9])
test_straight(h=[ 7, 7, 7, 3, 6, 5])
test_straight(h=[ 2, 2, 2, 3, 4, 5])
test_straight(h=[13,13,13,12,11,10])

