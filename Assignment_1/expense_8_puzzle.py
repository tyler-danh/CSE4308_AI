import sys
import numpy as np
from collections import deque
import heapq
import datetime
import copy
from Node import node

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
    #for BFS i will start at whichever node is in [0,0]
    #cant use a for loop to search through matrix because i am using numpy
    queue = deque([node(start, 0, start[0,0], 0)]) #queue is our fringe here but will still use fringe for dump file purposes
    visited = set()
    popped = 0
    expanded = 0 
    depth = 0
    lcounter = 0
    fringe = [] 
    state_step = {} #map each state to its step performed for path reconstruction
    visited.add(tuple(start.flatten()))
    while queue:
        successor_counter = 0
        lcounter += 1
        print(f"\rLoop: {lcounter}", end='')
        current_node = queue.popleft()
        depth += 1
        popped += 1
        if np.array_equal(current_node.state, goal):
            path = path_reconstruction(current_node, state_step)
            if dflag == True:
                with open(dfilename, "a") as file:
                    print(f"Goal found: state = {current_node.state}", file=file)
                    print(f"Nodes popped: {popped}", file=file)
                    print(f"Nodes expanded: {expanded}", file=file)
                    print(f"Max fringe size: {qsize}", file=file)
                    print(f"Solution found at depth {depth} with cost {current_node.cost}", file=file)
                    print(f"# of steps: {len(path)}", file=file)
            print(f"\nGOAL FOUND: state = {current_node.state}")
            print(f"Nodes popped: {popped}")
            print(f"Nodes expanded: {expanded}")
            print(f"Max fringe size: {qsize}")
            print(f"Solution found at depth {depth} with cost {current_node.cost}")
            for i in range(len(path)):
                print(f"\t{path[i]}")
            return 0
        for x,y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #down, up, left, right, this should expand more states(nodes)
            for i in range(9):
                index = np.where(current_node.state == 0)
                for i, j in zip(index[0], index[1]):
                    blank = (i,j)
            new_x = blank[0] + x
            new_y = blank[1] + y
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                successor_counter += 1
                expanded += 1
                new_state = copy.deepcopy(current_node.state)
                new_state[blank[0]][blank[1]] = new_state[new_x][new_y]
                Node_cost = new_state[new_x][new_y]         #because im using a copy of current_node i have to first save the cost then append it
                new_cost = current_node.cost + Node_cost    #cost does not matter in BFS
                new_state[new_x][new_y] = 0                 #moving the blank
                new_node = node(copy.deepcopy(new_state), current_node, new_cost, 0)
                
                if tuple(new_state.flatten()) not in visited:
                    qsize = len(queue)
                    visited.add(tuple(new_state.flatten()))
                    queue.append(new_node)
                    fringe.append(copy.deepcopy(new_node.state))
                    if x == -1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} down"
                    elif x == 1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} up"
                    elif y == -1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} right"
                    elif y == 1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} left"
        if dflag == True:
            with open(dfilename, "a") as file:
                print(f"{successor_counter} successors generated", file=file)
                print(f"Closed: {visited}", file=file) 
                print(f"Fringe: {fringe}", file=file)
    print("\nNO SOLUTION FOUND")
    print(f"Nodes popped: {popped}")
    print(f"Nodes expanded: {expanded}")
    print(f"Max fringe size: {qsize}")
    if dflag == True:
        with open(dfilename, "a") as file:
            print("NO SOLUTION FOUND", file=file)
            print(f"Nodes popped: {popped}", file=file)
            print(f"Nodes expanded: {expanded}", file=file)
            print(f"Max fringe size: {qsize}", file=file)
    return 1
    
