import sys
import numpy as np
from collections import deque
import datetime

def main(method): #here using method to decide which search method to invoke
    if method == "bfs":         #breadth first search
        bfs(start, goal, dflag)
    elif method == "ucs":       #uniform cost
        ucs(start, goal, dflag)
    elif method == "greedy":    #greedy search
        greedy(start, goal, dflag)
    elif method == "a*":        #A* search
        a_star(start, goal, dflag)
    else:
        a_star(start, goal, dflag)


def bfs(start, goal, flag): #bfs's fringe is a FIFO so i should try and implement a queue
    print("this is bfs")
    #for BFS i will start at whichever node is 0
    #cant use a for loop to search through array because i am using numpy
    nodes = []
    for i in range(9):
        index = np.where(start == i)
        for i, j in zip(index[0], index[1]):
            node = (i,j)
            nodes.append(node)
    for node in nodes: #finding each node's neighbors
        i,j = node
        print(f"neighbors of {start[node]}")
        if (i == 2 and j == 2) or (i == 2 and j > 0) or (j == 2 and i > 0):
            print(f"{start[i-1, j]}, ({i-1}, {j})")
            print(f"{start[i, j-1]}, ({i}, {j-1})")
            continue
        elif (i == 0 and j == 0) or (i == 0 and j < 2) or (j == 0 and i < 2):
            print(f"{start[i+1, j]}, ({i+1}, {j})")
            print(f"{start[i, j+1]}, ({i}, {j+1})")
            continue
        elif i == 1 and j == 1:
            print(f"{start[i-1, j]}, ({i-1}, {j})")
            print(f"{start[i, j-1]}, ({i}, {j-1})")
            print(f"{start[i+1, j]}, ({i+1}, {j})")
            print(f"{start[i, j+1]}, ({i}, {j+1})")
        elif i == 2 and j == 0:
            print(f"{start[i-1, j]}, ({i-1}, {j})")
            print(f"{start[i, j+1]}, ({i}, {j+1})")
        elif i == 0 and j == 2:
            print(f"{start[i+1, j]}, ({i+1}, {j})")
            print(f"{start[i, j-1]}, ({i}, {j-1})")
        
    """queue = deque([start_node])
    visited = set([start_node]) #i do not want repeated states
    print(queue)
    print(visited)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(visited)
            for adj in start[node]:
                if adj not in visited:
                    queue.append(adj)"""

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

    else:
        if len(sys.argv) == 4:                         #3 flags = no dump flag
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
        if dflag == "True":
            print("dflag true")
            cdatetime = datetime.datetime.now()
            dfilename = cdatetime.strftime("trace-%m_%d_%Y-%H_%M") + ".txt" 
            with open(dfilename, "w") as file:
                print("HELLO WORLD!", file=file)
        
        #making sure each element in the list is an int
        #turning the start & goal lists into matrices
        start = np.vectorize(int)(start)
        start = np.array(start)
        goal = np.vectorize(int)(start)
        goal = np.array(goal)

        main(method)
    