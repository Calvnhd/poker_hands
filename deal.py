import cards
import hands

d = cards.Deck()
o = hands.Odds() 

i = 0
done = False
while not done:
    d.shuffle()
    h = []
    while len(h) < 5:
        print('DEALING CARD -----------------------------------------------------------------------------------')
        print('DECK: ' + str(d.get_deck()))
        h.append(d.take_card())
        o.update(h,d)
        if len(h) != 5:
            print('=====================================================================')
            print('hand: ' + str(h))
            # print(o.get_possible())
            print(o.get_chances_safe())
            print(o.get_chances_hit())
            o.print_outs()
            print('=====================================================================\n\n')
        else:
            eval = hands.evaluate_hand(h)
            print('Complete hand: ' + str(h) + ' ... ' + str(hands.interpret_eval(eval)) + '\n')
    i += 1
    if eval[0] >= 3:
        if h[0][0] == h[1][0] and h[0][0] == h[2][0] or eval[0] >= 6:
            done = True
print('Finished after ' + str(i) + ' hands')