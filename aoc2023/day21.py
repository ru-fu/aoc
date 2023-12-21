import sys
from functools import cache

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

rocks = set()
positions = set()

with open(inputfile,"r") as input:

  for x,line in enumerate(input):
    line = line.strip()
    for y,char in enumerate(line):
      if char == "#":
        rocks.add((x,y))
      elif char == "S":
        start = (x,y)

  max_x = x + 1
  max_y = len(line)

def visualize(positions):

  global rocks, max_x, max_y

  for x in range(max_x):
    line = ""
    for y in range(max_y):
      if (x,y) in rocks:
        line += "#"
      elif (x,y) in positions:
        line += "O"
      else:
        line += "."
    print(line)

  print()

@cache
def take_step(start,part):

  global rocks, max_x, max_y

  pos = [(start[0]-1,start[1]),
         (start[0]+1,start[1]),
         (start[0],start[1]-1),
         (start[0],start[1]+1)]
  new_pos = set()

  if part == 1:

    for p in pos:
      if p[0] >= 0 and p[0] < max_x and p[1] >= 0 and p[1] < max_y and not p in rocks:
        new_pos.add(p)

  elif part == 2:

    for p in pos:
        if p[0] < 0:
          new_x = p[0] % max_x
        elif p[0] > max_x:
          new_x = p[0] % max_x
        else:
          new_x = p[0]

        if p[1] < 0:
          new_y = p[1] % max_y
        elif p[1] > max_y:
          new_y = p[1] % max_y
        else:
          new_y = p[1]

        if not new_x >= 0 and new_x < max_x:
          print("NOOOOOOOOOOOO!")
        if not new_y >= 0 and new_y < max_y:
          print("AAAAAAAAARGH!")

        #if not p == (new_x, new_y):
        #  print(str(p)+" to "+str((new_x,new_y)))
        #  print(p[0] % max_x)

        if not (new_x,new_y) in rocks:
          new_pos.add(p)

  return new_pos

def take_steps(positions,part):

  new_pos = set()

  for pos in positions:
    new_pos.update(take_step(pos,part))

  return new_pos


def run_part1():

  global positions

  print(rocks)
  print(start)
  print(max_x)
  print(max_y)

  positions.add(start)

  for i in range(6):

    positions = take_steps(positions,1)

    #visualize(positions)
    #print(positions)

  print(len(positions))

def run_part2():

  p2 = set()
  p2.add(start)

  for i in range(327):

    p2 = take_steps(p2,2)

    if i == 64:
      print("65: "+str(len(p2)))
    elif i == 195:
      print("196: "+str(len(p2)))
    elif i == 326:
      print("327: "+str(len(p2)))

# ￼15181 x^2 + 15301 x + 3849 where x = (26501365 - 65) / 131
    #visualize(p2)

  print(len(p2))

#run_part1()
run_part2()
