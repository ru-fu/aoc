import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

list1 = []
list2 = []

with open(inputfile,"r") as input:

  for line in input:
    (a,b) = line.rstrip().rsplit(" ",1)
    list1.append(int(a.rstrip()))
    list2.append(int(b))

def run_part1():

  list1.sort()
  list2.sort()

  distances = []
  for i, val in enumerate(list1):
    distances.append(abs(list2[i]-val))

  print(list1)
  print(list2)
  print(distances)
  print(sum(distances))

def run_part2():

  cache = {}
  score = 0

  for val in list1:
    if val in cache:
      score += cache[val]
    else:
      cache[val] = val * len([x for x in list2 if x == val])
      score += cache[val]
    #print(score)

  print(cache)
  print(score)

run_part1()
run_part2()
