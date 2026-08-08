# Best logic i have ever made connected with main.py the snake water gun game :

import random

computer = random.choice([1, -1 , 0])
youstr = input("Enter your choice : ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "sanke", -1 : "water",  0 : "gun"}
you = youdict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if((computer - you) == -1 or (computer - you) == 2):
    print("You lose !")
else:
    print("You win !")