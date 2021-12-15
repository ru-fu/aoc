grid = []

def print_grid():

    for x, row in enumerate(grid):
        coll = ""
        for y, val in enumerate(row):
            coll += str(grid[x][y])
        print(coll)
    print("")

def extend_grid():
    for x,line in enumerate(grid):
        line_copy = line.copy()
        for i in range(4):
            for y,char in enumerate(line_copy):
                new_char = char + i + 1
                if new_char > 9:
                    new_char = new_char - 9
                grid[x].append(new_char)

    grid_copy = grid.copy()
    for i in range(4):
        for line in grid_copy:
            new_line = []
            for char in line:
                new_char = char + i + 1
                if new_char > 9:
                    new_char = new_char - 9
                new_line.append(new_char)
            grid.append(new_line)

with open("input15.txt","r") as input:

    for line in input:
        grid.append([int(x) for x in list(line.strip())])

extend_grid()
#print_grid()

max_y = len(grid)-1
max_x = len(grid[0])-1

def find_nb(one):
    neighbors = []
    (x,y) = one
    if x > 0:
        neighbors.append((x-1,y))
    if x < max_x:
        neighbors.append((x+1,y))
    if y > 0:
        neighbors.append((x,y-1))
    if y < max_y:
        neighbors.append((x,y+1))
    return neighbors

saved_lowest = -1

def find_current():
    global saved_lowest
    lowest_val = -1
    lowest = None
    for x in unvisited:
        if x in levels:
            if lowest_val == -1 or levels[x] < lowest_val:
                lowest_val = levels[x]
                lowest = x
            if saved_lowest > -1 and lowest_val == saved_lowest:
                return lowest
    if lowest:
        saved_lowest = lowest_val
        return lowest
    else:
        return None

unvisited = []
for x in range(max_x+1):
    for y in range(max_y+1):
        unvisited.append((x,y))

visited = []
levels = {(0,0): 0}

current = find_current()

while current and not (max_x,max_y) in levels:
    #print(current)
    if len(visited) % 1000 == 0:
        print(len(visited))
    neighbors = [x for x in find_nb(current) if x not in visited]

    for nb in neighbors:
        distance = levels[current] + grid[nb[0]][nb[1]]
        if nb in levels and levels[nb] > distance:
            levels[nb] = distance
        elif not nb in levels:
            levels[nb] = distance

    visited.append(current)
    unvisited.remove(current)
    levels.pop(current)

    current = find_current()

print(levels[(max_x,max_y)])
