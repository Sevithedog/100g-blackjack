#!python3

'''
In Blackjack, having a score over 21 is an automatic loss.
Create a function that determines if the score is a bust
'''
"""from x01_deck import createDeck
deck = createDeck()
from x02_value import makehand
hand = makehand(deck)
from x02_value import value"""
"Val = value(hand)"
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
  '''
  inputs:
  int score:  determined by another function
  
  return:
  True : user busts if the score is over 21
  False : user does not bust becuase score is 21 or less
  '''
  
  return None


def main():
  assert busts(22) == True
  assert busts(20) == False
  assert busts(21) == False
  assert busts(17) == False
  assert busts(30) == True
  
if __name__ == "__main__":
  main()
