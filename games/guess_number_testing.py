# guess number

import random

print("I'm thinking of number between 1 and 50.")
number = random.randint(1, 50)
print(number)

def diff_easy():
    attempts = 5
    game_over = False
    while not game_over:
        guess = int(input("Guess the number: "))
        if attempts == 1:
            print("Game over!")
            game_over = True
        elif guess == number:
            print("You guessed the number. You win!!")
            game_over = True
        elif guess < number:
            attempts -= 1
            print(f"Too low. You have only {attempts} attempts.")
        else:
            attempts -= 1
            print("Too high. You have only {attempts} attempts.")
        
def diff_hard():
    attempts = 3
    game_over = False
    while not game_over:
        guess = int(input("Guess the number: "))
        if attempts == 1:
            print("Game over!")
            game_over = True
        elif guess == number:
            print("You guessed the number. You win!!")
            game_over = True
        elif guess < number:
            attempts -= 1
            print(f"Too low. You have only {attempts} attempts.")
        else:
            attempts -= 1
            print(f"Too high. You have only {attempts} attempts.")
        

play_game = True
while play_game:
    choose_game = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if choose_game == 'easy':
        diff_easy()
    else:
        diff_hard()
            
    play_again = input("Do you want to play again? y/n").lower()
    if play_again == 'y':
        play_game = True
    else:
        print("Thank you")
        play_game = False
        
        
    