import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

grid = []
stargrid = []


with open(inputfile,"r") as input:

  for line in input:
    grid.append(list(line.strip()))

  x_length = len(grid)
  y_length = len(grid[0])

  for x in range(x_length):
    for y in range(y_length):
      if grid[x][y] == "S":
        start = (x,y)
        break

def move(paths):

  global grid, x_length, y_length

  new = (None,None)

  for i,path in enumerate(paths):
    (frx, fry) = path[-1]
#    print("Checking ("+str(frx)+","+str(fry)+")")
    if grid[frx][fry] == "|":
      if frx > 0 and (grid[frx - 1][fry] == "|" or grid[frx - 1][fry] == "F" or grid[frx - 1][fry] == "7") and not (frx - 1,fry) in path:
        paths[i] = path + [(frx - 1,fry)]
        new = (frx - 1,fry)
      elif frx + 1 < x_length and (grid[frx + 1][fry] == "|" or grid[frx + 1][fry] == "L" or grid[frx + 1][fry] == "J") and not (frx + 1,fry) in path:
        paths[i] = path + [(frx + 1,fry)]
        new = (frx + 1,fry)
    elif grid[frx][fry] == "-":
      if fry > 0 and (grid[frx][fry - 1] == "-" or grid[frx][fry - 1] == "F" or grid[frx][fry - 1] == "L") and not (frx,fry - 1) in path:
        paths[i] = path + [(frx,fry - 1)]
        new = (frx,fry - 1)
      elif fry + 1 < y_length and (grid[frx][fry + 1] == "-" or grid[frx][fry + 1] == "J" or grid[frx][fry + 1] == "7") and not (frx,fry + 1) in path:
        paths[i] = path + [(frx,fry + 1)]
        new = (frx,fry + 1)
    if grid[frx][fry] == "L":
      if frx > 0 and (grid[frx - 1][fry] == "|" or grid[frx - 1][fry] == "F" or grid[frx - 1][fry] == "7") and not (frx - 1,fry) in path:
        paths[i] = path + [(frx - 1,fry)]
        new = (frx - 1,fry)
      elif fry + 1 < y_length and (grid[frx][fry + 1] == "-" or grid[frx][fry + 1] == "J" or grid[frx][fry + 1] == "7") and not (frx,fry + 1) in path:
        paths[i] = path + [(frx,fry + 1)]
        new = (frx,fry + 1)
    elif grid[frx][fry] == "J":
      if fry > 0 and (grid[frx][fry - 1] == "-" or grid[frx][fry - 1] == "F" or grid[frx][fry - 1] == "L") and not (frx,fry - 1) in path:
        paths[i] = path + [(frx,fry - 1)]
        new = (frx,fry - 1)
      elif frx > 0 and (grid[frx - 1][fry] == "|" or grid[frx - 1][fry] == "F" or grid[frx - 1][fry] == "7") and not (frx - 1,fry) in path:
        paths[i] = path + [(frx - 1,fry)]
        new = (frx - 1,fry)
    elif grid[frx][fry] == "7":
      if fry > 0 and (grid[frx][fry - 1] == "-" or grid[frx][fry - 1] == "F" or grid[frx][fry - 1] == "L") and not (frx,fry - 1) in path:
        paths[i] = path + [(frx,fry - 1)]
        new = (frx,fry - 1)
      elif frx + 1 < x_length and (grid[frx + 1][fry] == "|" or grid[frx + 1][fry] == "L" or grid[frx + 1][fry] == "J") and not (frx + 1,fry) in path:
        paths[i] = path + [(frx + 1,fry)]
        new = (frx + 1,fry)
    elif grid[frx][fry] == "F":
      if fry + 1 < y_length and (grid[frx][fry + 1] == "-" or grid[frx][fry + 1] == "J" or grid[frx][fry + 1] == "7") and not (frx,fry + 1) in path:
        paths[i] = path + [(frx,fry + 1)]
        new = (frx,fry + 1)
      elif frx + 1 < x_length and (grid[frx + 1][fry] == "|" or grid[frx + 1][fry] == "L" or grid[frx + 1][fry] == "J") and not (frx + 1,fry) in path:
        paths[i] = path + [(frx + 1,fry)]
        new = (frx + 1,fry)

    if new == (None,None):
      paths[i] = []
#    else:
#      print("Found new: "+str(new))

    for j in range(len(paths)):
      if not i == j:
        if new in paths[j]:
          return (True,[paths[i],paths[j]])

  paths = [x for x in paths if not x == []]

  return (False, paths)


def visualize(path):

  global stargrid

  global grid, x_length, y_length
  for x in range(x_length):
    line = ""
    for y in range(y_length):
      if (x,y) in path:
        line += "*"
      elif grid[x][y] == "S":
        line += "*"
      else:
        line += "."
    stargrid.append(line)
    print(line)

theloop = []

