import random
# import subprocess

# subprocess.call(["cls"])
print("Welcome to Abdul's Rock-Paper-Scissors.")
name = input("Please Enter Your Name => ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
           
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(f"Hi {name} Select What Do You Want To Choose.")
user_input_nint = input("\nROCK =>1 \nPAPER =>2 \nSCISSORS =>3\nPlease Enter A Choice Hear => ")
user_input = int(user_input_nint)
coumputer_output = random.randint(1, 3)
print(f"{name}'s")
if user_input == 1  :
    print(rock)
elif user_input == 2  :
    print(paper)
elif user_input == 3  :
    print(scissors)
else:
    print("Please Enter \n1 for Rock\n2 for Paper\n3 for Scissorss")
print("Coumputer's")
if coumputer_output == 1  :
    print(rock)
elif coumputer_output == 2  :
    print(paper)
elif coumputer_output == 3  :
    print(scissors)
if  coumputer_output == 1 and user_input == 2:
    print(f"Hay {name} you won The Match")
elif coumputer_output == 2 and user_input == 3:
    print(f"Hay {name} you won The Match")
elif coumputer_output == 3 and user_input == 1:
    print(f"Hay {name} you won The Match")
elif coumputer_output == user_input :
    print(f"{name} This Match is tie")
else:
    print(f"{name} Sorry You lost the game")
print(f"Thanks {name} For Playing Abdul's Rock-Paper-Scissors. ")
k=input("press close to exit") 