import random
import time


def roller():
    print("Rolling the dices...")
    time.sleep(2)

    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    print(f"You rolled {dice1} and {dice2}.")
    print("")

    restart = input("Do you wanna roll again? 'Y' - yes; 'N' - no: ").upper()
    while restart != "Y" or "N":
        if restart == "Y":
            roller()
        elif restart == "N":
            exit()


print("Welcome to 'The Dice'")
start = input(
    """ Press 'Y' to roll the dice or 'E' to exit the program: """).upper()

if start == "Y":
    roller()
elif start == "E":
    exit()
else:
    again = True
    while again == True:
        start = input(
            """ Press 'Y' to roll the dice or 'E' to exit the program: """).upper()
        if start == "Y":
            again == False
            roller()
        elif start == "E":
            exit()
        else:
            again == True
