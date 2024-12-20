import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

allwalls = []
start = None
endloc = None
max_x = 0
max_y = 0
costs = {}
visited = []
unvisited = []
  
with open(inputfile,"r") as input1:

  for i,line in enumerate(input1):
    line = line.rstrip()
    for j,val in enumerate(line):
      if val == "#":
        allwalls.append((i,j))
      elif val == "S":
        start = (i,j)
      elif val == "E":
        endloc = (i,j)
      if j > max_y:
        max_y = j
    max_x = i

def find_neighbors(start,walls):
  global max_x, max_y
  (x,y) = start
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
    
def find_current(maxmoves = 0):
  global unvisited, costs

  lowest_val = -1
  lowest = None

  for x in unvisited:
    if x in costs:
      if maxmoves > 0 and costs[x] > maxmoves:
        return None
      if lowest_val == -1 or costs[x] < lowest_val:
        lowest_val = costs[x]
        lowest = x
        
  if lowest:
    return lowest
  else:
    print("huh?")
    #raise Exception("No path found!")

def calc_costs(fr,nbs):
  global costs

  new_cost = 1 + costs[fr]
  
  for nb in nbs:

    if nb in costs and costs[nb] > new_cost:
      costs[nb] = new_cost
    elif not nb in costs:
      costs[nb] = new_cost

def run(walls,maxmoves = 0):
  global costs,max_y,max_y,visted,unvisited,endloc

  costs = {start: 0}
  visited = []
  unvisited = []
  for x in range(max_x+1):
    for y in range(max_y+1):
      if not (x,y) in walls:
        unvisited.append((x,y))

  current = find_current(maxmoves)

  while current:
    
    #if len(visited) % 1000 == 0:
    #    print(len(visited))
    
    if current == endloc:
#      print("Found "+str(current))
      break

    #print("Processing "+str(current))

    nbs = find_neighbors(current,walls)

    calc_costs(current,nbs)
    #print(costs)
    
    visited.append(current)
    unvisited.remove(current)

    current = find_current()
      
    
def run_part1():
  global allwalls, costs, endloc

  run(allwalls)
  default = costs[endloc]

  shorter = []

  savehowmuch = 100

  print(len(allwalls))
  i = 0

  for w in allwalls:
    print(i)
    i += 1
    newwalls = allwalls.copy()
    newwalls.remove(w)
    run(newwalls,default-savehowmuch)
    if costs[endloc] + savehowmuch <= default:
      shorter.append(w)

  print(shorter)
  print(len(shorter))

def run_part2():

  global allcoords,howmany

  for i in range(howmany,len(allcoords)):

    print(allcoords[:i])
    run(allcoords[:i])


run_part1()
#run_part2()
