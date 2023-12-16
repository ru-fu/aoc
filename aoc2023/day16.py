import sys

sys.setrecursionlimit(10000)

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

mirrors = {}
energized = {}

with open(inputfile,"r") as input:

  x = 0
  for line in input:
    line = line.strip()
    for y,char in enumerate(line):
      if not char == ".":
        if char == "\\":
          mirrors[(x,y)] = "B"
        else:
          mirrors[(x,y)] = char
    x +=1

  max_x = x
  max_y = y + 1

def visualize(which):

  global energized, mirrors

  for x in range(max_x):
    line = ""
    for y in range(max_y):
      if (which == "mirrors" or which == "all") and ((x,y) in mirrors):
        line += mirrors[(x,y)]
      elif which == "all" and (x,y) in energized:
        if len(energized[(x,y)]) == 1:
          line += energized[(x,y)][0]
        else:
          line += str(len(energized[(x,y)]))
      elif (x,y) in energized:
        line += "#"
      else:
        line += "."

    print(line)

  print()

def mark(start,direction):

  global mirrors, energized

  if start in energized:
    if not direction in energized[start]:
      energized[start].append(direction)
  else:
    energized[start] = [direction]

  if start in mirrors:
    if mirrors[start] == "B":
     if direction == ">":
       direction = "v"
     elif direction == "<":
       direction = "^"
     elif direction == "^":
       direction = "<"
     elif direction == "v":
       direction = ">"
    elif mirrors[start] == "/":
     if direction == ">":
       direction = "^"
     elif direction == "<":
       direction = "v"
     elif direction == "^":
       direction = ">"
     elif direction == "v":
       direction = "<"
    elif mirrors[start] == "-":
     if direction == "^" or direction == "v":
       direction = "<"
       mark(start,">")
    elif mirrors[start] == "|":
     if direction == "<" or direction == ">":
       direction = "^"
       mark(start,"v")

  if direction == ">":
    n = (start[0],start[1]+1)
  elif direction == "<":
    n = (start[0],start[1]-1)
  elif direction == "^":
    n = (start[0]-1,start[1])
  elif direction == "v":
    n = (start[0]+1,start[1])

  #print("Potential new: "+str(n))

  if 0 <= n[0] < max_x and 0 <= n[1] < max_y:
    if n in energized:
      if not direction in energized[n]:
        energized[n].append(direction)
        mark(n,direction)
    else:
      energized[n] = [direction]
      mark(n,direction)

  #print(energized)

def run_part1():

  start = (0,0)
  direction = ">"

  mark(start, direction)

  visualize("none")
  visualize("mirrors")
  visualize("all")

  #print(mirrors)
  print(len(energized))

def run_part2():

  results = []

  for x in range(max_x):
    energized.clear()
    mark((x,0),">")
    results.append(len(energized))

    energized.clear()
    mark((x,max_y - 1),"<")
    results.append(len(energized))

  for y in range(max_y):
    energized.clear()
    mark((0,y),"v")
    results.append(len(energized))

    energized.clear()
    mark((max_x - 1,y),"^")
    results.append(len(energized))


  print(results)
  print(max(results))

#run_part1()
run_part2()
