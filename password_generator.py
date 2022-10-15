
import random


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
s_ch = ['~', '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', '>', '?', '/']

low_alph = list(map(chr, range(97, 123)))  # create lowercase alphabet
upp_alph = [var.upper() for var in low_alph]  # create uppercase alphabet

lenght = 0


def lenght_of_password():

    lenght_question = input("""How long does your password should be?
                A) 8 characters long
                B) 12 characters long
                Q) Quit the program

                You can choose by typing A/B or Q: """).lower()

    if lenght_question == 'q':
        quit()

    print()

    if lenght_question == "a":
        lenght = 8
        password = []

# add special characters
        n_of_sch = random.randrange(1, 3)
        for i in range(n_of_sch):
            password.append(random.choice(s_ch))

        lenght = lenght - n_of_sch
        pas_num = []

        # add numbers
        for n in range(2):
            pas_num.append(random.choice(numbers))

        lenght = lenght - 2
        password.extend(pas_num)

        # add lower letters
        lower_ch_n = random.randrange(2, 4)
        low_ch = []

        for u in range(lower_ch_n):
            low_ch.append(random.choice(low_alph))

        lenght = lenght - lower_ch_n
        password.extend(low_ch)

        # add upper letters
        upp_ch_n = lenght
        upp_ch = []

        for u in range(upp_ch_n):
            upp_ch.append(random.choice(upp_alph))

        lenght = lenght - upp_ch_n
        password.extend(upp_ch)
        random.shuffle(password)


    # 12 character password
    if lenght_question == "b":
        lenght = 12
        password = []
    # add special characters
        
        for i in range(2):
            password.append(random.choice(s_ch))

        lenght = lenght - 2
        pas_num = []

        # add numbers
        for n in range(3):
            pas_num.append(random.choice(numbers))

        lenght = lenght - 3
        password.extend(pas_num)

        # add lower letters
     
        low_ch = []

        for u in range(4):
            low_ch.append(random.choice(low_alph))

        lenght = lenght - 4
        password.extend(low_ch)

        # add upper letters
        upp_ch_n = lenght
        upp_ch = []

        for u in range(upp_ch_n):
            upp_ch.append(random.choice(upp_alph))

        lenght = lenght - upp_ch_n
        password.extend(upp_ch)
        random.shuffle(password)
    
    x = ''.join(password)
    print()
    print("Your password is:", x)
    print()
    another = input("Do you want to generate another password? yes[y]/no[n]: ").lower() 

    if another == 'no' or another == 'n':
        quit()
    elif another == 'yes' or another == 'y':
        lenght_of_password()
    else:
        print("You need to type Y or N. Shutting down prorgamm...")
        quit()

lenght_of_password()
