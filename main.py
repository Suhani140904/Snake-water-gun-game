'''

snake = 1
water = -1
gun = 0


'''
import random
computer = random.choice([1, -1, 0])
yourstr = input("Enter your choice: ")
yourDict = {"s" : 1 ,
           "w" : -1 ,
           "g" : 0}
reverseDict = {1 : "snake" ,
            -1 : "water" , 
            0 : "gun"}

you = yourDict[yourstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else:
    if(computer == 1 and you == 0):
        print("YOU WIN")

    elif(computer == 1 and you == -1 ):
        print("YOU LOSE")

    elif(computer == -1 and you == 0):
        print("YOU LOSE")

    elif(computer == -1 and you == 1 ):
        print("YOU WIN")

    elif(computer == 0 and you == 1):
        print("YOU WIN")

    elif(computer == 0 and you == -1 ):
        print("YOU LOSE")

    else:
        print("Something went wrong !")       

