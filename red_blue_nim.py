import sys

def perform_minimax(state, search_depth, alpha_value, beta_value, is_maximizing_player, game_rule):
    red_count, blue_count = state

    if red_count == 0 or blue_count == 0:
        base_score = 2 * red_count + 3 * blue_count
        return (base_score if game_rule == "standard" else -base_score) * (-1 if is_maximizing_player else 1)

    if search_depth == 0:
        return calculate_score(state, game_rule)

    optimal_score = float('-inf') if is_maximizing_player else float('inf')

    possible_moves = [(0, 1), (1, 0)] if game_rule == "standard" else [(1, 0), (0, 1)]

    for current_move in possible_moves:
        new_state = (red_count - current_move[0], blue_count - current_move[1])
        if new_state[0] >= 0 and new_state[1] >= 0:  # Valid move
            current_score = perform_minimax(new_state, search_depth - 1, alpha_value, beta_value, not is_maximizing_player, game_rule)
            optimal_score = max(current_score, optimal_score) if is_maximizing_player else min(current_score, optimal_score)
            alpha_value = max(alpha_value, optimal_score) if is_maximizing_player else alpha_value
            if beta_value <= alpha_value:
                break

    return optimal_score

def calculate_score(state, game_rule):
    red_count, blue_count = state
    score_difference = red_count - blue_count

    if game_rule == "misere":
        score_difference = -score_difference

    return score_difference

def request_player_move(state):
    while True:
        selected_pile = input("Choose a pile to remove from (red/blue): ").strip().lower()
        if selected_pile in ["red", "blue"] and state[0 if selected_pile == "red" else 1] > 0:
            return (1, 0) if selected_pile == "red" else (0, 1)
        print("Invalid move. Please choose a non-empty pile.")

def initiate_game(red_count, blue_count, game_rule, initial_player, search_depth):
    game_state = (red_count, blue_count)
    current_turn = initial_player

    while game_state[0] > 0 and game_state[1] > 0:
        print(f"Current state: Red - {game_state[0]}, Blue - {game_state[1]}")

        if current_turn == "computer":
            highest_score = float('-inf')
            optimal_move = None

            possible_moves = [(0, 1), (1, 0)] if game_rule == "standard" else [(1, 0), (0, 1)]

            for current_move in possible_moves:
                updated_state = (game_state[0] - current_move[0], game_state[1] - current_move[1])
                if updated_state[0] >= 0 and updated_state[1] >= 0:  # Valid move
                    evaluation_score = perform_minimax(updated_state, search_depth, float('-inf'), float('inf'), False, game_rule)
                    if evaluation_score > highest_score:
                        highest_score = evaluation_score
                        optimal_move = current_move

            game_state = (game_state[0] - optimal_move[0], game_state[1] - optimal_move[1])
            pile_name = "Red" if optimal_move == (1, 0) else "Blue"
            print(f"Computer takes from {pile_name} pile.")
        else:
            player_move = request_player_move(game_state)
            game_state = (game_state[0] - player_move[0], game_state[1] - player_move[1])

        current_turn = "human" if current_turn == "computer" else "computer"

    final_score = 2 * game_state[0] + 3 * game_state[1]
    if game_rule == "misere":
        final_score *= -1
        victor = "Computer" if current_turn == "human" else "Human"
    else:
        victor = "Human" if current_turn == "human" else "Computer"

    print(f"Game over. {victor} wins with a score of {final_score}.")

def execute_game():
    command_arguments = sys.argv[1:]

    rule_variant = "standard"
    starting_player = "computer"
    max_search_depth = float('inf')

    red_pile_count = int(command_arguments[0])
    blue_pile_count = int(command_arguments[1])

    if len(command_arguments) >= 3:
        rule_variant = command_arguments[2]
    if len(command_arguments) >= 4:
        starting_player = command_arguments[3]
    if len(command_arguments) >= 5:
        max_search_depth = int(command_arguments[4])

    initiate_game(red_pile_count, blue_pile_count, rule_variant, starting_player, max_search_depth)

if __name__ == "__main__":
    execute_game()
