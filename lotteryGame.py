#Lottery Game


import secrets
import sys
secretNumber=secrets.SystemRandom()

while True:
    print("____Welcome to Our Game______")
    option=int(input("Please enter Press 1 to read the rule or Press 2 to continue the game"))
    if option==1:
        print(">Age must be 18 or above<")
        print(">Show money must be above 50000<")
        print("U must use more than 1000 each")
    if option==2:
        uName=input("Please enter your name")
        uAge=int(input("Please enter your age"))
        while len(uName)>2 and uAge>17:
            print("You can play now")
            print("Welcome to our Game ",uName)
            while True:
                sMoney = int(input("Please enter your show Money"))
                while sMoney>4999:
                    while True:
                       print("This is your show Money",sMoney)
                       inputMoney=int(input("Please enter your input money amount"))
                       luckyNo=(input("Please enter your lucky number"))
                       while True:
                           print("Number must be digits")
                           if luckyNo.isdigit() and len(luckyNo)>1 and len(luckyNo)<3:
                               print("It is work.")
                               break
                           print("You should be careful!!!Number must be digits!!")
                           break
                       break
                       sysytemNo=secretNumber.randint(10,99)
                       while luckyNo==20:
                          print("You win in lottery")
                          sMoney=(inputMoney*10)+(sMoney-inputMoney)
                          print("All your money is ",sMoney)
                          toQuit=int(input("Please enter 0 if you wanna play again"))
                          if toQuit!=0:
                              sys.exit("Bye Bye")
                          else:
                              continue
                       print("Try again!!......Lucky no is ",sysytemNo)
                       sMoney=sMoney-inputMoney
                       if sMoney<1000:
                           print("Your money is insufficient")
                           break
                print("Please More Money")
        print("Please read the rule again")
