import sys

def standard_game(red_num, blue_num, first_player):
    print(f"red: {red_num}  blue: {blue_num}")
    if first_player == "computer":
        print("Computer goes first")
    else:
        print("Human goes first")
        marbles = input("Enter # of marbles to take from 1-2: ")
        print(f"{marbles}")

def misere_game(red_num, blue_num, first_player):
    print(f"red: {red_num}  blue: {blue_num}")
    if first_player == "computer":
        print("Computer goes first")
    else:
        print("Human goes first")
        marbles = input("Enter # of marbles to take from 1-2: ")
        print(f"{marbles}")

def alpha_beta():
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: red_blue_nim.py <num-red> <num-blue> <version> <first-player>")
    else:
        if sys.argv[3] == "standard":
            print("standard")
            standard_game(sys.argv[1], sys.argv[2], sys.argv[4])
        elif sys.argv[3] == "misere":
            print("misere")    