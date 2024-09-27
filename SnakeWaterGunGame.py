#snake water gun
import random
print("Welcome to snake water gun programmed by Mudit Agrawal")
#l1=["Snake", "Water", "Gun"]
M=int("10")
CP=0
HP=0
while True:
    M=M-1
    #move = random.choice(l1)
    pos = random.randrange(1,10)
    if pos <= 3:
        move = "Snake"
    elif pos > 3 and pos <= 6:
        move = "Water"
    else:
        move = "Gun"
    n1= input("Please enter your move,\nS for Snake W for Water and G for Gun\n")
    n= n1.upper()
    print("Computer played:", move)
    if n=="S" and move=="Gun":
        print("Your snake is killed by Gun and you lost")
        CP=CP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="S" and move=="Water":
        print("Your snake drank all the water and you won")
        HP=HP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="S" and move=="Snake":
        print("round tied because of same moves")
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="W" and move=="Snake":
        print("the snake drank all your water and you lost")
        CP=CP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="W" and move=="Gun":
        print("the gun sank in your water and you won")
        HP=HP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="W" and move=="Water":
        print("round tied because of same moves")
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="G" and move=="Gun":
        print("round tied because of same moves")
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="G" and move=="Water":
        print("your gun sank in the water and you lost")
        CP=CP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    elif n=="G" and move=="Snake":
        print("the snake is killed by your Gun and you won")
        HP=HP+1
        print("Computer's points are",CP)
        print("Your points are",HP)
    if M==0:
        print("Game over")
        break
if HP>CP:
    print("Congratulations YOU WON")
elif CP>HP:
    print("Sorry, YOU LOST\nBetter luck next time.")
elif CP==HP:
    print("The match is tied!")
