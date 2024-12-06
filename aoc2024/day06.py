import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

grid = []
  
with open(inputfile,"r") as input:

  grid = [line.rstrip() for line in input]

  for i,x in enumerate(grid):
    pos = x.find("^")
    if pos >= 0:
      startguard = (i,pos,"^")
      break

def get(x,y,grid):
  
  if 0 <= x < len(grid):
    if 0 <= y < len(grid[x]):
      return grid[x][y]

  return "OoB"
  
def next_pos(guard, grid):
  (x,y,facing) = guard

  new_x = x
  new_y = y
  new_facing = facing

  if facing == "^":
    new_x = x-1
    new_facing = ">"
  elif facing == ">":
    new_y = y+1
    new_facing = "v"
  elif facing == "<":
    new_y = y-1
    new_facing = "^"
  elif facing == "v":
    new_x = x+1
    new_facing = "<"
  else:
    print("huh?!")

  new_pos = get(new_x,new_y,grid)
  if new_pos == "." or new_pos == "^":
    return (new_x,new_y,facing)
  elif new_pos == "#":
    return (x,y,new_facing)
  elif new_pos == "OoB":
    return None

def mycopy(x,y):
  global grid

  newgrid = []

  for i in range(len(grid)):
    if not i == x:
      newgrid.append(grid[i])
    else:
      new_y = ""
      for j in range(len(grid[i])):
        if not j == y:
          new_y += grid[i][j]
        else:
          new_y += "#"
      newgrid.append(new_y)

  return newgrid
      

path = set()

def run_part1():
  global startguard

  fullpath = set()
  print(startguard)
  guard = startguard

  while guard:
#    print(guard)
    path.add((guard[0],guard[1]))
    if guard in fullpath:
      print(guard)
      print("LOOP!")
    fullpath.add(guard)
    guard = next_pos(guard,grid)

#  for line in grid:
#    print(line)

#  print(path)
  print(len(path))
#  print(len(fullpath))

def run_part2():

  options = 0

  for (x,y) in path:
    if not grid[x][y] == "^":
      newgrid = mycopy(x,y)
     # for l in newgrid:
     #   print(l)
     # print()

      guard = startguard

      fullpath = set()

      while guard:
#    print(guard)
        if guard in fullpath:
#          print(guard)
#          print("LOOP!")
          options += 1
          break
        fullpath.add(guard)
        guard = next_pos(guard,newgrid)

  print(options)

run_part1()
run_part2()
