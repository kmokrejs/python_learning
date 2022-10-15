

def rps():
    import random
    user_wins = 0
    pc_wins = 0
    print()

    print("""Welcome to the game 'Rock, Paper, Scissors'. 
    Rules: You have to insert only inputs, that you are told to. If you type something wrong, round will be skipped. 
    Winner is decided from 5 rounds. If it is draw, you should play again to decide the winner.   """)
    print()
    for count in range(5):

        game_input = ("Rock", "Paper", "Scissors")
        options = ['rock', 'paper', 'scissors']

        user_input = input("Type 'r' for Rock, 'p' for Paper, 's' Scissors  or 'q' to quit: ").lower()
        if user_input == 'q':
            break

        
        while user_input not in ['r', 'p', 's', 'q']:
            user_input = input("Type 'r' for Rock, 'p' for Paper, 's' Scissors  or 'q' to quit: ").lower()
            if user_input == 'q':
                break


        # let the user know what pc draws
        pc_draw = random.choice(game_input)

        print("PC pick:", pc_draw + ".")

        # asserting number to pc draw
        if pc_draw == "Rock":
            pc_numb = 0
        elif pc_draw == "Paper":
            pc_numb = 1
        elif pc_draw == "Scissors":
            pc_numb = 2

        # asserting number to user input
        if user_input == "r":
            user_numb = 0

        elif user_input == "p":
            user_numb = 1

        elif user_input == "s":
            user_numb = 2

        # scenarios of win of the user
        if user_input == "r" and pc_draw == "Scissors":
            user_wins += 1
            print("You won!")
        elif user_input == "p" and pc_draw == "Rock":
            user_wins += 1
            print("You won!")
        elif user_input == "s" and pc_draw == "Paper":
            user_wins += 1
            print("You won!")
        elif user_numb == pc_numb:
            print("Draw!")
        else:
            pc_wins += 1
            print("PC wins!")

    print()
    print("Score is:", user_wins, ":",  pc_wins)
    if user_wins > pc_wins:
        print("Congratulations, you won the game!!")
    elif user_wins < pc_wins:
        print("PC won. Good luck next time")
    elif user_wins == pc_wins:
        print("It is a draw, you should play again to decide!")
    again = input("Do you want to play again? yes[y]/no[n]: ")
    if again == "y":
        rps()
    else:
        quit()


rps()
