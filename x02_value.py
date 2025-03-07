#!python3
from x01_deck import createDeck
deck = createDeck()
def makehand(deck):
  import random
  a = random.randint(0,len(deck)-1)
  b=random.randint(0,len(deck)-2)
  print(a,len(deck),b,len(deck))
  hand = [deck.pop(a),deck.pop(b)]
  return  hand


hand = makehand(deck)
print(hand)

def value(hand):
  #hand[1] = input()
  #hand[2] = input()
  Val = [0,0]
  for i in hand:
    print(i , i[1])
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
    print(Val[0])
    return Val[0]
  elif Val[0]< 21 and Val[1] > 21:
    print(Val[0])
    return Val[0] 
  else: 
    print(Val)
    return Val



    




value(hand)

'''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
'''
  



def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
