import random
import string

words = ["ford", "audi", "bmw", "citroen", "skoda", "porsche", "ferrari", "mercedes", "renault"]

def choose_word(words):
    word = random.choice(words)

    return word.upper()

def hangman():
    word = choose_word(words)
    word_lett = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_lett) > 0 and lives > 0:
        print("You have", lives, "lives left and you have already used: ", " ".join(used_letters))
    
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_lett:
                word_lett.remove(user_letter)
            
            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print("You have already used that character. Try again!")

        else:
            print("Invalid character! Try again.")

    if len(word_lett) == 0:
        print(f"Congratulations, you won! The correct word was {word}.")
        print()
    elif lives == 0:
        print(f'You ran out of lives. Sorry. You lost! Correct word was {word}.')
        print()


hangman()