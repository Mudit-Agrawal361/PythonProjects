import random
import os
import sys
import subprocess

def clear_and_restart():
    """Clears the terminal and restarts the script."""

    # Clear the terminal
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

    # Restart the script
    subprocess.call(["python", sys.argv[0]])
    sys.exit()


while True:
    w= random.randrange(1, 1000)
    if type(w)==float:
        print("you are being fooled")
    elif w>1000:
        print("the number hidden or the500 correct number is greater than 1000")
    elif w<1:
        print("the number hidden or the correct number is smaller than 1000")
    else:
        print("Welcome, to mind games programmed by Mudit Agrawal")
        print("Rules:\n You have to guess a number. And to guess it, you have only 11 chances")
        print("Clue the number is between 1 to 1000")
        chances= 11
        while(True):
            n= int(input("Enter the number here:\n"))
            chances=chances-1
            if n==w:
                print("Congratulations, you have won")
                print("You have finished in",(11-chances), "chances\n")
                print("if you want to continue enter Y and if you want to stop enter anything else")
                e=input()
                B=e.upper()
                if B=="Y":
                    clear_and_restart()
                else:
                    break
            elif chances==0:
                print ("Game over\n","The correct number was",w)
                print("if you want to continue enter Y and if you want to stop enter anything else")
                e=input()
                B=e.upper()
                if B=="Y":

                    clear_and_restart()
                else:
                    break        
            elif n>w:
                print("The number entered is Greater than the correct number")
                print("Chances left:",chances)
                continue    
            elif n<w:
                print("The number entered is smaller then the correct number")
                print("Chances left:",chances)
                continue