def ucs(start, goal, flag):
    print("this is ucs")
    #for UCS i will start at whichever node is in [0,0]
    #cant use a for loop to search through matrix because i am using numpy
    queue = deque([node(start, 0, start[0,0], 0)]) #queue is our fringe here but will still use fringe for dump file purposes
    visited = set()
    popped = 0
    expanded = 0 
    depth = 0
    lcounter = 0
    fringe = [] 
    state_step = {} #map each state to its step performed for path reconstruction
    visited.add(tuple(start.flatten()))
    while queue:
        successor_counter = 0
        lcounter += 1
        print(f"\rLoop: {lcounter}", end='')
        current_node = queue.popleft()
        depth += 1
        popped += 1
        if np.array_equal(current_node.state, goal):
            path = path_reconstruction(current_node, state_step)
            if dflag == True:
                with open(dfilename, "a") as file:
                    print(f"Goal found: state = {current_node.state}", file=file)
                    print(f"Nodes popped: {popped}", file=file)
                    print(f"Nodes expanded: {expanded}", file=file)
                    print(f"Max fringe size: {qsize}", file=file)
                    print(f"Solution found at depth {depth} with cost {current_node.cost}", file=file)
                    print(f"# of steps: {len(path)}", file=file)
            print(f"\nGOAL FOUND: state = {current_node.state}")
            print(f"Nodes popped: {popped}")
            print(f"Nodes expanded: {expanded}")
            print(f"Max fringe size: {qsize}")
            print(f"Solution found at depth {depth} with cost {current_node.cost}")
            for i in range(len(path)):
                print(f"\t{path[i]}")
            return 0
        for x,y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #down, up, left, right, this should expand more states(nodes)
            for i in range(9):
                index = np.where(current_node.state == 0)
                for i, j in zip(index[0], index[1]):
                    blank = (i,j)
            new_x = blank[0] + x
            new_y = blank[1] + y
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                successor_counter += 1
                expanded += 1
                new_state = copy.deepcopy(current_node.state)
                new_state[blank[0]][blank[1]] = new_state[new_x][new_y]
                Node_cost = new_state[new_x][new_y]         #because im using a copy of current_node i have to first save the cost then append it
                new_cost = current_node.cost + Node_cost    #cost does not matter in BFS
                new_state[new_x][new_y] = 0                 #moving the blank
                new_node = node(copy.deepcopy(new_state), current_node, new_cost, 0)
                
                if tuple(new_state.flatten()) not in visited:
                    qsize = len(queue)
                    visited.add(tuple(new_state.flatten()))
                    queue.append(new_node)
                    fringe.append(copy.deepcopy(new_node.state))
                    if x == -1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} down"
                    elif x == 1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} up"
                    elif y == -1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} right"
                    elif y == 1:
                        state_step[tuple(new_state.flatten())] = f"move {new_state[blank[0]][blank[1]]} left"
        if dflag == True:
            with open(dfilename, "a") as file:
                print(f"{successor_counter} successors generated", file=file)
                print(f"Closed: {visited}", file=file) 
                print(f"Fringe: {fringe}", file=file)
    print("\nNO SOLUTION FOUND")
    print(f"Nodes popped: {popped}")
    print(f"Nodes expanded: {expanded}")
    print(f"Max fringe size: {qsize}")
    if dflag == True:
        with open(dfilename, "a") as file:
            print("NO SOLUTION FOUND", file=file)
            print(f"Nodes popped: {popped}", file=file)
            print(f"Nodes expanded: {expanded}", file=file)
            print(f"Max fringe size: {qsize}", file=file)
    return 1

