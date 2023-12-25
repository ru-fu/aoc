import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

rocks = []
blocks = []
max_x = 0
max_y = 0

with open(inputfile,"r") as input:

  x = 0

  for line in input:
    line = line.strip()
    for y, char in enumerate(line):
      if char == "O":
        rocks.append((x,y))
      elif char == "#":
        blocks.append((x,y))
    x += 1

  max_x = x
  max_y = len(line)

x_blocks = []
x_blocks_rev = []
y_blocks = []
y_blocks_rev = []

for x in range(max_x):
  l = [b2 for (b1,b2) in blocks if b1 == x]
  l.sort()
  x_blocks.append(list(l))
  l.sort(reverse=True)
  x_blocks_rev.append(list(l))
for y in range(max_y):
  l = [b1 for (b1,b2) in blocks if b2 == y]
  l.sort()
  y_blocks.append(list(l))
  l.sort(reverse=True)
  y_blocks_rev.append(list(l))




def visualize(rocks):

  global blocks, max_x, max_y

  for x in range(max_x):
    line = ""
    for y in range(max_y):
      if (x,y) in rocks:
        line += "O"
      elif (x,y) in blocks:
        line += "#"
      else:
        line += "."
    print(line)

  print()

def find_lowest_block(y_blocks,lowest):

  global max_y

  higher = [b for b in y_blocks if b > lowest]
  #print(y_blocks,higher)

  if len(higher) > 0:
    lowest_block = higher[0]
    while lowest_block + 1 in higher:
      lowest_block += 1
  else:
    lowest_block = max_y + 1

  #print("Lowest block for lowest "+str(lowest))
  #print(y_blocks)
  #print(lowest_block)

  return lowest_block

def find_highest_block(y_blocks,highest):

  lower = [b for b in y_blocks if b < highest]

  if len(lower) > 0:
    highest_block = lower[0]
    while highest_block - 1 in lower:
      highest_block = highest_block - 1
  else:
    highest_block = 0

  #print("Highest block for column "+str(col))
  #print(highest_block)

  return highest_block

def tilt(rocks,direction):

  global blocks, x_blocks, x_blocks_rev, y_blocks, y_blocks_rev

  new_rocks = []

  if direction == "N":

    for y in range(max_y):
      lowest = 0
      lowest_block = find_lowest_block(y_blocks[y],-1)
      y_rocks = [r for r in rocks if r[1] == y]
      y_rocks.sort()
      for rock in y_rocks:
#        print("Checking rock "+str(rock))
        while rock[0] > lowest_block:
          lowest = lowest_block + 1
          lowest_block = find_lowest_block(y_blocks[y],lowest)

        if rock[0] == lowest:
          new_rocks.append(rock)
          lowest += 1
        else:
          new_rocks.append((lowest,rock[1]))
          lowest += 1

  elif direction == "S":

    for y in range(max_y):
      highest = max_y - 1
      highest_block = find_highest_block(y_blocks_rev[y],max_y)
      y_rocks = [r for r in rocks if r[1] == y]
      y_rocks.sort(reverse=True)
      for rock in y_rocks:
        #print("Checking rock "+str(rock))
        while rock[0] < highest_block:
          highest = highest_block - 1
          highest_block = find_highest_block(y_blocks_rev[y],highest)

        if rock[0] == highest:
          new_rocks.append(rock)
          highest = highest - 1
        else:
          new_rocks.append((highest,rock[1]))
          highest = highest - 1

  elif direction == "W":

    for x in range(max_x):
      lowest = 0
      lowest_block = find_lowest_block(x_blocks[x],-1)
      x_rocks = [r for r in rocks if r[0] == x]
      x_rocks.sort()
      for rock in x_rocks:
       # print("Checking rock "+str(rock))
        while rock[1] > lowest_block:
          lowest = lowest_block + 1
          lowest_block = find_lowest_block(x_blocks[x],lowest)

        if rock[1] == lowest:
          new_rocks.append(rock)
          lowest += 1
        else:
          new_rocks.append((rock[0],lowest))
          lowest += 1

  elif direction == "E":

    for x in range(max_x):
      highest = max_x - 1
      highest_block = find_highest_block(x_blocks_rev[x],max_y)
      x_rocks = [r for r in rocks if r[0] == x]
      x_rocks.sort(reverse=True)
      for rock in x_rocks:
        #print("Checking rock "+str(rock))
        while rock[1] < highest_block:
          highest = highest_block - 1
          highest_block = find_highest_block(x_blocks_rev[x],highest)

        if rock[1] == highest:
          new_rocks.append(rock)
          highest = highest - 1
        else:
          new_rocks.append((rock[0],highest))
          highest = highest - 1

  return new_rocks

def score(rocks):

  global blocks

  result = 0
  for x in range(max_x):
    new = len([r for r in rocks if r[0] == x]) * (max_x - x)
    #print(new)
    result += new

  return result


def cycle(rocks):

  rocks =  tilt(list(rocks),"N")
  rocks =  tilt(list(rocks),"W")
  rocks =  tilt(list(rocks),"S")
  rocks =  tilt(list(rocks),"E")

  return rocks

def run_part1():

  global rocks
  rocks1 = list(rocks)

  #print("Rocks: "+str(rocks1))
  #print("Blocks: "+str(blocks))
  visualize(rocks1)

  rocks1 = tilt(list(rocks1),"N")
  visualize(rocks1)

  result = score(rocks1)

  print(result)

def run_part2():

  global rocks
  rocks2 = list(rocks)

  visualize(rocks2)

  cache = []

  howmany = 1000000000
  for i in range(howmany):
    if i % 100000 == 0:
      print(i)
    rocks2 = cycle(rocks2)
    if rocks2 in cache:
      print("FOUND IT! "+str(i))
      j = cache.index(rocks2)
      break
    else:
      cache.append(rocks2)

  visualize(rocks2)


  which = ((howmany - j - 1) % (i - j)) + j
  print(which)
  result = score(cache[which])

  print(result)


#run_part1()
run_part2()
