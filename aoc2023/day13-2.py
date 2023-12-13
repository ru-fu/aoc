import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

patterns = []
scores1 = []
foundhow1 = []

with open(inputfile,"r") as input:

  pattern = []

  for line in input:
    line = line.strip()
    if line == "":
      patterns.append(pattern)
      pattern = []
    else:
      pattern.append(line)

  patterns.append(pattern)
  print(patterns)


def check(pattern,maximum,factor,how,elim):
  pots = []

  for row in pattern.values():
    if len(row) > 1:
      for num in row:
        if num+1 in row:
          pots.append(num)

  for pot in pots:
    i = 1
    ok = 1
    while pot-i >= 0 and pot+i+1 <= maximum:
      if len([x for x in pattern.values() if pot-i in x and pot+i+1 in x]) == 0:
        ok = 0
        break
      i += 1
    if ok:
      if elim and elim == (how,pot):
        continue
      else:
        #print("Found match: "+str(pot))
        return ((how,pot),factor * (pot+1))

  return (("N",-1),0)

def collect(pattern):

  rows = {}
  count = 0

  for line in pattern:

    if line in rows:
      rows[line].append(count)
    else:
      rows[line] = [count]
    count += 1

  maximum = count - 1

  return (rows,maximum)

def check_one(pattern,elim):

  (rows, maximum) = collect(pattern)

  # Check horizontal reflection
  (which, result) = check(rows,maximum,100,"H",elim)
  if result > 0:
    return (which, result)

  # Rotate
  rotated = []
  for i in range(len(list(pattern[0]))):
    rotated.append("")

  x = 0
  while x >= 0:
    pat = [pat for pat,nums in rows.items() if x in nums]
    if len(pat) == 1:
      for y,char in enumerate(pat[0]):
        rotated[y] += char
      x += 1
    else:
      x = -1

  (cols, maximum) = collect(rotated)

  # Check vertical reflection
  (which, result) = check(cols,maximum,1,"V",elim)
  if result > 0:
    return (which, result)


  return (("N",-1),0)

def visualize(pattern):

  for line in pattern:
    print(line)

def run_part1():

  for pattern in patterns:
    (which,result) = check_one(pattern,None)
    foundhow1.append(which)
    scores1.append(result)

  print(scores1)
  print(len(scores1))
  print(foundhow1)
  print(sum(scores1))

def run_part2():

  scores = []
  foundhow2 = []

  for p,pattern in enumerate(patterns):

    alloptions = []

    for x in range(len(pattern)):
      for y in range(len(pattern[x])):
        new = list(pattern)
        if pattern[x][y] == ".":
          new[x] = pattern[x][:y]+"#"+pattern[x][y+1:]
        else:
          new[x] = pattern[x][:y]+"."+pattern[x][y+1:]
        alloptions.append(new)

    foundone = 0
    for option in alloptions:
      #visualize(option)
      #print()

      (which,result) = check_one(option,foundhow1[p])
      if result > 0 and not which == foundhow1[p]:
        foundone = 1
        scores.append(result)
        foundhow2.append(which)
        break

    if not foundone:
      print("NOOOOOOO!")
      visualize(pattern)
      print()
      visualize(alloptions[0])

  print(scores)
  print(len(scores))
  print(foundhow2)
  print(sum(scores))


run_part1()
run_part2()
