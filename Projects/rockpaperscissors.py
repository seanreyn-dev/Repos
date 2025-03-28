# Rock Paper Scissors Game

#psuedo code
#1. Create a list of options for the user to choose from
#3. Create a while loop to keep the user choosing until they choose a valid option
#4. Create a variable to store the computer's choice
#5. Print the user's choice and the computer's choice
#6. Compare the user's choice to the computer's choice
#7. Ask the user if they want to play again
#8. If they say no, break the loop

import random
def main():
    while True:
        options = ["Rock", "Paper", "Scissors"]
        
        while True:
            user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
            if user_choice not in options:
                print("Please choose Rock, Paper, or Scissors")
            else:
                break

        comp_choice = random.choice(options)

        print(f"You chose: {user_choice}, Cpu chose: {comp_choice}")

        if user_choice == comp_choice:
            print(f"You both chose {user_choice}, there's a tie!")
        elif user_choice == "Rock":
            if comp_choice == "Paper":
                print("Cpu chose Paper, you lose!")
            else:
                print("Cpu chose Scissors, you win!")
        elif user_choice == "Paper":
            if comp_choice == "Rock":
                print("Cpu chose Rock, you win!")
            else:
                print("Cpu chose Scissors, you lose!")
        elif user_choice == "Scissors":
            if comp_choice == "Paper":
                print("Cpu chose Paper, you win!")
            else:
                print("Cpu chose Rock, you lose!")

        repeat_game = input("Would you like to play? Yes/No: ")
        if repeat_game.lower() != "yes":
            break

main()


import random

def main():
    while True:
        options = ["Rock", "Paper", "Scissors"]
        
        comp_choice = get_computer_choice()
        
        while True:
            user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
            if user_choice not in options:
                print("Please choose Rock, Paper, or Scissors")
            else:
                break

        print(f"You chose: {user_choice}, Cpu chose: {comp_choice}")

        result = determine_winner(user_choice, comp_choice)
        print(result)

        if "tie" in result.lower():
            continue 

        repeat_game = input("Would you like to play? Yes/No: ")
        if repeat_game.lower() != "yes":
            break

def get_computer_choice():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices[random.randint(1, 3)]

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie! Play again to determine a winner."
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

main()
