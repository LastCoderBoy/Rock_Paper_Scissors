import random
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

ask_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
random_sign_comp = random.randint(0,2)

if ask_user == 0 and random_sign_comp == 1:
    print(f"You Chose: \n {rock}")
    print(f"Computer Chose: \n{paper}")
    print("You Lose!")
elif ask_user == 0 and random_sign_comp == 2:
    print(f"You Chose: \n {rock}")
    print(f"Computer Chose: \n{scissors}")
    print("You Won!")

elif ask_user == 1 and random_sign_comp == 0:
    print(f"You Chose: \n {paper}")
    print(f"Computer Chose: \n{rock}")
    print("You Won!")

elif ask_user == 1 and random_sign_comp == 2:
    print(f"You Chose: \n {paper}")
    print(f"Computer Chose: \n{scissors}")
    print("You Lose!")

elif ask_user == 2 and random_sign_comp == 0:
    print(f"You Chose: \n {scissors}")
    print(f"Computer Chose: \n{rock}")
    print("You Lose!")
elif ask_user == 2 and random_sign_comp == 1:
    print(f"You Chose: \n {scissors}")
    print(f"Computer Chose: \n{paper}")
    print("You Won!")
else:
    print()
    print("It's Draw!")



