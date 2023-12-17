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
  max_result = 0

  for x in range(x):
    max_result += vals[x][x]
    max_result += vals[x][x+1]
  print(max_result)
  print(max_x)
  print(max_y)


@cache
def move(start,direction,result):

 # print(result)

  global max_x, max_y, max_result, vals

  if result >= max_result:
    return max_result

  if start == (max_x - 1, max_y - 1):
    return result

  if len(direction) == 0:
    options = []
    if start[1] + 1 < max_y:
      options.append(move((start[0],start[1] + 1),">",result + vals[start[0]][start[1] + 1]))
    if start[1] - 1 >= 0:
      options.append(move((start[0],start[1] - 1),"<",result + vals[start[0]][start[1] - 1]))
    if start[0] + 1 < max_x:
      options.append(move((start[0] + 1,start[1]),"v",result + vals[start[0] + 1][start[1]]))
    if start[0] - 1 >= 0:
      options.append(move((start[0] - 1,start[1]),"^",result + vals[start[0] - 1][start[1]]))
    return min(options)
  elif len(direction) == 1:
    options = []
    if not direction == "<" and start[1] + 1 < max_y:
      newdir = ">"
      if direction == ">":
        newdir = ">>"
      options.append(move((start[0],start[1] + 1),newdir,result + vals[start[0]][start[1] + 1]))
    if not direction == ">" and start[1] - 1 >= 0:
      newdir = "<"
      if direction == "<":
        newdir = "<<"
      options.append(move((start[0],start[1] - 1),newdir,result + vals[start[0]][start[1] - 1]))
    if not direction == "^" and start[0] + 1 < max_x:
      newdir = "v"
      if direction == "v":
        newdir = "vv"
      options.append(move((start[0] + 1,start[1]),newdir,result + vals[start[0] + 1][start[1]]))
    if not direction == "v" and start[0] - 1 >= 0:
      newdir = "^"
      if direction == "^":
        newdir = "^^"
      options.append(move((start[0] - 1,start[1]),newdir,result + vals[start[0] - 1][start[1]]))
    return min(options)
  elif len(direction) == 2:
    options = []
    if not direction == "<<" and start[1] + 1 < max_y:
      newdir = ">"
      if direction == ">>":
        newdir = ">>>"
      options.append(move((start[0],start[1] + 1),newdir,result + vals[start[0]][start[1] + 1]))
    if not direction == ">>" and start[1] - 1 >= 0:
      newdir = "<"
      if direction == "<<":
        newdir = "<<<"
      options.append(move((start[0],start[1] - 1),newdir,result + vals[start[0]][start[1] - 1]))
    if not direction == "^^" and start[0] + 1 < max_x:
      newdir = "v"
      if direction == "vv":
        newdir = "vvv"
      options.append(move((start[0] + 1,start[1]),newdir,result + vals[start[0] + 1][start[1]]))
    if not direction == "vv" and start[0] - 1 >= 0:
      newdir = "^"
      if direction == "^^":
        newdir = "^^^"
      options.append(move((start[0] - 1,start[1]),newdir,result + vals[start[0] - 1][start[1]]))
    return min(options)
  elif len(direction) == 3:
    options = []
    if not direction == "<<<" and not direction == ">>>" and start[1] + 1 < max_y:
      options.append(move((start[0],start[1] + 1),">",result + vals[start[0]][start[1] + 1]))
    if not direction == ">>>" and not direction == "<<<" and start[1] - 1 >= 0:
      options.append(move((start[0],start[1] - 1),"<",result + vals[start[0]][start[1] - 1]))
    if not direction == "^^^" and not direction == "vvv" and start[0] + 1 < max_x:
      options.append(move((start[0] + 1,start[1]),"v",result + vals[start[0] + 1][start[1]]))
    if not direction == "vvv" and not direction == "^^^" and start[0] - 1 >= 0:
      options.append(move((start[0] - 1,start[1]),"^",result + vals[start[0] - 1][start[1]]))
    return min(options)
  else:
    print("NOOOOOOOOOOOOO!")
    return result + vals[start[0]][start[1]]

@cache
def move2(start,direction,result):

  global max_x, max_y, max_result, vals

  #print("Start: "+str(start)+" "+direction+" Result: "+str(result))

  if result >= max_result:
    return max_result

  if start == (0, 0):
    return result

  options = []
  if len(direction) == 0 or direction == "^" or direction == "v":
    if start[1] + 1 < max_y:
      options.append(move2((start[0],start[1] + 1),">",result + vals[start[0]][start[1] + 1]))
    if start[1] + 2 < max_y:
      options.append(move2((start[0],start[1] + 2),">",result + vals[start[0]][start[1] + 2] + vals[start[0]][start[1] + 1]))
    if start[1] + 3 < max_y:
      options.append(move2((start[0],start[1] + 3),">",result + vals[start[0]][start[1] + 3] + vals[start[0]][start[1] + 2] + vals[start[0]][start[1] + 1]))
    if start[1] - 1 >= 0:
      options.append(move2((start[0],start[1] - 1),"<",result + vals[start[0]][start[1] - 1]))
    if start[1] - 2 >= 0:
      options.append(move2((start[0],start[1] - 2),"<",result + vals[start[0]][start[1] - 2] + vals[start[0]][start[1] - 1]))
    if start[1] - 3 >= 0:
      options.append(move2((start[0],start[1] - 3),"<",result + vals[start[0]][start[1] - 3] + vals[start[0]][start[1] - 2] + vals[start[0]][start[1] - 1]))
  if len(direction) == 0 or direction == "<" or direction == ">":
    if start[0] + 1 < max_x:
      options.append(move2((start[0] + 1,start[1]),"v",result + vals[start[0] + 1][start[1]]))
    if start[0] + 2 < max_x:
      options.append(move2((start[0] + 2,start[1]),"v",result + vals[start[0] + 2][start[1]] + vals[start[0] + 1][start[1]]))
    if start[0] + 3 < max_x:
      options.append(move2((start[0] + 3,start[1]),"v",result + vals[start[0] + 3][start[1]] + vals[start[0] + 2][start[1]] + vals[start[0] + 1][start[1]]))
    if start[0] - 1 >= 0:
      options.append(move2((start[0] - 1,start[1]),"^",result + vals[start[0] - 1][start[1]]))
    if start[0] - 2 >= 0:
      options.append(move2((start[0] - 2,start[1]),"^",result + vals[start[0] - 2][start[1]] + vals[start[0] - 1][start[1]]))
    if start[0] - 3 >= 0:
      options.append(move2((start[0] - 3,start[1]),"^",result + vals[start[0] - 3][start[1]] + vals[start[0] - 2][start[1]] + vals[start[0] - 1][start[1]]))

  return min(options)

def run_part1():

 # print(move((0,0),"",0))
  print(move2((max_x-1,max_y-1),"",vals[max_x - 1][max_y - 1] - vals[0][0]))

def run_part2():

  print("result")

run_part1()
run_part2()
