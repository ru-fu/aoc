import sys
import math, numpy

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  times = [int(x) for x in input.readline()[5::].strip().split()]
  distances = [int(x) for x in input.readline()[9::].strip().split()]

def run(times,distances):

  lower = []
  upper = []
  wins = []

  for i, t in enumerate(times):
    lower.append((t - math.sqrt(t**2 - 4 * distances[i])) / 2)
    upper.append((t + math.sqrt(t**2 - 4 * distances[i])) / 2)


  for i, low in enumerate(lower):
    if int(low) == low:
      start = int(low) + 1
    else:
      start = math.ceil(low)
    if int(upper[i]) == upper[i]:
      end = int(upper[i]) - 1
    else:
      end = math.floor(upper[i])

    wins.append(1 + end - start)

  print(lower)
  print(upper)
  print(wins)
  print(numpy.prod(wins))

def run_part1():

  print(times)
  print(distances)

  run(times,distances)

def run_part2():

  with open(inputfile,"r") as input:

    times = [int(input.readline()[5::].strip().replace(" ",""))]
    distances = [int(input.readline()[9::].strip().replace(" ",""))]

  run(times,distances)

run_part1()
run_part2()
