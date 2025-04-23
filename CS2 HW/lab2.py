# Sean Reynolds
# Program that plays a guess the number game with the user
import random

## function determines bounds, rejects if less than 1 or greater than 500 and returns the values
def getRange():
    while True:
        lower_bound = int(input("Set the lower bound: "))
        upper_bound = int(input("Set the upper bound: "))
        if lower_bound < 1:
            print("Enter a value of 1 or greater")
        elif upper_bound > 500:
            print("Enter a value less than 500")
        elif lower_bound >= upper_bound:
            print("Lower bound cannot be greater than or equal to upper bound")
        else:
            return lower_bound, upper_bound
   
## takes parameters and asks user to guess a number inbetween them. Prevents guesses from being larger than 500
## or less than 1. Returns user_gues
def getGuess(low, high):
    while True:
        user_guess = int(input(f"Guess a number between {low} and {high}, inclusive: "))
        if user_guess > 500 or user_guess < 1:
            print("Stay within the number range")
        else:
            return user_guess

## takes random number inbetween parameters low and high. Tries counter increases when a guess is incorrect.
## Breaks when the correct number is guessed
def playOneGame(low, high):
    ran_num = random.randint(low, high)
    tries = 0
    while True:
        guess = getGuess(low, high)
        tries += 1
        if guess == ran_num:
            print(f"Correct! Number of tries: {tries}")
            break
        elif guess < ran_num:
            print("Guess higher")
        elif guess > ran_num:
            print("Guess lower")

def main():
    while True:
        play_game = input("Do you want to play the game? y/n: ").lower()
        if play_game != "y":
            print("Thanks for playing")
            break
        low, high = getRange()

        playOneGame(low, high)
        print("\n" + "-" * 30 + "\n")

        
main()