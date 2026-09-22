### python by moshiurr007 --> beginner_level ###

# number guessing game #

import random

def game_on():
    the_number = random.randint(1, 100)
    total_attempt = 0
    player_choice = None

    while player_choice != the_number:
        try:
            player_choice = int(input("Guess the integer number between 1 and 100: "))
        except ValueError:
            print("Wrong input type. Enter an integer number.")
            continue

        if player_choice < 1 or player_choice > 100:
            print("Out of range.")
        else:
            total_attempt += 1
            if player_choice > the_number:
                print(f"The number is less than {player_choice}")
            elif player_choice < the_number:
                print(f"The number is greater than {player_choice}")
        
    return f"You have guessed the number {the_number} correctly in {total_attempt} attempts."

print(game_on())