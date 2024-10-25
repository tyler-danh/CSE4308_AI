import sys
import math

#create dictionary for moves
standard_moves = {"Pick 2 Red" : 2, "Pick 2 Blue" : 2, "Pick 1 Red" : 1, "Pick 1 Blue" : 1}
standard_list =["Pick 2 Red", "Pick 2 Blue", "Pick 1 Red", "Pick 1 Blue"]
misere_moves = {"Pick 1 Blue" : 1, "Pick 1 Red" : 1, "Pick 2 Blue" : 2, "Pick 2 Red" : 2}
misere_list = ["Pick 1 Blue", "Pick 1 Red", "Pick 2 Blue", "Pick 2 Red"]

def play_game(red_num, blue_num, version, first_player):
    # print(f"red: {red_num}  blue: {blue_num}")
    print(f"First player: {first_player}")
    if first_player == "computer":
        human_player = False
    else:
        human_player = True
    marble_piles = [red_num, blue_num] #list to represent the 2 piles
    while True:
        if human_player == False:
            print("Computer Turn")
            if marble_piles[0] == 0 or marble_piles[1] == 0:
                if version == "standard":
                    if marble_piles[0] == 0:
                        score = marble_piles[1] * 3 #blue = 3 points
                        print(f"You win! (:\nRed pile empty\nScore: {score}")
                        return False
                    elif marble_piles[1] == 0:
                        score = marble_piles[0] * 2 #red = 2 points
                        print(f"You win! (:\nBlue pile empty\nScore: {score}")
                        return False
                if version == "misere":
                    if marble_piles[0] == 0:
                        score = marble_piles[1] * 3 #blue = 3 points
                        print(f"Computer wins ):\nRed pile empty\nScore: {score}")
                        return False
                    elif marble_piles[1] == 0:
                        score = marble_piles[0] * 2 #red = 2 points
                        print(f"Computer wins ):\nBlue pile empty\nScore: {score}")
                        return False
            action = alpha_beta(marble_piles, first_player, version)
            if marble_piles[0] - standard_moves[action] < 0 or marble_piles[1] - standard_moves[action] < 0:
                continue
            elif "Blue" in action:
                marble_piles[1] -= standard_moves[action]
            elif "Red" in action:
                marble_piles[0] -= standard_moves[action]
            print(f"Red Pile: {marble_piles[0]}      Blue Pile: {marble_piles[1]}")
            human_player = True

        elif human_player == True:
            print("Your Turn")
            human_player = True
            if version == "standard":
                print("Standard move list:")
                if marble_piles[0] == 0:
                    score = marble_piles[1] * -3 #blue = 3 points
                    print(f"Computer Wins ):\nRed pile empty\nScore: {score}")
                    return False
                elif marble_piles[1] == 0:
                    score = marble_piles[0] * -2 #red = 2 points
                    print(f"Computer wins ):\nBlue pile empty\nScore: {score}")
                    return False
                for i in range(4):
                    print(f"[{i+1}] {standard_list[i]}")
                move_selection = input("Enter the number corresponding to your move: ")
                move = standard_list[int(move_selection)-1]
                if (int(move_selection)-1) % 2 == 0: #in standard mode red pile is even, blue pile is odd
                    if marble_piles[0] - standard_moves[move] < 0:
                        print(f"Invalid Move\nThere is only {marble_piles[0]} red left.")
                        continue
                    marble_piles[0] -= standard_moves[move]
                else:
                    if marble_piles[1] - standard_moves[move] < 0:
                        print(f"Invalid Move\nThere is only {marble_piles[1]} blue left.")
                        continue
                    marble_piles[1] -= standard_moves[move]
            elif version == "misere":
                print("Misere move list:")
                if marble_piles[0] == 0:
                    score = marble_piles[1] * 3 #blue = 3 points
                    print(f"You win! (:\nred pile empty\nscore: {score}")
                    return False
                elif marble_piles[1] == 0:
                    score = marble_piles[0] * 2 #red = 2 points
                    print(f"You win! (:\nblue pile empty\nscore: {score}")
                    return False
                for i in range(4):
                    print(f"[{i+1}] {misere_list[i]}")
                move_selection = input("Enter the number corresponding to your move: ")
                move = misere_list[int(move_selection)-1]
                if (int(move_selection)-1) % 2 == 0: #in misere mode blue pile is even, red pile is odd
                    if marble_piles[1] - misere_moves[move] < 0:
                        print(f"Invalid Move\nThere is only {marble_piles[1]} blue left.")
                        continue
                    marble_piles[1] -= misere_moves[move]
                    print(marble_piles)
                else:
                    if marble_piles[1] - misere_moves[move] < 0:
                        print(f"Invalid Move\nThere is only {marble_piles[0]} red left.")
                        continue
                    marble_piles[0] -= misere_moves[move]
                    print(marble_piles)
            print(f"Red Pile: {marble_piles[0]}      Blue Pile: {marble_piles[1]}")
            human_player = False
                


