import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return
        
        attempts -= 1
    
    print("You lost. Want to play again? (yes/Y/ok)")
    again = input().lower()
    if again in ['y', 'yes', 'ok']:
        play_game()

play_game()
