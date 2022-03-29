import random
from typing import List
print("Hello,this Game is from 2 players \neach one take one or two coin and the last one to take is the winner  ")
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def Game_over(list):
    if list1 == ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]:
        print("the Game is over ")
        return True
    return False


def player1():
    if Game_over(list1) == True:
        print("Player2 wins")
        quit()
    else:
       print("<Player1>")
       print(list1)
       you_want_number = int(input("Enter the number you want choose 1 or 2 :"))

       if you_want_number == 1:
          thefirstnumber = int(input("Enter the number :"))
          if thefirstnumber in list1:
            thelocation11 = list1.index(thefirstnumber)
            list1[thelocation11] = "_"
          else:
              print("your choice is wrong choose agin")
              player1()
       elif you_want_number == 2:

           thefirstnumber = int(input("Enter the first number :"))
           thesecondnumber = int(input("Enter the second number : "))

           if thefirstnumber in list1 and thesecondnumber == thefirstnumber+1:
                 thelocation11 = list1.index(thefirstnumber) 
                 thelocation22 = list1.index(thesecondnumber)
                 list1[thelocation11] = "_"
                 list1[thelocation22] = "_"

           else:
                print("your choice is wrong choose agin")
                player1()

       else:
                print("your choice is wrong choose agin")
                player1()


    
    
        
    player2()


def player2():
    if Game_over(list1) == True:
        print("player1 wins")
        quit()
    else:
        print("<Player2>")
        print(list1)
        you_want_number1 = int(input("Enter the number you want to choose 1 or 2 :"))

        if you_want_number1 == 1:
           thefirstnumber1 = int(input("Enter the number:"))
           if thefirstnumber1 in list1:
               thelocation1 = list1.index(thefirstnumber1)
               list1[thelocation1] = "_"
           else:
                print("your choice is wrong choose agin")
                quit()

       
        elif you_want_number1 == 2:
            thefirstnumber1 = int(input("Enter the first number :"))
            thesecondnumber1 = int(input("Enter the second number : "))
            if thefirstnumber1 in list1 and thesecondnumber1 == thefirstnumber1+1:
               thelocation1 = list1.index(thefirstnumber1) 
               thelocation2 = list1.index(thesecondnumber1)
               list1[thelocation1] = "_"
               list1[thelocation2] = "_"
            else:
                print("your choice is wrong choose agin")
                player2()
    
        else:
                print("your choice is wrong choose agin")
                player2()
    

    player1()
        

player1()

