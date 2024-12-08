import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

grid = []
max_x = 0
max_y = 0
antennas = {}
antinodes = set()
antinodes2 = set()

with open(inputfile,"r") as input:

  grid = [line.rstrip() for line in input]

  for i,x in enumerate(grid):
    for j, y in enumerate(x):
      if not y == ".":
        if y in antennas:
          antennas[y].append((i,j))
        else:
          antennas[y] = [(i,j)]

  max_x = len(grid)-1
  max_y = len(grid[0])-1

def find_antinodes(one,two):
  global antinodes
  difference = (one[0]-two[0], one[1]-two[1])
  new1 = (one[0]+difference[0],one[1]+difference[1])
  new2 = (two[0]-difference[0],two[1]-difference[1])

  if 0 <= new1[0] <= max_x and 0 <= new1[1] <= max_y:
    antinodes.add(new1)

  if  0 <= new2[0] <= max_x and 0 <= new2[1] <= max_y:
    antinodes.add(new2)

  print(str(one)+"//"+str(two)+"=>"+str(difference)+"=>"+str(new1)+"//"+str(new2))

def find_antinodes2(one,two):
  global antinodes2
  difference = (one[0]-two[0], one[1]-two[1])

  added = True
  i = -1

  while added:
    i += 1

    new1 = (one[0]+(difference[0]*i),one[1]+(difference[1]*i))
    new2 = (two[0]-(difference[0]*i),two[1]-(difference[1]*i))

    added = False

    if 0 <= new1[0] <= max_x and 0 <= new1[1] <= max_y:
      antinodes2.add(new1)
      added = True

    if  0 <= new2[0] <= max_x and 0 <= new2[1] <= max_y:
      antinodes2.add(new2)
      added = True


def run_part1():

#  for line in grid:
#    print(line)
  print(antennas)
  print(max_y)
  print(max_y)

  for fre in antennas:
    process = antennas[fre].copy()
    while len(process) > 1:
      first = process.pop(0)
      for pair in process:
        find_antinodes(first,pair)

  print(antinodes)
  print(len(antinodes))

def run_part2():

  for fre in antennas:
    process = antennas[fre].copy()
    while len(process) > 1:
      first = process.pop(0)
      for pair in process:
        find_antinodes2(first,pair)

  print(antinodes2)
  print(len(antinodes2))

#  for i,line in enumerate(grid):
#    pr = ""
#    for j,y in enumerate(line):
#      if (i,j) in antinodes2:
#        pr += "#"
#      else:
#        pr += y
#    print(pr)


run_part1()
run_part2()
