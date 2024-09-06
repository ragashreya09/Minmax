RAGA SHREYA MEKALA
1002156846

The provided code is written in Python3. 

Structure of code:

calculate_score: 
●	Counting Marbles: The function starts by unpacking the state tuple into two variables, red_count and blue_count, which represent the number of red and blue marbles (or points) accordingly.

●	Calculating Difference: It calculates the score_difference by subtracting the number of blue marbles from the number of red marbles. The result is a positive number if there are more red marbles, negative if there are more blue marbles, and zero if both are equal.

●	Rule Consideration: If the game_rule is set to "misere" (a version of the game where the objective is typically to force the opponent to take the last marble or to lose), the function reverses the sign of score_difference. This adjustment implies that in "misere", the game prioritizes states where the player has fewer marbles compared to the opponent (a situation usually considered disadvantageous in standard rules).

●	Result: The function returns the score_difference, which serves as the heuristic evaluation of the current game state. In the context of game strategy, this score helps the AI determine the most favorable moves by prioritizing states with a higher score under the current rules. This method provides a strategic advantage, guiding the AI's choices during the minimax decision-making process.

request_player_move: Handles user input for choosing moves.

initiate_game: Controls the game flow, alternating turns between the player and computer, and checks for the end of the game.


execute_game: Serves as the main function to start the game, parse command-line arguments, and initialize game settings.

Main Block: The script's execution begins here if it's run as the main program. It calls the execute_game function, setting the game in motion.

python3 red_blue_nim.py [red_count] [blue_count] [game_rule] [initial_player] [search_depth]




