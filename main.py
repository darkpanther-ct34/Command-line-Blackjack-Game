import random
import time
import json
import os

File = "Balance.txt"

def write_json(data, filename=File):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


with open(File) as json_file:
    data = json.load(json_file)

validSave = False

if len(data) == 0:
        print("There are no save files.")
        SaveName = str(input("What do you want to name your first save?  "))
        data[SaveName] = "100.00"
        write_json(data)
else:
  print("Save files: ")
  for save in data:
      print("   "+save+": £"+"%.2f" % float(data[save]))
  print("")
  while not validSave:
      save_found = False

      SaveName = str(input("What save do you want to use?  "))

        
      for save in data:
          if save == SaveName:
              save_found = True
              break

          

      if save_found == True:
          if float(data[SaveName]) <= 0:
              print("That save ran out of money and cannot be used.")
          else:
              print("Save opened.")
              validSave = True
          time.sleep(0.5)
      
      else:
          ValidChoice = False
          while not ValidChoice:
              choice = str(input("That save doesnt exist, do you want to make a new one? y/n   "))
              if choice == "y":
                  data[SaveName] = "100.00"
                  write_json(data)
                  ValidChoice = True
                  validSave = True
              elif choice == "n":
                  validSave = False
                  ValidChoice = True
              else:
                  print("Thats an invalid choice, please enter y/n  ")
        


with open(File) as json_file:
    data = json.load(json_file)
    bal=float(data[SaveName])
            
