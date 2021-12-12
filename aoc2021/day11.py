grid = []
count = 0
steps = 0

def inc_neighbors(x,y):

    grid[x][y] += 1

    if (y > 0):
        grid[x][y-1] += 1
    if (y < max_y):
        grid[x][y+1] += 1
    if (x > 0):
        grid[x-1][y] += 1
    if (x > 0) and (y > 0):
        grid[x-1][y-1] += 1
    if (x > 0) and (y < max_y):
        grid[x-1][y+1] += 1
    if (x < max_x):
        grid[x+1][y] += 1
    if (x < max_x) and (y > 0):
        grid[x+1][y-1] += 1
    if (x < max_x) and (y < max_y):
        grid[x+1][y+1] += 1


with open("input11.txt","r") as input:

    for line in input:
        grid.append([int(x) for x in list(line.strip())])

max_x = len(grid)-1
max_y = len(grid[0])-1

def grid_print(grid):

    for x, row in enumerate(grid):
        coll = ""
        for y, val in enumerate(row):
            coll += str(grid[x][y])
        print(coll)
    print("")

for x in range(500):

    steps += 1

    nines = []
    flashed = []

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            grid[x][y] += 1
            if grid[x][y] > 9:
                nines.append((x,y))

    while len(nines) > 0:
#        print(nines)
        (x,y) = nines.pop(0)
        if (x,y) in flashed:
            continue
        else:
            flashed.append((x,y))

            inc_neighbors(x,y)
            for x, row in enumerate(grid):
                for y, val in enumerate(row):
                    if grid[x][y] > 9:
                        if not (x,y) in flashed and not (x,y) in nines:
                            nines.append((x,y))

    for (x,y) in flashed:
        grid[x][y] = 0

    count += len(flashed)

    if len(flashed) == (max_x + 1) * (max_y + 1):
        print(steps)
        break;
#    grid_print(grid)

print(count)
