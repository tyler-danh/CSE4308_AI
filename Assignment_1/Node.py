class node:
    def __init__(this, state, parent, cost, heuristic = 0):
        this.state = state          #some matrix, successor or start
        this.parent = parent        #prev node. if none then parent = 0
        this.cost = cost            # will be the value of the matrix element
        this.heuristic = heuristic #will be used in greedy/A*, default is 0

        def __eq__(this, other):
            return (this.state, this.cost, this.heuristic) == (other.state, other.cost, other.heuristic)
        def __lt__(this, other):
            return (this.cost + this.heuristic) < (other.cost + other.heuristic) #adding heuristic should not matter in bfs or ucs
        def __hash__(this):
            return hash((this.state, this.cost, this.heuristic))