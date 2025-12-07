import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

splitters = set()

with open(inputfile,"r") as input:

  for r,line in enumerate(input):
    for c,col in enumerate(line.rstrip()):
      if line[c] == "S":
        start = (r,c)
      elif line[c] == "^":
        splitters.add((r,c))

  print(splitters)
  print(start)
  max_r = r
  max_c = c

splits = 0

def go_down(r,c):
  global splitters,splits

  if (r+1, c) in splitters:
    print("splitter "+str((r+1, c)))
    splits += 1
    return [c-1,c+1]
  else:
    print("new beam "+str((r+1,c)))
    return [c]

def run_part1():

  if not start[0] == 0:
    print("HEY! Not starting at the top!")
    exit

  beams = dict()
  beams[0] = {start[1]}

  for r in range(1,max_r+1):
    if not r in beams:
      beams[r] = set()
    for beam in beams[r-1]:
      beams[r].update(go_down(r-1,beam))

  print(beams)
  print(splits)

options = dict()

def calculate_options(s):
  global options, max_r, max_c, splitters

  if s in options:
    return options[s]
  else:
    result = 0
    next_l = (s[0],s[1]-1)
    while True:
      if next_l in splitters:
        result += calculate_options(next_l)
        break
      elif next_l[0] == max_r:
        result += 1
        break
      else:
        next_l = (next_l[0]+1,next_l[1])
    next_r = (s[0],s[1]+1)
    while True:
      if next_r in splitters:
        result += calculate_options(next_r)
        break
      elif next_r[0] == max_r:
        result += 1
        break
      else:
        next_r = (next_r[0]+1,next_r[1])
    return result

def run_part2():

  global options

  for s in sorted(splitters, reverse=True):
    res = calculate_options(s)
    options[s] = res


  print(options)

run_part1()
run_part2()
