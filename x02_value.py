#!python3
from x01_deck import createDeck
deck = createDeck()
def makehand(deck):
  import random
  hand = [deck.pop(random.randint(0,51)),deck.pop(random.randint(0,51))]
  return  hand

hand = makehand(deck)
print(hand)

def value(hand):
  valN = 0
  if "A" in hand:

  else:
    for i in hand:
    print(i , i[1])
    if i[1].isnumeric():
      valN += int(i[1])
    elif i[1] == "K" or i[1] == "Q" or i[1] == "J":
      valN += 10
  

  print(valN)
    



print(value(hand))

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
