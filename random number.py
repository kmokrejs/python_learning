import random

# generate random number from 1 to 10


def quessgame():
    rn = random.randrange(1, 10)
    # print(rn)
    c = 0
    print("""
    Rules: You have three [3] attempts to quess the number. If you type anything except numbers, the game will reload automatically. 
    Quessed number will appera at the end of the game. Good Luck!!
    """)

    for i in range(3):
        quess = input("Quess the number from 1 to 10: ")
        check = quess.isnumeric()
        c += 1
       
        checkrange = False

        while not checkrange:       
            while quess not in ["1", "2", "3", "4", "5", "6", "7","8","9", "10"]:
               quess = input("You need to insert number from 1 to 10! Try again: ")
            checkrange = True

        quess = int(quess)

        if quess == rn:
            print("Congratulations, your quess is correct!")
            cora = input("Do you want to play again? yes[y]/no[n]: ")
            if cora == 'y':
                quessgame()
            elif cora == 'n':
                quit()

        else:

            if c == 3:
                print("Correct number was", rn)
                break
            else:
                print("Wrong, try again!")

    again = input(
        "Your quesses were wrong, do you want to play again? yes[y]/no[n]: ")
    if again == 'y':
        quessgame()
    elif again == 'n':
        print("Nice to play with you, bye!")
        quit()


quessgame()
