import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

ranges = []
ingredients = set()
  
with open(inputfile,"r") as input:

  for line in input:
    if "-" in line:
      x = line.rstrip().split("-")
      ranges.append((int(x[0]),int(x[1])))
    elif len(line) > 1:
      ingredients.add(int(line.rstrip()))

def find(i):
  global ranges

  options = [(x,y) for (x,y) in ranges if x <= i and y >= i]

  #print(options)

  if len(options) > 0:
     return 1
  else:
    return 0
      
def run_part1():

  print(ranges)
  print(ingredients)

  count = 0

  for i in ingredients:
    if find(i):
      count += 1

  print(count)

def red(r):

  for (x,y) in r:

    options = [(a,b) for (a,b) in r if a <= x and b >= x]

    print("Looking for "+str((x,y)))
    print(options)

    if len(options) > 1:
      new = (min([a for (a,b) in options]),max([b for (a,b) in options]))
      print(new)
      for one in options:
        r.remove(one)
      r.append(new)
    
  return r

def count(r):

  lengths = [y-x+1 for (x,y) in r]

  return sum(lengths)
      
def run_part2():

  ranges_old = ranges

  while 1:
    ranges_new = red(ranges_old.copy())

    if len(ranges_new) == len(ranges_old):
      break
    else:
      ranges_old = ranges_new

  print(ranges_new)
  print(count(ranges_new))
      
run_part1()
run_part2()
