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
import random

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))

if user_choice >= 3 or user_choice < 0:
    print("This is not valid number!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[computer_choice])


    if user_choice == computer_choice:
        print("It's draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) \
         or (user_choice == 1 and computer_choice == 0):
        print("You win!")
    else:
        print("Computer wins!")

 
   

