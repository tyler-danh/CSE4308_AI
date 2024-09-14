Tyler Danh
1001706320

Python 3.11.7

Structure:
Code first parses the argvs to decide which search to use, which files for start and goal, and whether to create the dumpfile.
If dfile = True, then we will create the file for the code to write to before any searches are executed.
Start and Goal are then vectorized to ensure they're all ints then turned into NumPy arrays
Then the search is selected based on method

Search function is then called
Variables needed are then initialized
The first instance of Node is called, which will contain the start input
The first node is then added to the visited set and the search algorithim commences
Each search function has the same node expansion/generation until the check for valid indices
Then each function will check if the node is in visited then add to the queue/heap and print to dfile if dfile = true
Each function has the same prints in the event of NO SOLUTION FOUND

A seperate file containing the Node class is included.
Creates a node object for ease of use
The object contains the state, parent, cost and heuristic.

Instructions for Running:
python expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>
No need for " " around the method, just enter bfs, ucs, etc.
If the amount of flags is not the minimum (3) or too many flags (>4) are entered a message explaining usage will be displayed.
Make sure Node.py is in the same directory.
No other specific instructions.