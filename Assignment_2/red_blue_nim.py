import sys
import math

#create dictionary for moves
standard_moves = {"Pick 2 Red" : 2, "Pick 2 Blue" : 2, "Pick 1 Red" : 1, "Pick 1 Blue" : 1}
standard_list =["Pick 2 Red", "Pick 2 Blue", "Pick 1 Red", "Pick 1 Blue"]
misere_moves = {"Pick 1 Blue" : 1, "Pick 1 Red" : 1, "Pick 2 Blue" : 2, "Pick 2 Red" : 2}
misere_list = ["Pick 1 Blue", "Pick 1 Red", "Pick 2 Blue", "Pick 2 Red"]

def play_game(red_num, blue_num, version, first_player):
    print(f"red: {red_num}  blue: {blue_num}")
    while True:
        if first_player == "computer":
            print("Computer goes first")
            #we do the alpha/beta pruning here then we take human moves
        else:
            print("Human goes first")
            if version == "standard":
                print("Standard move list:")
                for i in range(4):
                    print(f"[{i+1}] {standard_list[i]}")
                move_selection = input("Enter the number corresponding to your move: ")
                move = standard_list[int(move_selection)-1]
                print(standard_moves[move])
                if (int(move_selection)-1) % 2 == 0: #in standard mode red pile is even, blue pile is odd
                    red_num -= int(standard_moves[move])
                    print(red_num)
                else:
                    blue_num -= int(standard_moves[move])
                    print(blue_num)

            elif version == "misere":
                print("Misere move list:")
                for i in range(4):
                    print(f"[{i+1}] {misere_list[i]}")
                move_selection = input("Enter the number corresponding to your move: ")
                move = misere_list[int(move_selection)-1]
                print(misere_moves[move])
                if (int(move_selection)-1) % 2 == 0: #in misere mode blue pile is even, red pile is odd
                    blue_num -= misere_moves[move]
                    print(blue_num)
                else:
                    red_num -= misere_moves[move]
                    print(red_num)


        
        

def alpha_beta():
    alpha = -math.inf
    beta = math.inf
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: red_blue_nim.py <num-red> <num-blue> <version> <first-player>")
    else:
        play_game(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])   