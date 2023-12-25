import sys
from functools import cache

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

vals = []

with open(inputfile,"r") as input:

  for x,line in enumerate(input):
    line = line.strip()
    vals.append([])
    for char in line:
      vals[x].append(int(char))

  max_x = x + 1
  max_y = len(line)


def find_nb(start,direction):
    global max_x, max_y
    options = []
    if len(direction) == 0 or direction == "^" or direction == "v":
        if start[1] + 1 < max_y:
            options.append(((start[0],start[1] + 1),">"))
        if start[1] + 2 < max_y:
            options.append(((start[0],start[1] + 2),">"))
        if start[1] + 3 < max_y:
            options.append(((start[0],start[1] + 3),">"))
        if start[1] - 1 >= 0:
            options.append(((start[0],start[1] - 1),"<"))
        if start[1] - 2 >= 0:
            options.append(((start[0],start[1] - 2),"<"))
        if start[1] - 3 >= 0:
            options.append(((start[0],start[1] - 3),"<"))
    if len(direction) == 0 or direction == "<" or direction == ">":
        if start[0] + 1 < max_x:
            options.append(((start[0] + 1,start[1]),"v"))
        if start[0] + 2 < max_x:
            options.append(((start[0] + 2,start[1]),"v"))
        if start[0] + 3 < max_x:
            options.append(((start[0] + 3,start[1]),"v"))
        if start[0] - 1 >= 0:
            options.append(((start[0] - 1,start[1]),"^"))
        if start[0] - 2 >= 0:
            options.append(((start[0] - 2,start[1]),"^"))
        if start[0] - 3 >= 0:
            options.append(((start[0] - 3,start[1]),"^"))

    return options

def find_nb2(start,direction):
    global max_x, max_y
    options = []
    if len(direction) == 0 or direction == "^" or direction == "v":
        if start[1] + 4 < max_y:
            options.append(((start[0],start[1] + 4),">"))
        if start[1] + 5 < max_y:
            options.append(((start[0],start[1] + 5),">"))
        if start[1] + 6 < max_y:
            options.append(((start[0],start[1] + 6),">"))
        if start[1] + 7 < max_y:
            options.append(((start[0],start[1] + 7),">"))
        if start[1] + 8 < max_y:
            options.append(((start[0],start[1] + 8),">"))
        if start[1] + 9 < max_y:
            options.append(((start[0],start[1] + 9),">"))
        if start[1] + 10 < max_y:
            options.append(((start[0],start[1] + 10),">"))
        if start[1] - 4 >= 0:
            options.append(((start[0],start[1] - 4),"<"))
        if start[1] - 5 >= 0:
            options.append(((start[0],start[1] - 5),"<"))
        if start[1] - 6 >= 0:
            options.append(((start[0],start[1] - 6),"<"))
        if start[1] - 7 >= 0:
            options.append(((start[0],start[1] - 7),"<"))
        if start[1] - 8 >= 0:
            options.append(((start[0],start[1] - 8),"<"))
        if start[1] - 9 >= 0:
            options.append(((start[0],start[1] - 9),"<"))
        if start[1] - 10 >= 0:
            options.append(((start[0],start[1] - 10),"<"))
    if len(direction) == 0 or direction == "<" or direction == ">":
        if start[0] + 4 < max_x:
            options.append(((start[0] + 4,start[1]),"v"))
        if start[0] + 5 < max_x:
            options.append(((start[0] + 5,start[1]),"v"))
        if start[0] + 6 < max_x:
            options.append(((start[0] + 6,start[1]),"v"))
        if start[0] + 7 < max_x:
            options.append(((start[0] + 7,start[1]),"v"))
        if start[0] + 8 < max_x:
            options.append(((start[0] + 8,start[1]),"v"))
        if start[0] + 9 < max_x:
            options.append(((start[0] + 9,start[1]),"v"))
        if start[0] + 10 < max_x:
            options.append(((start[0] + 10,start[1]),"v"))
        if start[0] - 4 >= 0:
            options.append(((start[0] - 4,start[1]),"^"))
        if start[0] - 5 >= 0:
            options.append(((start[0] - 5,start[1]),"^"))
        if start[0] - 6 >= 0:
            options.append(((start[0] - 6,start[1]),"^"))
        if start[0] - 7 >= 0:
            options.append(((start[0] - 7,start[1]),"^"))
        if start[0] - 8 >= 0:
            options.append(((start[0] - 8,start[1]),"^"))
        if start[0] - 9 >= 0:
            options.append(((start[0] - 9,start[1]),"^"))
        if start[0] - 10 >= 0:
            options.append(((start[0] - 10,start[1]),"^"))

    return options

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
        if x == 0 and y == 0:
            unvisited.append(((x,y),""))
        else:
            unvisited.append(((x,y),">"))
            unvisited.append(((x,y),"<"))
            unvisited.append(((x,y),"^"))
            unvisited.append(((x,y),"v"))

