#Create a simple number guessing game.
#- The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
import random
def guessing_game():
    x=random.randint(1,100)
    n=10
    for i in range(n):
        y=int(input("Enter your guess: "))
        if y==x:
           print("Your guess is correct!") 
           return   
        elif y>x:
            print(f"Too high.\n You have {10-i-1} try.")
        elif y<x:
            print(f"Too low.\n You have {10-i-1} try. ")
    print("You lost. Want to play again? ")
while True:
    guessing_game()            
    q=str(input("Want to play again? "))
    quit=['Y', 'YES', 'y', 'yes', 'ok']
    quit1=['N', 'No', 'n', 'no', 'not','NOT']
    if q in quit1:
        print("Goodbye!")
        break
    
    