import random

def dice():
    min_val = 1
    max_val = 6
    val = random.randint(min_val, max_val)

    return val


while True:
    no_of_players = input('Enter no of players (2 - 4): ')
    if no_of_players.isdigit():
        no_of_players = int(no_of_players)
        if 2 <= no_of_players <= 4:
            break
        else:
            print('Invalid must be (2 - 4) try again!')
    else:
        print('Must be a Num, try again!')


max_score = 50
players_scores = [0 for i in range(no_of_players)]

while max(players_scores) < max_score:

    for player_idx in range(no_of_players):
        print("\nPlayer", player_idx + 1, "has just started!")
        print("Your total score is", players_scores[player_idx], "\n")

        current_score = 0

        while True:
            should_roll = input('Would you like to roll the dice (y)? ')
            if should_roll.lower() != 'y':
                break

            value = dice()
            if value == 1:
                print('You rolled 1! Your Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
                

            print('Your current turn score is:', current_score)

        players_scores[player_idx] += current_score
        print('Player no', player_idx + 1, 'total score is:', players_scores[player_idx])


max_players_score = max(players_scores)
winning_idx = players_scores.index(max_players_score)

print("\nPlayer number", winning_idx + 1, "is the winner with a score of:", max_players_score)