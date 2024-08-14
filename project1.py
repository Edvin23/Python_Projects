#importing random number generator 
import random

# defines the function roll 
def roll():
    min_value = 1
    max_value = 6
    #random number between the min and max value
    roll = random.randint(min_value, max_value)
    #returns the random number
    return roll
#While loop to ask how many players will play 
while True:
     players = input("Enter the numbers of players (2-4): ")
     if players.isdigit():
         players = int(players)
         #only 2 and 4 players can play 
         if 2 <= players <= 4:
             break
         else: 
             print("Must be between 2-4 players.")
     else:
         print("Invalid, try again.")

#The max number to win is 50   
max_scores = 50
#Shows the score for each player 
player_scores = [0 for _ in range(players)]

#while loop to check the score for players and the max score
while max(player_scores) < max_scores:
      for player_idx in range(players):#player idx is which player is playing 
        print("\nPlayer number", player_idx + 1, "turn has just started!\n") #
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0


        while True: #while loop to ask if they want to roll or not 
           should_roll = input("Would you like to roll (y)?")
           if should_roll.lower() != "y":
              break
      
           value = roll() # if you roll a 1 then game over 
           if value == 1:
               print("You rolled a 1! Turn Done!")
               current_score = 0
               break
           else:
            current_score += value
            print("You rolled a: ", value)
            print("Your score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])


max_scores = max(player_scores)
winning_idx = player_scores.index(max_scores)
print ("Player Number", winning_idx + 1,
       "is the winner with a score of: ", max_scores)
                    
        
      