"""this code is functionally useless for the assignment
but the logic is helpful."""
for node in nodes: #finding each node's neighbors
        i,j = node
        if flag == True:
            with open(dfilename, "a") as file: #REMEMBER TO OPEN THE FILE IN MODE='a' SO IT DOESNT OVERWRITE THE FILE
                print(f"neighbors of {start[node]}", file=file)
                if (i == 2 and j == 2) or (i == 2 and j > 0) or (j == 2 and i > 0):
                    print(f"{start[i-1, j]}, ({i-1}, {j})", file=file)
                    print(f"{start[i, j-1]}, ({i}, {j-1})", file=file)
                    continue
                elif (i == 0 and j == 0) or (i == 0 and j < 2) or (j == 0 and i < 2):
                    print(f"{start[i+1, j]}, ({i+1}, {j})", file=file)
                    print(f"{start[i, j+1]}, ({i}, {j+1})", file=file)
                    continue
                elif i == 1 and j == 1:
                    print(f"{start[i-1, j]}, ({i-1}, {j})", file=file)
                    print(f"{start[i, j-1]}, ({i}, {j-1})", file=file)
                    print(f"{start[i+1, j]}, ({i+1}, {j})", file=file)
                    print(f"{start[i, j+1]}, ({i}, {j+1})", file=file)
                elif i == 2 and j == 0:
                    print(f"{start[i-1, j]}, ({i-1}, {j})", file=file)
                    print(f"{start[i, j+1]}, ({i}, {j+1})", file=file)
                elif i == 0 and j == 2:
                    print(f"{start[i+1, j]}, ({i+1}, {j})", file=file)
                    print(f"{start[i, j-1]}, ({i}, {j-1})", file=file)