def alpha_beta(marble_pile, first_player, mode): #marble_pile is state
    utility, action = min_value(marble_pile, -math.inf, math.inf, mode)
    print(f"Selected {action}, with utility: {utility}")    
    return action #return the action to take? or the entire tree

def max_value(state, alpha, beta, mode):
    if state[0] == 0:
        return state[1] * 3, None
    elif state[1] == 0:
        return state[0] * 2, None
    v = -math.inf
    best_action = None
    for action, states in generate_successors(state, mode):
        utility, _ = min_value(states, alpha, beta, mode)
        if utility > v:
            v = utility
            best_action = action
        if v >= beta:
            return v, best_action
        alpha = max(alpha, v)
    return v, best_action

def min_value(state, alpha, beta, mode):
    if state[0] == 0:
        return state[1] * 3, None
    elif state[1] == 0:
        return state[0] * 2, None
    v = math.inf
    best_action = None
    for action, states in generate_successors(state, mode):
        utility, _ = max_value(states, alpha, beta, mode)
        if utility < v:
            v = utility
            best_action = action
        if v <= alpha:
            return v, best_action
        beta = min(beta, v)
    return v, best_action

def generate_successors(state, mode):
    red, blue = state
    red_blue = ()
    successsors = [] #[ action, (red, blue) ]
    if mode == "standard":
        while red > 0 and blue > 0:
            #print("successor while loop")
            if red < 0 or blue < 0:
                continue
            for i in range(4):
                move = standard_list[i]
                if i %2 == 0:
                    if red - standard_moves[move] < 0:
                        continue
                    else: 
                        red -= standard_moves[move]
                        red_blue = (red,blue)
                        successor_tuple = (move, red_blue)
                        successsors.append(successor_tuple)
                        if red == 0:
                            break
                else:
                    if blue - standard_moves[move] < 0:
                        continue
                    else: 
                        blue -= standard_moves[move]
                        red_blue = (red,blue)    
                        successor_tuple = (move, red_blue)
                        successsors.append(successor_tuple)
                        if blue == 0:
                            break
    if mode == "misere":
        while red != 0 or blue != 0:
            if red < 0 or blue < 0: 
                continue
            for i in range(4):
                move = misere_list[i]
                if i %2 == 0:
                    if red - misere_moves[move] < 0:
                        continue
                    else:
                        red -= misere_moves[move]
                        red_blue = (red,blue) 
                        successor_tuple = (move, red_blue)
                        successsors.append(successor_tuple)
                        if red == 0:
                            break
                else:
                    if blue - misere_moves[move] < 0:
                        continue
                    else:
                        blue -= misere_moves[move] 
                        red_blue = (red,blue)   
                        successor_tuple = (move, red_blue)
                        successsors.append(successor_tuple)
                        if blue == 0:
                            break
    return successsors

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: red_blue_nim.py <num-red> <num-blue> <version> <first-player>")
    else:
        play_game(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])   