def calc_distance(current,nb):
    global levels, vals

    result = levels[current]

    if nb[1] == ">":
        result += vals[nb[0][0]][nb[0][1]]
        if nb[0][1]-1 >= 0 and nb[0][1]-1 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-1]
        if nb[0][1]-2 >= 0 and nb[0][1]-2 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-2]
    elif nb[1] == "<":
        result += vals[nb[0][0]][nb[0][1]]
        if nb[0][1]+1 < max_y and nb[0][1]+1 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+1]
        if nb[0][1]+2 < max_y and nb[0][1]+2 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+2]
    elif nb[1] == "v":
        result += vals[nb[0][0]][nb[0][1]]
        if nb[0][0]-1 >= 0 and nb[0][0]-1 > current[0][0]:
            result += vals[nb[0][0]-1][nb[0][1]]
        if nb[0][0]-2 >= 0 and nb[0][0]-2 > current[0][0]:
            result += vals[nb[0][0]-2][nb[0][1]]
    elif nb[1] == "^":
        result += vals[nb[0][0]][nb[0][1]]
        if nb[0][0]+1 < max_x and nb[0][0]+1 < current[0][0]:
            result += vals[nb[0][0]+1][nb[0][1]]
        if nb[0][0]+2 < max_x and nb[0][0]+2 < current[0][0]:
            result += vals[nb[0][0]+2][nb[0][1]]

    return result

