grid = []
lowpoints = []
cache = {}
sum = 0

def check(x,y,val):
    if (y > 0) and (grid[x][y-1] <= val):
        return 0
    elif (y < max_y) and (grid[x][y+1] <= val):
        return 0
    elif (x > 0) and (grid[x-1][y] <= val):
        return 0
#    elif (x > 0) and (y > 0) and (grid[x-1][y-1] <= val):
#        return 0
#    elif (x > 0) and (y < max_y) and (grid[x-1][y+1] <= val):
#        return 0
    elif (x < max_x) and (grid[x+1][y] <= val):
        return 0
#    elif (x < max_x) and (y > 0) and (grid[x+1][y-1] <= val):
#        return 0
#    elif (x < max_x) and (y < max_y) and (grid[x+1][y+1] <= val):
#        return 0
    else:
        return 1

def find_nb_val(x,y,val):
    if val == 9:
        return []
    print("Find "+str(val)+" from "+str(x)+","+str(y))
#    if (x,y,val) in cache:
#        return cache[(x,y,val)]
    neighbors = []
    if (y > 0) and (9 > grid[x][y-1] >= val):
        neighbors.append((x,y-1))
    if (y < max_y) and (9 > grid[x][y+1] >= val):
        neighbors.append((x,y+1))
    if (x > 0) and (9 > grid[x-1][y] >= val):
        neighbors.append((x-1,y))
#    if (x > 0) and (y > 0) and (grid[x-1][y-1] == val):
#        neighbors.append((x-1,y-1))
#    if (x > 0) and (y < max_y) and (grid[x-1][y+1] == val):
#        neighbors.append((x-1,y+1))
    if (x < max_x) and (9 > grid[x+1][y] >= val):
        neighbors.append((x+1,y))
#    if (x < max_x) and (y > 0) and (grid[x+1][y-1] == val):
#        neighbors.append((x+1,y-1))
#    if (x < max_x) and (y < max_y) and (grid[x+1][y+1] == val):
#        neighbors.append((x+1,y+1))
    cache[(x,y,val)] = neighbors
    return neighbors

def find_basin(search,found):
#    print(str(search)+" "+str(found))
    if not search:
        return found
    else:
        process = search.pop(0)
        add = find_nb_val(process[0],process[1],grid[process[0]][process[1]]+1)
        for new in add:
            if not new in found:
                found.append(new)
        return find_basin(search+add,found)

with open("input09.txt","r") as input:

    for line in input:
        grid.append([int(x) for x in list(line.strip())])

max_x = len(grid)-1
max_y = len(grid[0])-1
basins = []

for x, row in enumerate(grid):
    for y, val in enumerate(row):
        if check(x,y,val):
#            print(str(x)+" "+str(y)+" "+str(val))
            lowpoints.append((x,y))
            sum += val + 1

for point in lowpoints:
    (x,y) = point
    basins.append(len(find_basin([(x,y)],[(x,y)])))

print(max_x)
print(max_y)
#print(grid)
print(sum)
print(lowpoints)
basins.sort()
print(basins)
