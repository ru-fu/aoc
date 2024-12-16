import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

walls = []
start = None
endloc = None
max_x = 0
max_y = 0
  
with open(inputfile,"r") as input1:

  for i,line in enumerate(input1):
    line = line.rstrip()
    for j,val in enumerate(line):
      if val == "#":
        walls.append((i,j))
      elif val == "S":
        start = (">",i,j)
      elif val == "E":
        endloc = (i,j)
      if j > max_y:
        max_y = j
    max_x = i

def find_neighbors(start):
  global max_x, max_y, walls
  (facing,x,y) = start
  nbs = []

  if 0 <= x-1 <= max_x and 0 <= y <= max_y and not (x-1,y) in walls:
    nbs.append((x-1,y))
  if 0 <= x+1 <= max_x and 0 <= y <= max_y and not (x+1,y) in walls:
    nbs.append((x+1,y))
  if 0 <= x <= max_x and 0 <= y-1 <= max_y and not (x,y-1) in walls:
    nbs.append((x,y-1))
  if 0 <= x <= max_x and 0 <= y+1 <= max_y and not (x,y+1) in walls:
    nbs.append((x,y+1))

  return nbs
    
def find_current():
  global unvisited, costs

  lowest_val = -1
  lowest = None

  for x in unvisited:
    if x in costs:
      if lowest_val == -1 or costs[x] < lowest_val:
        lowest_val = costs[x]
        lowest = x
        
  if lowest:
    return lowest
  else:
    print("huh?")

def set_cost(where,what,fr):
  global costs,bestpaths

#  print("Cost "+str(where)+": "+str(what)+ " (from "+str(fr)+")")

  if where in costs and costs[where] > what:
    costs[where] = what
    oldpaths = []
    for old in bestpaths[fr]:
      oldpaths.append(old.copy())
    paths = []
    for p in oldpaths:
      p.add((where[1],where[2]))
      paths.append(p)
    bestpaths[where] = paths
#    print("Better path: "+str(bestpaths[where]))
    #input()
  elif where in costs and costs[where] == what:
    oldpaths = []
    for old in bestpaths[fr]:
      oldpaths.append(old.copy())
    paths = []
    for p in oldpaths:
      p.add((where[1],where[2]))
      paths.append(p)
    bestpaths[where] = bestpaths[where] + paths
#    print("Equal path: "+str(bestpaths[where]))
    #input()
  elif not where in costs:
    costs[where] = what
    oldpaths = []
    for old in bestpaths[fr]:
      oldpaths.append(old.copy())
#    print("Old paths: "+ str(oldpaths))
    paths = []
    for p in oldpaths:
      p.add((where[1],where[2]))
      paths.append(p)
    bestpaths[where] = paths
#    print("New path: "+str(bestpaths[where]))
    #input()

def calc_costs(fr,nbs):
  global costs
  (facing,x,y) = fr

  for nb in nbs:
    #print("Consider "+str(nb))
    if facing == "^" and nb[0] == x-1 and nb[1] == y:
        set_cost(("^",nb[0],nb[1]),1 + costs[fr],fr)
        set_cost(("<",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost(("v",nb[0],nb[1]),2001 + costs[fr],fr)
        set_cost((">",nb[0],nb[1]),1001 + costs[fr],fr)
    elif facing == "v" and nb[0] == x+1 and nb[1] == y:
        set_cost(("^",nb[0],nb[1]),2001 + costs[fr],fr)
        set_cost(("<",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost(("v",nb[0],nb[1]),1 + costs[fr],fr)
        set_cost((">",nb[0],nb[1]),1001 + costs[fr],fr)
    elif facing == "<" and nb[0] == x and nb[1] == y-1:
        set_cost(("^",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost(("<",nb[0],nb[1]),1 + costs[fr],fr)
        set_cost(("v",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost((">",nb[0],nb[1]),2001 + costs[fr],fr)
    elif facing == ">" and nb[0] == x and nb[1] == y+1:
        set_cost(("^",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost(("<",nb[0],nb[1]),2001 + costs[fr],fr)
        set_cost(("v",nb[0],nb[1]),1001 + costs[fr],fr)
        set_cost((">",nb[0],nb[1]),1 + costs[fr],fr)
   # else:
   #   print("nope")

  
        
costs = {start: 0,
         ("^",start[1],start[2]): 1000,
         ("v",start[1],start[2]): 1000,
         ("<",start[1],start[2]): 2000}
visited = []
unvisited = [start]
bestpaths = {start: [{(start[1],start[2])}],
             ("^",start[1],start[2]): [{(start[1],start[2])}],
             ("v",start[1],start[2]): [{(start[1],start[2])}],
             ("<",start[1],start[2]): [{(start[1],start[2])}]
             }
ends = []

for d in ["<","^",">","v"]:
  ends.append((d,endloc[0],endloc[1]))

def run_part1():
  global unvisited,costs, visited,bestpaths,ends

  
  unvisited += ends
  for x in range(max_x+1):
    for y in range(max_y+1):
      if not (x,y) in walls:
        for d in ["<","^",">","v"]:
          unvisited.append((d,x,y))

  current = find_current()

  while current:
    
    if len(visited) % 1000 == 0:
        print(len(visited))
    
    if current in ends:
      print("Found "+str(current))
      break

    #print("Processing "+str(current))

    nbs = find_neighbors(current)

    calc_costs(current,nbs)
    #print(costs)
    
    visited.append(current)
    unvisited.remove(current)

    current = find_current()

  result = [costs[e] for e in ends]
  print(result)
  print(min(result))

def run_part2():
  global bestpaths,ends

  result = [bestpaths[e] for e in ends]
  tiles = set()
  for r in result:
    for path in r:
      for tile in path:
        tiles.add(tile)

  print(len(tiles))

run_part1()
run_part2()
