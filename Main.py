def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  for i in range(4): 
      s = suits[i]
      for j in range(13):
        r = ranks[j]
        comb = s+r
        deck.append(comb)
  return deck
def makehand(deck):
  import random
  a = random.randint(0,len(deck)-1)
  b=random.randint(0,len(deck)-2)
  #print(a,len(deck),b,len(deck))
  hand = [deck.pop(a),deck.pop(b)]
  return  hand, deck
def value(hand):
  Val = [0,0]
  for i in hand:
    if i[1].isnumeric():
      Val[0]+= int(i[1])
      Val[1]+= int(i[1])
    elif i[1] == "K" or i[1] == "Q" or i[1] == "J" or i[1] == "T":
      Val[0] += 10
      Val[1] += 10
    elif i[1] == "A":
      Val[0] += 1
      Val[1] += 11
  if Val[0] == Val[1]:
    return Val[0]
  elif Val[0]< 21 and Val[1] > 21:
    return Val[0] 
  else:
    return Val
def busts(Val):
  if type(Val) == list:
    if Val[0] > 21:
      bust = True
    else:
      bust = False
  else:
    if Val > 21:
      bust = True
    else:
      bust = False
  return bust
def Dealer(deck,dealer):
  import random
  #print(dealer)
  score=0
  score = value(dealer)
  bust = busts(score)
  count = 2
  if type(score) == int:
    while score <= 16 and bust == False and type(score) == int:
      count+=1
      dealer.append(deck.pop(random.randint(0,len(deck)-1)))
      score = value(dealer)
      print(dealer)
  if type(score) == list:
    while score[1] <= 16 and bust == False and type(score) == list:
      count+=1
      dealer.append(deck.pop(random.randint(0,len(deck)-1)))
      score = value(dealer)
      print(f"Dealer: {dealer}")
  #print(dealer,score, deck)
  print(f"Dealer: {dealer}")
  return [ dealer , score , deck ]
def play(hand, deck):
  bust = False
  Blackjack= False
  Val = value(hand)
  if Val == 21:
    print("BlackJack!")
    Blackjack = True
    return Blackjack
  else:
    while bust == False:
        move = float(input("Press 0 to stand, press 1 to hit: "))
        count = 0 
        if move == 0:
          return Val, deck, hand
        elif move == 1:
          count +=1
          c = random.randint(0,len(deck)-1)
          hand.append(deck.pop(c))
          print(hand)
          Val = value(hand)
          print(Val)
          bust = busts(Val)  
    if busts(Val) == True:
      print("Bust")
      bust = True
      return bust


  
import random
"Main code"
deck = createDeck()
handcomb = makehand(deck)
hand = handcomb[0]
deck = handcomb[1]
dealer = []
a = random.randint(0,len(deck)-1)
b = random.randint(0,len(deck)-2)
dealer.append(deck.pop(a)) 
dealer.append(deck.pop(b))
print(f"Your hand: {hand}")
print(f"Dealer card: {dealer[0]}")
svalh = value(hand)
svald = value(dealer)
if type(svalh) == list and type(svald) == list and svald[1] == svalh[1] == 21:
  print(f"Dealers cards {dealer}")
  print("Blackjack push")
  exit()

elif value(hand) == 21 or value(hand[1]) == 21:
  print("Dealer Blackjack")
  exit()
elif value(dealer) == 21:
  print(f"Dealer's cards {dealer}")
  print("Dealer Blackjack")
  exit()
comba = play(hand, deck)
if comba == True:
  exit()
hand = comba[0]
deck = comba[1]
pval = comba[2]
combb = Dealer(deck,dealer)
dealer = combb[0]
dval = combb[1]
deck = combb[2]
if pval > dval:
  print("You win!!")
  exit()
elif pval == dval:
  print("Push!")
  exit()
elif pval < dval:
  print("Dealer wins :(")