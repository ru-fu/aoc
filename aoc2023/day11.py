import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

galaxies = []

def get_max(what):

  x_max = 0
  y_max = 0

  for one in what:
    if one[0] >= x_max:
      x_max = one[0] + 1
    if one[1] >= y_max:
      y_max = one[1] + 1

  return (x_max,y_max)

with open(inputfile,"r") as input:

  x = 0
  for line in input:
    for y,char in enumerate(line.strip()):
      if char == "#":
        galaxies.append((x,y))
    x += 1

  (x_max, y_max) = get_max(galaxies)


def visualize(what,x_max,y_max):

  for x in range(x_max):
    line = ""
    for y in range(y_max):
      if (x,y) in what:
        line += "#"
      else:
        line += "."
    print(line)

def expand(howmuch):

  global x_max, y_max

  doublex = []
  doubley = []

  for x in range(x_max):
    if len([gal for gal in galaxies if gal[0] == x]) == 0:
      doublex.append(x)

  for y in range(y_max):
    if len([gal for gal in galaxies if gal[1] == y]) == 0:
      doubley.append(y)

  #print(doublex)
  #print(doubley)

  expanded = []

  for gal in galaxies:
    addtox = len([d for d in doublex if d < gal[0]])
    addtoy = len([d for d in doubley if d < gal[1]])
    expanded.append((gal[0]+(howmuch*addtox),gal[1]+(howmuch*addtoy)))

  (new_x_max, new_y_max) = get_max(expanded)

  return (expanded,new_x_max,new_y_max)

def calc_path(pair):

  if pair[0][0] >= pair[1][0]:
    count = pair[0][0] - pair[1][0]
  else:
    count = pair[1][0] - pair[0][0]

  if pair[0][1] >= pair[1][1]:
    count += pair[0][1] - pair[1][1]
  else:
    count += pair[1][1] - pair[0][1]

  return count

def run_part1(x):

#  visualize(galaxies,x_max,y_max)

  (expanded,max_x,max_y) = expand(x)

#  visualize(expanded,max_x,max_y)

  pairs = [(a, b) for i, a in enumerate(expanded) for b in expanded[i + 1:]]

  result = []
  for pair in pairs:
    result.append(calc_path(pair))

  print(sum(result))

def run_part2():

  print("result")

run_part1(1)
run_part1(999999)
