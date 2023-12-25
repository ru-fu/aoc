import sys
import numpy

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"


games = {}

with open(inputfile,"r") as input:

  for line in input:

    getgame = line.strip().split(": ")
    gameID = getgame[0][5:]

    getsets = getgame[1].split("; ")
    sets = []
    for oneset in getsets:
      getcubes = oneset.split(", ")
      cubes = {}
      for cube in getcubes:
        pair = cube.split(" ")
        cubes[pair[1]] = int(pair[0])
      sets.append(cubes)

    games[gameID] = sets

def run_part1():

  colors = {
    "red": 12,
    "green": 13,
    "blue": 14
    }

  IDs = []

  for game in games:
    ok = 1
    for oneset in games[game]:
      for color in colors:
        if color in oneset and oneset[color] > colors[color]:
          ok = 0
          break
    if ok:
      IDs.append(int(game))

  print(games)
  print(IDs)
  print(sum(IDs))

def run_part2():

  powers = []

  for game in games:

    colors = {
      "red": 0,
      "green": 0,
      "blue": 0
    }

    for oneset in games[game]:
      for color in colors:
        if color in oneset and oneset[color] > colors[color]:
          colors[color] = oneset[color]

    powers.append(numpy.prod(list(colors.values())))

  print(powers)
  print(sum(powers))

run_part1()
run_part2()
