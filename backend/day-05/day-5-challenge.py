from difflib import get_close_matches
import random

options = {
    "scissor": {
        "wins to": "paper",
        "losses to": "rock",
    },
    "rock": {
        "wins to": "scissor",
        "losses to": "paper"
    },
    "paper": {
        "wins to": "rock",
        "losses to": "scissor"
    }
}

def validate_input(player_input):
    valid_choices = options.keys()
    closest_match = get_close_matches(player_input, valid_choices, n=1, cutoff=0.6)

    if closest_match:
        return closest_match[0]
    else:
        print("INVALID INPUT")
        exit()

def evaluate(player, computer):
    if options[player]["wins to"] == computer:
        print("You win!")
    elif options[player]["losses to"] == computer:
        print("Computer wins!")
    elif player == computer:
        print("It's a draw!")

def start_game():
    player_1 = validate_input(input("Player 1: ").lower())
    computer_choice = random.choice(list(options.keys()));
    print(f"Computer: {computer_choice}")

    evaluate(player_1, computer_choice)

start_game();