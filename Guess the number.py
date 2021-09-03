import random
import os
from LOGO import ART


def clear():
    os.system('cls')


def clues(answer, guess):
     if answer > guess:
         return "Oh! Your Guess is too low."
     elif answer < guess :

         return "Oh! Your Guess is too high."

     elif answer == guess:
         return "Absolutely Correct."
         # answred = True


print(random.choice(ART))
play = True
while play:
    clear()
    print("Welcome to guess the number")
    level = input("Choose a difficulty level .Type easy(e) or medium(m) or hard(h)").lower()
    print("I Guessed of a number between 1 to 100")
    chances = 0
    if level == "e" or level == "easy":
        chances = 10
    elif level == "m"or level =="medium":
        chances = 7
    elif level == "h" or level == "hard":
        chances = 5
    randnumb = random.randint(0, 100)
    game_end = False
    while not game_end:
        print(f"you have only {chances} chances.")
        choice = int(input("Guess what number did i guessed \n"))
        print(clues(randnumb, choice))
        chances = chances-1
        if chances == 0 or clues(randnumb, choice) == "Absolutely Correct.":
            game_end = True
            if not clues(randnumb, choice) == "Absolutely Correct.":
                print(f"Your out of your guesses the correct number is {randnumb}")
    y = input("To play again Type 'yes' or 'y'\nTo quit the game type 'no' or 'n'\n").lower()
    if y == "n" or y == "no":
        play = False
    clear()

