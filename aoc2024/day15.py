import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

robot = None
robot2 = None
boxes = []
boxopen = []
boxclose = []
walls = []
walls2 = []
instructions = ""
max_x = 0
max_x2 = 0
max_y = 0
max_y2 = 0

with open(inputfile,"r") as input1:

  ins = False
  x = 0

  for line in input1:
    line = line.rstrip()
    if len(line) == 0:
      ins = True
      max_x = x - 1
      max_x2 = x -1
    if not ins:
      y2 = 0
      for y,val in enumerate(line):
        if val == "#":
          walls.append((x,y))
          walls2.append((x,y2))
          walls2.append((x,y2+1))
        elif val == "O":
          boxes.append((x,y))
          boxopen.append((x,y2))
          boxclose.append((x,y2+1))
        elif val == "@":
          robot = (x,y)
          robot2 = (x,y2)

        y2 += 2

        if y > max_y:
          max_y = y

        if y2 > max_y2:
          max_y2 = y2
      x += 1
    else:
      instructions += line


def visualize(which=1):
  global walls,walls2,boxes,boxopen,boxclose,robot,robot2

  if which == 1:
    for x in range(max_x+1):
      row = ""
      for y in range(max_y+1):
        if (x,y) in walls:
          row += "#"
        elif (x,y) in boxes:
          row += "O"
        elif (x,y) == robot:
          row += "@"
        else:
          row += "."
      print(row)
  else:
    for x in range(max_x2+1):
      row = ""
      for y in range(max_y2+1):
        if (x,y) in walls2:
          row += "#"
        elif (x,y) in boxopen:
          row += "["
        elif (x,y) in boxclose:
          row += "]"
        elif (x,y) == robot2:
          row += "@"
        else:
          row += "."
      print(row)

def move(direction):
  global walls, boxes, robot

  print("Move "+direction)

  (x,y) = robot

  find = True

  while find:

    if direction == "<":
      emptyfield = (x,y-1)
    elif direction == ">":
      emptyfield = (x,y+1)
    elif direction == "^":
      emptyfield = (x-1,y)
    elif direction == "v":
      emptyfield = (x+1,y)

    if (0 <= emptyfield[0] <= max_x and
        0 <= emptyfield[1] <= max_y):
      if emptyfield in boxes:
        x = emptyfield[0]
        y = emptyfield[1]
      elif emptyfield in walls:
        return
      else:
        find = False

  #print(emptyfield)

  if direction == "<":
    moveto = (robot[0],robot[1]-1)
  elif direction == ">":
    moveto = (robot[0],robot[1]+1)
  elif direction == "^":
    moveto = (robot[0]-1,robot[1])
  elif direction == "v":
    moveto = (robot[0]+1,robot[1])

  #print(moveto)

  if not moveto == emptyfield:
    boxes.remove(moveto)
    boxes.append(emptyfield)

  robot = moveto

def move2(direction):
  global walls2, boxopen, boxclose, robot2, max_x2, max_y2

  print("Move "+direction)

  moves = {}

  (x,y) = robot2

  if direction == "<" or direction == ">":

    find = True

    while find:
      #print(str(x)+"  "+str(y))
      if direction == "<":
        emptyfield = (x,y-1)
      elif direction == ">":
        emptyfield = (x,y+1)

      if 0 <= emptyfield[1] <= max_y2:
        if emptyfield in boxclose:
          moves[(x,y)]=emptyfield
          x = emptyfield[0]
          y = emptyfield[1]
        elif emptyfield in boxopen:
          moves[(x,y)]=emptyfield
          x = emptyfield[0]
          y = emptyfield[1]
        elif emptyfield in walls2:
          return
        else:
          moves[(x,y)]=emptyfield
          find = False

      #print(emptyfield)

  elif direction == "v":

    check = [((x,y),(x+1,y))]

    while len(check) > 0:

      current = check.pop(0)
      tocheck = current[1]

      if (0 <= tocheck[0] <= max_x2 and
          0 <= tocheck[1] <= max_y2):
        if tocheck in boxclose:
            moves[current[0]]=tocheck
            check.append((tocheck,(tocheck[0]+1,tocheck[1])))
            check.append(((tocheck[0],tocheck[1]-1),(tocheck[0]+1,tocheck[1]-1)))
        elif tocheck in boxopen:
            moves[current[0]]=tocheck
            check.append((tocheck,(tocheck[0]+1,tocheck[1])))
            check.append(((tocheck[0],tocheck[1]+1),(tocheck[0]+1,tocheck[1]+1)))
        elif tocheck in walls2:
          return
        else:
            moves[current[0]]=tocheck

  elif direction == "^":

    check = [((x,y),(x-1,y))]

    while len(check) > 0:

      current = check.pop(0)
      tocheck = current[1]


      if (0 <= tocheck[0] <= max_x2 and
          0 <= tocheck[1] <= max_y2):
        if tocheck in boxclose:
            moves[current[0]]=tocheck
            check.append((tocheck,(tocheck[0]-1,tocheck[1])))
            check.append(((tocheck[0],tocheck[1]-1),(tocheck[0]-1,tocheck[1]-1)))
        elif tocheck in boxopen:
            moves[current[0]]=tocheck
            check.append((tocheck,(tocheck[0]-1,tocheck[1])))
            check.append(((tocheck[0],tocheck[1]+1),(tocheck[0]-1,tocheck[1]+1)))
        elif tocheck in walls2:
          return
        else:
            moves[current[0]]=tocheck



  for fr,to in reversed(moves.items()):
    if True: #direction == "<" or direction == ">":
      if fr in boxopen:
        boxopen.remove(fr)
        boxopen.append(to)
      elif fr in boxclose:
        boxclose.remove(fr)
        boxclose.append(to)
      elif fr == robot2:
        robot2 = to


  print(moves)

  #robot2 = moveto


def run_part1():

  print(boxes)
  print(walls)
  print(robot)
  print(instructions)
  print(max_x)
  print(max_y)

  for ins in instructions:
    move(ins)
    #visualize()
    #input()

  coords = [100 * x + y for (x,y) in boxes]
  print(coords)
  print(sum(coords))

def run_part2():

  print(max_y2)
  visualize(2)

  for ins in instructions:
    move2(ins)
  #  visualize(2)
  #  input()

  coords = [100 * x + y for (x,y) in boxopen]
  print(coords)
  print(sum(coords))

run_part1()
run_part2()
