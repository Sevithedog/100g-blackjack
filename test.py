#from x01_deck import createDeck
deck = createDeck()
from x02_value import value
from x03_bust import busts
def dealer(deck):
  import random
  #deck = deck
  dealer = []
  score = 0
  #a = random.randint(0,len(deck)-1)
  #b = random.randint(0,len(deck)-2)
  dealer.append(deck.pop(a)) 
  dealer.append(deck.pop(b))
  #print(dealer)
  #score = value(dealer)
  #bust = busts(score)
  count = 2
  while score <=16 and bust == False:
    count+=1
    dealer.append(deck.pop(random.randint(0,len(deck)-count)))
    score = value(dealer)
  #print(dealer,score,deck)