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

def main():
  assert busts(22) == True
  assert busts(20) == False
  assert busts(21) == False
  assert busts(17) == False
  assert busts(30) == True
  
if __name__ == "__main__":
  main()
