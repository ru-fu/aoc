import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
  max_x = 6
  max_y = 6
  howmany = 12
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"
  max_x = 70
  max_y = 70
  howmany = 1024

allcoords = []
costs = {}
coords = []
visited = []
unvisited = []
  
with open(inputfile,"r") as input:

  for line in input:
    c = line.rstrip().split(",")
    allcoords.append((int(c[1]),int(c[0])))

def find_neighbors(start,coords):
  global max_x, max_y
  (x,y) = start
  nbs = []

  if 0 <= x-1 <= max_x and 0 <= y <= max_y and not (x-1,y) in coords:
    nbs.append((x-1,y))
  if 0 <= x+1 <= max_x and 0 <= y <= max_y and not (x+1,y) in coords:
    nbs.append((x+1,y))
  if 0 <= x <= max_x and 0 <= y-1 <= max_y and not (x,y-1) in coords:
    nbs.append((x,y-1))
  if 0 <= x <= max_x and 0 <= y+1 <= max_y and not (x,y+1) in coords:
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
    raise Exception("No path found!")

def calc_costs(fr,nbs):
  global costs

  new_cost = 1 + costs[fr]
  
  for nb in nbs:

    if nb in costs and costs[nb] > new_cost:
      costs[nb] = new_cost
    elif not nb in costs:
      costs[nb] = new_cost

def run(coords):
  global costs,max_y,max_y,visted,unvisited,end

  costs = {(0,0): 0}
  visited = []
  unvisited = []
  for x in range(max_x+1):
    for y in range(max_y+1):
      unvisited.append((x,y))
  end = (max_x,max_y)

  current = find_current()

  while current:
    
    #if len(visited) % 1000 == 0:
    #    print(len(visited))
    
    if current == end:
      print("Found "+str(current))
      break

    #print("Processing "+str(current))

    nbs = find_neighbors(current,coords)

    calc_costs(current,nbs)
    #print(costs)
    
    visited.append(current)
    unvisited.remove(current)

    current = find_current()
      
    
def run_part1():

  run(allcoords[:howmany])

  print(costs[end])

def run_part2():

  global allcoords,howmany

  for i in range(howmany,len(allcoords)):

    print(allcoords[:i])
    run(allcoords[:i])


run_part1()
run_part2()
