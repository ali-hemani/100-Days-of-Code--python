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

# Write your code below this line 👇
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print("\n"+choices[user_choice])
print("\nComputer chose:")
computer_choice = random.randint(0,2)
print("\n"+choices[computer_choice])
if user_choice == 0:
    if computer_choice == 0:
        print("\nTie!")
    elif computer_choice == 1:
        print("\nYou Lose!")
    else:
        print("\nYou Win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("\nYou Win!")
    elif computer_choice == 1:
        print("\nTie!")
    else:
        print("\nYou Lose!")
else:
    if computer_choice == 0:
        print("\nYou Lose!")
    elif computer_choice == 1:
        print("\nYou Win!")
    else:
        print("\nTie!")

