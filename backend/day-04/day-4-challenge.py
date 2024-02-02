from difflib import get_close_matches

options = {
    "scissor": {
        "wins to": "scissor",
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

def evaluate(p1, p2):
    if options[p1]["wins to"] == p2:
        print("Player 1 wins!")
    elif options[p1]["losses to"] == p2:
        print("Player 2 wins!")
    elif p1 == p2:
        print("It's a draw!")

player_1 = validate_input(input("Player 1: ").lower())
player_2 = validate_input(input("Player 2: ").lower())

evaluate(player_1, player_2)