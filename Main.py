def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  for i in range(4): 
      s = suits[i]
      for i in range(13):
        r = ranks[i]
        comb = s+r
        deck.append(comb)
  return deck
def makehand(deck):
  import random
  a = random.randint(0,len(deck)-1)
  b=random.randint(0,len(deck)-2)
  #print(a,len(deck),b,len(deck))
  hand = [deck.pop(a),deck.pop(b)]
  return  hand
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
      dealer.append(deck.pop(random.randint(0,len(deck)-count)))
      score = value(dealer)
  if type(score) == list:
    while score[1] <= 16 and bust == False and type(score) == list:
      count+=1
      dealer.append(deck.pop(random.randint(0,len(deck)-count)))
      score = value(dealer)
  #print(dealer,score, deck)
  return [ dealer , score , deck ]
def play(hand):
  bust = False
  Blackjack= False
  Val = value(hand)
  if Val == 21:
    print("BlackJack!")
    Blackjack = True
    return Blackjack
  else:
    while bust == False:
        move = input("Press 0 to stand, press 1 to hit: ")
        count = 0 
        if move == 0:
          return Val
        if move == 1:
          count +-1
          hand.append(deck.pop(random.randint(0,len(deck)-count)))
          print(hand)
          Val = value(hand)
          bust = busts(Val)  
    if busts(Val) == True:
      print("Bust")
      bust = True
      return bust
    

  
import random
"Main code"
deck = createDeck()
hand = makehand(deck)
dealer = []
a = random.randint(0,len(deck)-1)
b = random.randint(0,len(deck)-2)
dealer.append(deck.pop(a)) 
dealer.append(deck.pop(b))
print(f"Your hand: {hand}")
print(f"Dealer card: {dealer[0]}")

play(hand)
