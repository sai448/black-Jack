import random
from art import logo
flag=True
def sd():
  """Decision maker"""
  if sum(a)>sum(computer_choose):
      print("You won")
      
  elif sum(a)==sum(computer_choose):
      print("Draw") 
      
  else:
      print("you lose")
def kgf(q):
  """Choose one if Ace card comes and if score >21"""
  if q==11 and sum(computer_choose)>=11:
    computer_choose.append(1)
  else:
    computer_choose.append(q)    
def wer():
  """Start of the program"""
  global cards,a,computer_choose,flag
  flag=True
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  a=random.sample(cards,2)
  computer_choose=random.sample(cards,1)
  controlller=input("Do you want to continue:")
  if controlller=='y':
    print(logo)
    print("your cards:",a,", your current score is:",sum(a))
    print("computer choose:",computer_choose) 
wer()       
#logic 
while flag==True:
  if input("Take 'y' to get another card , type n to pass:")=="y":
     a.append(random.choice(cards))
     print("your cards:",a,", your current score is:",sum(a))
     print("computer choose:",computer_choose) 
     if sum(a)>21:
       print("you lose")
       flag=False
       wer()
  else:
    print("Your final score is:",a,",final score:",sum(a))
    kgf(random.choice(cards))
    #computer_choose.append(random.choice(cards))
    print("Computer final hand is:",computer_choose,", final score is:",sum(computer_choose))
    if sum(computer_choose)>=17:
      sd()
      flag=False
      wer()
    while sum(computer_choose)<17:
      kgf(random.choice(cards))
      #computer_choose.append(random.choice(cards))
      if sum(computer_choose)>21:
        print("Computer Final score:",sum(computer_choose))
        print("You won, dealer score is more than 21")
        flag=False
        wer()
        
      else:
        print("Computer final hand is:",computer_choose,", final score is:",sum(computer_choose))
        if (sum(computer_choose)>17):
          sd()
          flag=False
          wer()