def run_part1():

  global theloop
  paths = []

  if grid[start[0] - 1][start[1]] == "|" or grid[start[0] - 1][start[1]] == "7" or grid[start[0] - 1][start[1]] == "F":
    paths.append([(start[0] - 1,start[1])])
  if grid[start[0] + 1][start[1]] == "|" or grid[start[0] + 1][start[1]] == "J" or grid[start[0] + 1][start[1]] == "L":
    paths.append([(start[0] + 1,start[1])])
  if grid[start[0]][ start[1] - 1] == "-" or grid[start[0]][ start[1] - 1] == "F" or grid[start[0]][ start[1] - 1] == "L":
    paths.append([(start[0],start[1] - 1)])
  if grid[start[0]][ start[1] + 1] == "-" or grid[start[0]][ start[1] + 1] == "J" or grid[start[0]][ start[1] + 1] == "7":
    paths.append([(start[0],start[1] + 1)])

#  print(paths)
  result = (False, paths)

  while result[0] == False:
    result = move(result[1])
#    print(result)

  print([len(x) for x in result[1]])


  theloop = result[1][0] + result[1][1][:-1]
#  print(grid)
#  print(start)
#  print(x_length)

def run_part2():

  global theloop

  visualize(theloop)

  potentials = []
  for x in range(x_length):
    for y in range(y_length):
      if stargrid[x][y] == ".":
        if "*" in stargrid[x][:y]:
          if "*" in stargrid[x][y:]:
            potentials.append((x,y))

  for pot in list(potentials):
    found1 = False
    print("Checking "+str(pot))
    for x in range(pot[0],x_length):
      if x+1 < x_length and stargrid[x+1][pot[1]] == "*":
        found1 = True
        break
    if found1:
      found2 = False
      for x in range(0,pot[0]):
        if stargrid[x][pot[1]] == "*":
          found2 = True
          break
    if not (found1 and found2):
      print("Remove "+str(pot))
      potentials.remove(pot)

  print(potentials)

  inner = []

  polygon = Polygon(theloop)

  for tile in list(potentials):
    point = Point(tile[0], tile[1])
    if polygon.contains(point):
      inner.append(tile)
      potentials.remove(tile)

  print(inner)
  result = 0

  while not result == len(inner):
    result = len(inner)
    for tile in inner:

      if tile[0] > 0:
        if (tile[0] - 1, tile[1]) in potentials:
          inner.append((tile[0] - 1, tile[1]))
          potentials.remove((tile[0] - 1, tile[1]))
        if (tile[0]+1 < x_length):
          if (tile[0]+1, tile[1]) in potentials:
            inner.append((tile[0]+1, tile[1]))
            potentials.remove((tile[0]+1, tile[1]))
        if tile[1] > 0:
          if (tile[0], tile[1] - 1) in potentials:
            inner.append((tile[0], tile[1] - 1))
            potentials.remove((tile[0], tile[1] - 1))
        if (tile[1]+1 < y_length):
          if (tile[0], tile[1] + 1) in potentials:
            inner.append((tile[0], tile[1] + 1))
            potentials.remove((tile[0], tile[1] + 1))

  print("Inner: "+str(inner))
  print(len(inner))
  print(potentials)




def whatever():

  for pot in list(potentials):

    left = [a for a in stargrid[pot[0]][:pot[1]] if a == "*"]
    print(str(pot)+" has "+str(len(left))+" to the left.")
    if len(left) % 2:
      inner.append(pot)
      potentials.remove(pot)
    else:
      right = [a for a in stargrid[pot[0]][pot[1]:] if a == "*"]
      print(str(pot)+" has "+str(len(right))+" to the right.")
      if len(right) % 2:
        inner.append(pot)
        potentials.remove(pot)
      else:
        bottom = 0
        for x in range(pot[0],x_length):
          if x+1 < x_length and stargrid[x+1][pot[1]] == "*":
            bottom += 1
        print(str(pot)+" has "+str(bottom)+" underneath.")
        if bottom % 2:
          inner.append(pot)
          potentials.remove(pot)
        else:
          top = 0
          for x in range(0,pot[0]):
            if stargrid[x][pot[1]] == "*":
              top += 1
          print(str(pot)+" has "+str(top)+" on top.")
          if top % 2:
            inner.append(pot)
            potentials.remove(pot)

  print("Inner: "+str(inner))

  for tile in inner:

    if tile[0] > 0:
      if (tile[0] - 1, tile[1]) in potentials:
        inner.append((tile[0] - 1, tile[1]))
        potentials.remove((tile[0] - 1, tile[1]))
    if (tile[0]+1 < x_length):
      if (tile[0]+1, tile[1]) in potentials:
        inner.append((tile[0]+1, tile[1]))
        potentials.remove((tile[0]+1, tile[1]))
    if tile[1] > 0:
      if (tile[0], tile[1] - 1) in potentials:
        inner.append((tile[0], tile[1] - 1))
        potentials.remove((tile[0], tile[1] - 1))
    if (tile[1]+1 < y_length):
      if (tile[0], tile[1] + 1) in potentials:
        inner.append((tile[0], tile[1] + 1))
        potentials.remove((tile[0], tile[1] + 1))

  print("Inner: "+str(inner))
  print(potentials)



run_part1()
run_part2()
