import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

patternsr = []
maxr = []
maxc = []
score = 0

with open(inputfile,"r") as input:

  rows = {}
  count = 0
  for line in input:
    line = line.strip()
    if line == "":
      patternsr.append(rows)
      maxr.append(count - 1)
      rows = {}
      count = 0
    else:
      if line in rows:
        rows[line].append(count)
      else:
        rows[line] = [count]
      count += 1

  patternsr.append(rows)
  maxr.append(count - 1)

def check_rows(patterns,maximum,factor):

  global score

  remove = []

  for n,pattern in enumerate(patterns):

    pots = []

    for row in pattern.values():
      if len(row) > 1:
        for num in row:
          if num+1 in row:
            pots.append(num)

    for pot in pots:
      i = 1
      ok = 1
      while pot-i >= 0 and pot+i+1 <= maximum[n]:
        if len([x for x in pattern.values() if pot-i in x and pot+i+1 in x]) == 0:
          ok = 0
          break
        i += 1
      if ok:
        print("Found match: "+str(pot))
        score += factor * (pot+1)
        remove.append(pattern)

  for rem in remove:
    patterns.remove(rem)

def rotate(patterns):

  global maxc
  cols = []

  for pattern in patterns:

    newinput = []
    for i in range(len(list(pattern.keys())[0])):
      newinput.append("")

    x = 0
    while x >= 0:
      pat = [pat for pat,nums in pattern.items() if x in nums]
      if len(pat) == 1:
        for y,char in enumerate(pat[0]):
          newinput[y] += char
        x += 1
      else:
        x = -1

    print(newinput)

    rows = {}
    count = 0

    for line in newinput:

      if line in rows:
        rows[line].append(count)
      else:
        rows[line] = [count]
      count += 1

    cols.append(rows)
    maxc.append(count - 1)

  return cols

def run_part1():

  print(patternsr)
  print(maxr)

  check_rows(patternsr,maxr,100)

  patternsc = rotate(patternsr)

  print(patternsc)
  print(maxc)

  check_rows(patternsc,maxc,1)

  print(score)

def run_part2():

  print("result")

run_part1()
run_part2()
