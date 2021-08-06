import cards
import hands

d = cards.Deck()
o = hands.Odds() 

i = 0
done = False
while not done:
    print('loop ' + str(i))
    d.shuffle()
    # d.bias_deck(8)
    h = []
    while len(h) < 7:
        input("Press Enter to deal a card \n")
        print('DEALING CARD -----------------------------------------------------------------------------------')
        h.append(d.take_card())
        o.update(h,d)
        if len(h) >= 5:
            # make_hands expects hand + board. Slicing adapts to suit this.
            h_h = h[:2]
            h_b = h[2:]
            best_hand = hands.make_hands(h_h,h_b)
            print('Best hand: ' + str(h) + ' ... ' + str(hands.interpret_eval(best_hand)) + '\n')
        if len(h) != 7:
            print('*********************************************************************')
            print('hand: ' + str(h))
            print(o.get_chances_safe())
            print(o.get_chances_hit())
            o.print_outs()
            print('=====================================================================\n\n')
    i += 1
    if best_hand[0] >= 7:
        # if h[0][0] == h[1][0] and h[0][0] == h[2][0] or eval[0] >= 6:
        done = True
print('Finished after ' + str(i) + ' hands')