import cards
import hands

d = cards.Deck()
o = hands.Odds() 

i = 0
done = False
while not done:
    print(f'***   Hand number {i}   ***')
    d.shuffle()
    # d.bias_deck(9)
    h = []
    while len(h) < 7:
        input("Press Enter to deal a card \n")
        print('DEALING CARD -----------------------------------------------------------------------------------')
        h.append(d.take_card())
        o.update(h,d)
        
        if len(h) <= 7:
            print('*********************************************************************')
            # print('hand: ' + str(h))
            # print(f'safe: {o.get_chances_safe()}')
            # print(f' hit: {o.get_chances_hit()}')
            o.print_info()
            print('=====================================================================\n\n')
    i += 1
    # if best_hand[0] >= 5:
        # if h[0][0] == h[1][0] and h[0][0] == h[2][0] or eval[0] >= 6:
        # done = True
print('Finished after ' + str(i) + ' hands')