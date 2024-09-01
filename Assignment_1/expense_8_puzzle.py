import sys
import numpy as np

def main(method): #here using method to decide which search method to invoke
    if method == "bfs":
        bfs(start, goal, dflag)
    elif method == "ucs":
        ucs(start, goal, dflag)
    elif method == "greedy":
        greedy(start, goal, dflag)
    elif method == "a*":
        a_star(start, goal, dflag)
    else:
        a_star(start, goal, dflag)


def bfs(start, goal, flag):
    print("this is bfs")
    if np.array_equal(start, goal):
        return 0
    
def ucs(start, goal, flag):
    print("this is ucs")
    if np.array_equal(start, goal):
        return 0

def greedy(start, goal, flag):
    print("this is greedy")
    if np.array_equal(start, goal):
        return 0

def a_star(start, goal, flag):
    print("this is a_star")
    if np.array_equal(start, goal):
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 4 and len(sys.argv) != 5 and len(sys.argv) != 3:
        print("Usage: expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>")
    elif len(sys.argv) == 4:                         #3 flags = no dump flag
        start_file = sys.argv[1]
        goal_file = sys.argv[2]
        method = sys.argv[3]
        dflag = False
    elif len(sys.argv) == 5:                         #4 flags = dump flag
        start_file = sys.argv[1]
        goal_file = sys.argv[2]
        method = sys.argv[3]
        dflag = sys.argv[len(sys.argv)-1]
    elif len(sys.argv) == 3:
        start_file = sys.argv[1]
        goal_file = sys.argv[2]
        method = "a*"
        dflag = False
    
    with open(start_file, 'r') as file:
        start = file.readlines()
        start = [start.split() for start in start]  #splitting start contents by each character instead of each line
    with open(goal_file, 'r') as file:
         goal = file.readlines()
         goal = [goal.split() for goal in goal]     #splitting goal contents by each character instead of each line
    
    #turning the start & goal lists into matrices
    start = np.matrix(start)
    goal = np.matrix(goal)

    main(method)
    