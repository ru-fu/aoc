import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

grid = []
options = {}

with open(inputfile,"r") as input:

  grid = [line.rstrip() for line in input if len(line) > 1]

  max_x = len(grid)
  max_y = len(grid[0])

def get(neighbor):
  if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y and neighbor in options:
    return (int(grid[neighbor[0]][neighbor[1]]),options[neighbor])
  else:
    return (-9,None)
  
def get2(neighbor):
  if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y and neighbor in options:
    return (int(grid[neighbor[0]][neighbor[1]]),options[neighbor])
  else:
    return (-9,None)
  
def find_tops(h,x,y,which):

  if which == 1:
    if h == 9:
      return {(x,y)}
    else:
      ret = set()
      for nb in [(x-1,y),(x,y+1),(x,y-1),(x+1,y)]:
        nb_result = get(nb)
        #  print("NB: "+str(nb)+" result: "+str(nb_result))
        if nb_result[0] == h + 1:
          ret.update(nb_result[1])
 #   print("ret: "+str(ret))
      return ret

  else:
    if h == 9:
      return 1
    else:
      ret = 0
      for nb in [(x-1,y),(x,y+1),(x,y-1),(x+1,y)]:
        nb_result = get2(nb)
        if nb_result[0] == h + 1:
          ret += nb_result[1]
      return ret
  
def fill_options(which):
  global grid, options

  for h in range(9,-1,-1):
    for i,x in enumerate(grid):
      for j,y in enumerate(x):
        if y.isdigit() and int(y) == h:
          options[(i,j)] = find_tops(h,i,j,which)

def find_trailheads(which):
  global grid,options

  ret = []
  
  for i,x in enumerate(grid):
    for j,y in enumerate(x):
      if y.isdigit() and int(y) == 0:
        if which == 1:
          ret.append(len(options[(i,j)]))
        else:
          ret.append(options[(i,j)])

  return ret
  
def run_part1():

  fill_options(1)
  
  for l in grid:
    print(l)

  print(options)
  print(sum(find_trailheads(1)))

def run_part2():
  global options

  del options
  options = {}
  

  fill_options(2)
  print(options)
  print(sum(find_trailheads(2)))

run_part1()
run_part2()
