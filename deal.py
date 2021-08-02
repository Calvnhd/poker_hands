import cards
import hands

d = cards.Deck()
d.shuffle()
o = hands.Odds() 

h = []
while len(h) < 5:
    h.append(d.take_card())
    print(h)
    o.update(h,d)
    print(o.get_possible())