play=True
score=0
dealerscore=0
while play==True:
    bal = round(bal, 2)
    number = [2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 10,10,10,10, 10,10,10,10, 10,10,10,10, 11,11,11,11]
    suit = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    playeronecard1 = random.choice(number)
    playeronesuit1 = random.choice(suit)
    number.remove(playeronecard1)
    playeronecard2 =random.choice(number)
    playeronesuit2 = random.choice(suit)
    number.remove(playeronecard2)
    if playeronecard1==11 and playeronecard2==11:
        playeronecard2=1
    if playeronecard1 == playeronecard2 and playeronesuit1 == playeronesuit2:
        while playeronesuit1 == playeronesuit2:
            playeronesuit2=random.choice(suit)
    validinput=False
    while not validinput:
      os.system("printf '\033c'") 
      bet = input("Your balance is £"+ "%.2f" % float(bal) + ", what do you want to bet?\n")
      try:
        bet = float(bet)
        validinput = True
        if bet>bal:
          print("You don't have that much!")
          validinput = False
          time.sleep(0.5)
        else:
          bal -= bet
          validinput = True
      except:
        print("Thats not a number.")
        validinput = False
        time.sleep(0.5)
      os.system("printf '\033c'") 


    print(str(playeronecard1) + ' ' + playeronesuit1)
    time.sleep(0.5)
    print(str(playeronecard2) + ' ' + playeronesuit2)
    time.sleep(0.5)
    playeronetotal=playeronecard1+playeronecard2
    print("Your total is " + str(playeronetotal) + '.')
    Q=input("Do you want another card? y/n ")
    bust=False
    if Q=="y" and bust == False:
       os.system("printf '\033c'") 
       playeronecard3=random.choice(number)
       playeronesuit3=random.choice(suit)
       number.remove(playeronecard3)
       playeronetotal = playeronecard1 + playeronecard2 + playeronecard3
       if playeronecard3==11 and playeronetotal>21:
           playeronecard3=1
       if playeronecard1 == playeronecard3 and playeronesuit1 == playeronesuit3 or playeronecard2 == playeronecard3 and playeronesuit2 == playeronesuit3:
           while playeronesuit1 == playeronesuit3 or playeronesuit2 == playeronesuit3:
            playeronesuit3 = random.choice(suit)
       print(str(playeronecard1) + ' ' + playeronesuit1)
       time.sleep(0.5)
       print(str(playeronecard2) + ' ' + playeronesuit2)
       time.sleep(0.5)
       print(str(playeronecard3) + ' ' + playeronesuit3)
       time.sleep(0.5)
       playeronetotal=playeronecard1+playeronecard2+playeronecard3
       print("Your total is " + str(playeronetotal) + '.')
       if playeronetotal>21:
           print("You went bust.")
           bust=True
       if bust==False:
           Qu=input("Do you want another card? y/n ")
           if Qu=="y":
               os.system("printf '\033c'") 
               playeronecard4=random.choice(number)
               playeronesuit4=random.choice(suit)
               number.remove(playeronecard4)
               playeronetotal = playeronecard1 + playeronecard2 + playeronecard3 + playeronecard4
               if playeronecard4 == 11 and playeronetotal > 21:
                   playeronecard4=1
               if playeronecard1 == playeronecard4 and playeronesuit1 == playeronesuit4 or playeronecard2 == playeronecard4 and playeronesuit2 == playeronesuit4 or playeronecard3 == playeronecard4 and playeronesuit3 == playeronesuit4:
                   while playeronesuit1 == playeronesuit4 or playeronesuit2 == playeronesuit4 or playeronesuit3 == playeronesuit4:
                       playeronesuit4 = random.choice(suit)
               print(str(playeronecard1) + ' ' + playeronesuit1)
               time.sleep(0.5)
               print(str(playeronecard2) + ' ' + playeronesuit2)
               time.sleep(0.5)
               print(str(playeronecard3) + ' ' + playeronesuit3)
               time.sleep(0.5)
               print(str(playeronecard4) + ' ' + playeronesuit4)
               time.sleep(0.5)
               playeronetotal=playeronecard1+playeronecard2+playeronecard3+playeronecard4
               print("Your total is " + str(playeronetotal) + '.')
               if playeronetotal>21:
                   print("You went bust.")
                   bust = True
               if bust==False:
                   Que=input("Do you want another card? y/n ")
                   if Que=="y" and bust==False:
                       os.system("printf '\033c'") 
                       playeronecard5=random.choice(number)
                       playeronesuit5=random.choice(suit)
                       number.remove(playeronecard5)
                       playeronetotal = playeronecard1 + playeronecard2 + playeronecard3 + playeronecard4 + playeronecard5
                       if playeronecard5 == 11 and playeronetotal > 21:
                           playeronecard5=1
                       if playeronecard1 == playeronecard5 and playeronesuit2 == playeronesuit5 or playeronecard2 == playeronecard5 and playeronesuit2 == playeronesuit5 or playeronecard3 == playeronecard5 and playeronesuit3 == playeronesuit5 or playeronecard4 == playeronecard5 and playeronesuit4 == playeronesuit5:
                           while playeronecard1 == playeronecard5 and playeronesuit2 == playeronesuit5 or playeronecard2 == playeronecard5 and playeronesuit2 == playeronesuit5 or playeronecard3 == playeronecard5 and playeronesuit3 == playeronesuit5 or playeronecard4 == playeronecard5 and playeronesuit4 == playeronesuit5:
                               playeronesuit5 = random.choice(suit)
                       print(str(playeronecard1) + ' ' + playeronesuit1)
                       time.sleep(0.5)
                       print(str(playeronecard2) + ' ' + playeronesuit2)
                       time.sleep(0.5)
                       print(str(playeronecard3) + ' ' + playeronesuit3)
                       time.sleep(0.5)
                       print(str(playeronecard4) + ' ' + playeronesuit4)
                       time.sleep(0.5)
                       print(str(playeronecard5) + ' ' + playeronesuit5)
                       time.sleep(0.5)
                       playeronetotal=playeronecard1+playeronecard2+playeronecard3+playeronecard4+playeronecard5
                       print("Your total is " + str(playeronetotal) + '.')
                       if playeronetotal>21:
                           print("You went bust.")
                           bust = True
    dealercard1=random.choice(number)
    number.remove(dealercard1)
    dealercard2=random.choice(number)
    number.remove(dealercard2)
    if dealercard1 == 11 and dealercard2 == 11:
        dealercard1=1
    dealertotal=dealercard1 + dealercard2
    if dealertotal<17:
       dealercard3 = random.choice(number)
       number.remove(dealercard3)
       dealertotal = dealercard1 + dealercard2 + dealercard3
       if dealercard3 == 11 and dealertotal > 21:
           dealercard3=1
       dealertotal = dealercard1 + dealercard2 + dealercard3
       if dealertotal < 17:
           dealercard4 = random.choice(number)
           number.remove(dealercard4)
           dealertotal = dealercard1 + dealercard2 + dealercard3 + dealercard4
           if dealercard4 == 11 and dealertotal > 21:
               dealercard4 = 1
           dealertotal = dealercard1 + dealercard2 + dealercard3 + dealercard4
           if dealertotal < 17:
               dealercard5 = random.choice(number)
               number.remove(dealercard5)
               dealertotal = dealercard1 + dealercard2 + dealercard3 + dealercard4 + dealercard5
               if dealercard5 == 11 and dealertotal > 21:
                   dealercard5 = 1
               dealertotal = dealercard1 + dealercard2 + dealercard3 + dealercard4 + dealercard5
    time.sleep(1)
    print("The dealer total is " + str(dealertotal) + '.')
    time.sleep(1)
    bothBust = False
    if dealertotal>playeronetotal and dealertotal<22 and playeronetotal<22:
       print('The dealer wins.')
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       time.sleep(1)
    elif dealertotal<22 and playeronetotal<22 and dealertotal<playeronetotal:
       print("You Win!")
       bal += bet*2
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       time.sleep(1)
    if playeronetotal<22 and not dealertotal<22:
       print("You win!")
       bal += bet*2
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       time.sleep(1)
    if not playeronetotal<22 and dealertotal<22:
       print("The dealer wins.")
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       time.sleep(1)
    if not playeronetotal<22 and not dealertotal<22:
       print("You both went bust.")
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       bothBust = True
       time.sleep(1)
    if playeronetotal==dealertotal and not bothBust:
       print("Its a draw!")
       bal += bet
       bal = round(bal, 2)
       print( "You have £"+"%.2f" % float(bal)+".")
       time.sleep(1)
    if bal > 0.00:   
      keepplay=input('Do you want to keep playing? y/n ')
      if keepplay=='y':
          play=True
      elif keepplay=='n':
          play=False
    else:
      print("Oh, no! You ran out of money!")
      play=False
      bal = round(bal, 2)
      
    with open(File) as json_file:
        data = json.load(json_file)
    data[SaveName] = str(bal)
    write_json(data)

    
    time.sleep(1)

