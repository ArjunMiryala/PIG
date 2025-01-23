import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:                                        
    players =input("Enter the number of players (2 - 4): ")
    if players.isdigit():        # .isdigit is going to tell us its a digit(valid whole number) or not
        players = int(players)      # then after checking if digit or not we can convert that into int
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
        
max_score = 50
player_scores = [0 for _ in range(players)]  # using _ becuase we dont care about what variable there is # range function is for looping number of players we have

while max(player_scores) < max_score:           # max(player_scores) will give maximum value of the array pplayer_scores
    
    for player_index in range(players):                     #using range we can go from index 1 to end and the value of player_index changes every for loop.(Interation)
        print("\nPlayer", player_index +1, "turn has jsut started!")
        print("Your total score is:", player_scores[player_index], "\n")
        current_score = 0
        
        
        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break                
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            

            print("Your Score is:", current_score)
        
        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])



max_score = max(player_scores)
winnning_index = player_scores.index(max_score)
print("Player number", winnning_index + 1, "is the winner with a score of:", max_score)