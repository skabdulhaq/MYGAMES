import random
# import subprocess

a=[''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''',
]
print(random.choice(a))


name = input("Please enter Player's name ==>> ")

print(f"Hi {name} Welcome to Hangman")
print("Guess a letter which is in this word")
hmp = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''' ]
# print(word)
word_list = ["ardvark", "camel"]+['ant', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'fox', 'frog', 'goat', 'goose', 'lion', 'lizard', 'monkey', 'mouse', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit',  'rat',  'rhino', 'seal', 'shark', 'sheep', 'snake', 'spider',  'swan', 'tiger',  'turkey', 'turtle', 'whale', 'wolf',  'zebra']
choosen_word = random.choice(word_list)
len_word = len(choosen_word)
# print(choosen_word)
y=[]
a=["_"]
for x in range(0, len_word):
    y=y+a
# print(y)
z = ""
b = "_"
for somthing in range (len_word):
    z = z+b
print(z)
life = 6
end = False
choosen_word_list = []
for x in choosen_word:
    choosen_word_list.append(x)
while end == False:
    # subprocess.call([cls])
    guess_lower = input("Guess a letter =>> ").lower()
    if guess_lower in y:
        print(f"The word you entered is already guessed by you. ")
    for letter in range(len_word):
        x = choosen_word_list[letter]
        someone = False
        if x == guess_lower:
            y[letter] = guess_lower
            someone = True

    s=""

    for som in y:
        s = s+som
    print(s)
    if someone==True:
        print(f"Yes you are correct the letter {guess_lower} is in the word")

    # if guess_lower in y:
    #     print(f"The word you entered is already guessed by you. ")
    if guess_lower not in choosen_word:
        life = life -1
        print(f"the letter {guess_lower} is not in the word hurry up save hungman.")

    if life < 6 :
        print(hmp[life])
        # print(f"Hurry up save hungman")
    if life == 0 :
        end = True
        print("You lose.")
        print(choosen_word)
    if "_" not in y:
        end = True
        print("you won.")