def greedy(start, goal, flag):
    print("this is greedy")
    if dflag == True:
        file = open(dfilename, 'a')
    #cant use a for loop to search through matrix because i am using numpy
    visited = set()
    popped = 0
    expanded = 0 
    depth = 0
    fringe = [] 
    steps = []
    while queue:
        current_node = queue.popleft()
        depth += 1
        popped += 1
        if np.array_equal(current_node.state, goal):
            if dflag == True:
                print(f"Goal found: state = {current_node.state}", file=file)
                print(f"Nodes popped: {popped}", file=file)
                print(f"Nodes expanded: {expanded}", file=file)
                print(f"Max fringe size: {len(fringe)}", file=file)
                print(f"Goal found: state = {current_node.state}", file=file)
                print(f"Nodes popped: {popped}", file=file)
                print(f"Nodes expanded: {expanded}", file=file)
                print(f"Max fringe size: {len(fringe)}", file=file)
                print(f"Solution found at depth {depth} with cost {current_node.cost}", file=file)
                file.close()
            print(f"Goal found: state = {current_node.state}")
            print(f"Nodes popped: {popped}")
            print(f"Nodes expanded: {expanded}")
            print(f"Max fringe size: {len(fringe)}")
            print(f"Solution found at depth {depth} with cost {current_node.cost}")
            for i in range(len(steps)):
                print(f"\t{steps[i]}")
            return 0
    if np.array_equal(start, goal):
        return 0

def a_star(start, goal, flag):
    print("this is a_star")
    if dflag == True:
        file = open(dfilename, 'a')
    #cant use a for loop to search through matrix because i am using numpy
    visited = set()
    popped = 0
    expanded = 0 
    depth = 0
    fringe = [] 
    steps = []
    while queue:
        current_node = queue.popleft()
        depth += 1
        popped += 1
        if np.array_equal(current_node.state, goal):
            if dflag == True:
                print(f"Goal found: state = {current_node.state}", file=file)
                print(f"Nodes popped: {popped}", file=file)
                print(f"Nodes expanded: {expanded}", file=file)
                print(f"Max fringe size: {len(fringe)}", file=file)
                print(f"Goal found: state = {current_node.state}", file=file)
                print(f"Nodes popped: {popped}", file=file)
                print(f"Nodes expanded: {expanded}", file=file)
                print(f"Max fringe size: {len(fringe)}", file=file)
                print(f"Solution found at depth {depth} with cost {current_node.cost}", file=file)
                file.close()
            print(f"Goal found: state = {current_node.state}")
            print(f"Nodes popped: {popped}")
            print(f"Nodes expanded: {expanded}")
            print(f"Max fringe size: {len(fringe)}")
            print(f"Solution found at depth {depth} with cost {current_node.cost}")
            for i in range(len(steps)):
                print(f"\t{steps[i]}")
            return 0
    if np.array_equal(start, goal):
        return 0
    
def path_reconstruction(current_goal_node, state_step_map):
    reconstructed_path = []
    while current_goal_node.parent != 0:
        reconstructed_path.insert(0, state_step_map[tuple(current_goal_node.state.flatten())])
        current_goal_node = current_goal_node.parent
    return reconstructed_path
    

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
        #file handling
        with open(start_file, 'r') as file:
            start = []
            for line in file:
                if line.strip() == "END OF FILE":      #each start/goal file includes the END OF FILE line. so stop reading when that line is read.  
                    break
                start.append(line.split())             #splitting start contents by each character instead of each line
        with open(goal_file, 'r') as file:
            goal = []
            for line in file:
                if line.strip() == "END OF FILE":     
                    break
                goal.append(line.split())             #splitting goal contents by each character instead of each line
        #dflag dump file generation
        if dflag == "True" or dflag == "true" or dflag == 't': #the argv is read as a string so we check "True" instead of True and other forms of True
            dflag = True
            cdatetime = datetime.datetime.now()
            dfilename = cdatetime.strftime("trace-%m_%d_%Y-%H_%M") + ".txt"
            with open(dfilename, "w") as file:
                print(f"Command Line Arguments: ['{start_file}', '{goal_file}', '{method}', {dflag}]", file=file)
                print(f"Method: {method}", file=file)
        
        #making sure each element in the list is an int
        #turning the start & goal lists into matrices
        start = np.vectorize(int)(start)
        start = np.array(start)
        goal = np.vectorize(int)(goal)
        goal = np.array(goal)

        main(method)
    