def calc_distance2(current,nb):
    global levels, vals

    result = levels[current]

    if nb[1] == ">":
        result += vals[nb[0][0]][nb[0][1]] + vals[nb[0][0]][nb[0][1] - 1] + vals[nb[0][0]][nb[0][1] - 2] + vals[nb[0][0]][nb[0][1] - 3]
        if nb[0][1]-4 >= 0 and nb[0][1]-4 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-4]
        if nb[0][1]-5 >= 0 and nb[0][1]-5 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-5]
        if nb[0][1]-6 >= 0 and nb[0][1]-6 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-6]
        if nb[0][1]-7 >= 0 and nb[0][1]-7 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-7]
        if nb[0][1]-8 >= 0 and nb[0][1]-8 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-8]
        if nb[0][1]-9 >= 0 and nb[0][1]-9 > current[0][1]:
            result += vals[nb[0][0]][nb[0][1]-9]
    elif nb[1] == "<":
        result += vals[nb[0][0]][nb[0][1]] + vals[nb[0][0]][nb[0][1] + 1] + vals[nb[0][0]][nb[0][1] + 2] + vals[nb[0][0]][nb[0][1] + 3]
        if nb[0][1]+4 < max_y and nb[0][1]+4 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+4]
        if nb[0][1]+5 < max_y and nb[0][1]+5 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+5]
        if nb[0][1]+6 < max_y and nb[0][1]+6 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+6]
        if nb[0][1]+7 < max_y and nb[0][1]+7 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+7]
        if nb[0][1]+8 < max_y and nb[0][1]+8 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+8]
        if nb[0][1]+9 < max_y and nb[0][1]+9 < current[0][1]:
            result += vals[nb[0][0]][nb[0][1]+9]
    elif nb[1] == "v":
        result += vals[nb[0][0]][nb[0][1]] + vals[nb[0][0]-1][nb[0][1]] + vals[nb[0][0]-2][nb[0][1]] + vals[nb[0][0]-3][nb[0][1]]
        if nb[0][0]-4 >= 0 and nb[0][0]-4 > current[0][0]:
            result += vals[nb[0][0]-4][nb[0][1]]
        if nb[0][0]-5 >= 0 and nb[0][0]-5 > current[0][0]:
            result += vals[nb[0][0]-5][nb[0][1]]
        if nb[0][0]-6 >= 0 and nb[0][0]-6 > current[0][0]:
            result += vals[nb[0][0]-6][nb[0][1]]
        if nb[0][0]-7 >= 0 and nb[0][0]-7 > current[0][0]:
            result += vals[nb[0][0]-7][nb[0][1]]
        if nb[0][0]-8 >= 0 and nb[0][0]-8 > current[0][0]:
            result += vals[nb[0][0]-8][nb[0][1]]
        if nb[0][0]-9 >= 0 and nb[0][0]-9 > current[0][0]:
            result += vals[nb[0][0]-9][nb[0][1]]
    elif nb[1] == "^":
        result += vals[nb[0][0]][nb[0][1]] + vals[nb[0][0]+1][nb[0][1]] + vals[nb[0][0]+2][nb[0][1]] + vals[nb[0][0]+3][nb[0][1]]
        if nb[0][0]+4 < max_x and nb[0][0]+4 < current[0][0]:
            result += vals[nb[0][0]+4][nb[0][1]]
        if nb[0][0]+5 < max_x and nb[0][0]+5 < current[0][0]:
            result += vals[nb[0][0]+5][nb[0][1]]
        if nb[0][0]+6 < max_x and nb[0][0]+6 < current[0][0]:
            result += vals[nb[0][0]+6][nb[0][1]]
        if nb[0][0]+7 < max_x and nb[0][0]+7 < current[0][0]:
            result += vals[nb[0][0]+7][nb[0][1]]
        if nb[0][0]+8 < max_x and nb[0][0]+8 < current[0][0]:
            result += vals[nb[0][0]+8][nb[0][1]]
        if nb[0][0]+9 < max_x and nb[0][0]+9 < current[0][0]:
            result += vals[nb[0][0]+9][nb[0][1]]

    return result


visited = []
levels = {((0,0),""): 0}

current = ((0,0),"")

print(len(unvisited))

part = 2

while current and not (((max_x-1,max_y-1),">") in levels and ((max_x-1,max_y-1),"v") in levels):
    #print("Current "+str(current))
    #print(levels[current])

    if len(visited) % 1000 == 0:
        print(len(visited))
    if part == 1:
        neighbors = [x for x in find_nb(current[0],current[1]) if x not in visited]
    else:
        neighbors = [x for x in find_nb2(current[0],current[1]) if x not in visited]

    for nb in neighbors:
        if part == 1:
            distance = calc_distance(current,nb)
        else:
            distance = calc_distance2(current,nb)
        #print("To nb: "+str(nb))
        #print(distance)
        if nb in levels and levels[nb] > distance:
            levels[nb] = distance
        elif not nb in levels:
            levels[nb] = distance

    visited.append(current)
    unvisited.remove(current)
    if not current[0] == (max_x-1,max_y-1):
        levels.pop(current)

   # print(visited)
   # print(unvisited)
   # print(levels)

    current = find_current()

#print(levels)
if ((max_x-1,max_y-1),">") in levels:
    print(levels[((max_x-1,max_y-1),">")])
if ((max_x-1,max_y-1),"v") in levels:
    print(levels[((max_x-1,max_y-1),"v")])
