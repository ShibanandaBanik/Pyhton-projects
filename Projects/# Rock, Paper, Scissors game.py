# Rock, Paper, Scissors game
import random

game_choices = ("Rock","Paper","Scissors")

CPU_choice = random.choice(game_choices)

while True:
    print("Welcome to Rock, Paper, Scissors game")
    
    if CPU_choice == "Rock":
        print("")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player_input = int(input("Enter Your choice: "))
        if player_input == 1 and CPU_choice:
            print("It's a Draw.")
        elif player_input == 2 and CPU_choice:
            print("You Win.")
        elif player_input == 3 and CPU_choice:
            print("You Lose.")
        else:
            print("Try again")

    elif CPU_choice == "Paper":
        print("")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player_input = int(input("Enter Your choice: "))
        if player_input == 1 and CPU_choice:
            print("You Lose.")
        elif player_input == 2 and CPU_choice:
            print("It's a Draw.")
        elif player_input == 3 and CPU_choice:
            print("You Win.")
        else:
            print("Try again")
    
    elif CPU_choice == "Scissors":
        print("")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player_input = int(input("Enter Your choice: "))
        if player_input == 1 and CPU_choice:
            print("You Win.")
        elif player_input == 2 and CPU_choice:
            print("You Lose.")
        elif player_input == 3 and CPU_choice:
            print("It's a Draw.")
        else:
            print("Try again")
    
    elif player_input == 0:
        break