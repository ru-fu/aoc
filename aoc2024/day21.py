import sys
import functools
sys.setrecursionlimit(150000)

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  codes = [line.rstrip() for line in input]

@functools.cache
def move_one_num(pos,one):

  #print(pos)
  #print(one)
  if one == "A":
    oneindex = 10
  else:
    oneindex = int(one)

  directions = []

  if pos == "A":
    # this is how to get from A to
    directions = [["<"],["^<<"],["<^"], ["^"], #0,1,2,3
                  ["^^<<"], #4
                  ["^^<"], ["^^"], #5,6
                  ["^^^<<"], #7
                  ["<^^^"],["^^^"],[""]] #8,9,A
  elif pos == "0":
    # this is how to get from 0 to
    directions = [[""],["^<"],["^"], ["^>"], #0,1,2,3
                  ["^^<"], #4
                  ["^^"], ["^^>"], #5,6
                  ["^^^<"], #7
                  ["^^^"],["^^^>"],[">"]] #8,9,A
  elif pos == "1":
    # this is how to get from 1 to
    directions = [[">v"],[""],[">"], [">>"], #0,1,2,3
                  ["^"], ["^>"], ["^>>"], #4, 5,6
                  ["^^"], ["^^>"], #7,8
                  ["^^>>"],[">>v"]] #9,A
  elif pos == "2":
    # this is how to get from 2 to
    directions = [["v"],["<"],[""],[">"],["<^"],["^"], #0,1,2,3,4,5
                  ["^>"],["<^^"],["^^"], #6,7,8
                  ["^^>"],["v>"]] #9,A
  elif pos == "3":
    # this is how to get from 3 to
    directions = [["<v"],["<<"],["<"],[""], #0,1,2,3
                  ["<<^"],["<^"],["^"], #4,5,6
                  ["<<^^"], #7
                  ["<^^"],["^^"],["v"]] #8,9,A
  elif pos == "4":
    # this is how to get from 4 to
    directions = [[">vv"],["v"],["v>"],["v>>"], #0,1,2,3
                  [""],[">"],[">>"],["^"],["^>"], #7,8
                  ["^>>"],[">>vv"]] #9,A
  elif pos == "5":
    # this is how to get from 5 to
    directions = [["vv"],["<v"],["v"],["v>"],["<"], #0,1,2,3,4
                  [""],[">"],["<^"],["^"],["^>"], #5,6,7,8,9
                  ["vv>"]] #A
  elif pos == "6":
    # this is how to get from 6 to
    directions = [["<vv"],["<<v"], #0,1
                  ["<v"],["v"],["<<"],["<"],[""], #2,3,4,5,6
                  ["<<^"],["<^"],["^"],["vv"]] #7,8,9,A
  elif pos == "7":
    # this is how to get from 7 to
    directions = [[">vvv"],["vv"],["<vv"], #0,1,2
                  ["vv>>"], #3
                  ["v"],["v>"],["v>>"],[""], #4,5,6,7
                  [">"],[">>"], #8,9
                  [">>vvv"]] #A
  elif pos == "8":
    # this is how to get from 8 to
    directions = [["vvv"],["<vv"],["vv"],["vv>"], #0,1,2,3
                  ["<v"],["v"],["v>"],["<"],[""],[">"], #4,5,6,7,8,9
                  ["vvv>"]] #A
  elif pos == "9":
    # this is how to get from 9 to
    directions = [["<vvv"], #0
                  ["<<vv"], #1
                  ["<vv"],["vv"],["<<v"], #2,3,4
                  ["<v"],["v"],["<<"],["<"],[""],["vvv"]] #5,6,7,8,9,A

  return [(x+"A",one) for x in directions[oneindex]][0]

@functools.cache
def move_one_dir(pos,one):

  if one == "^":
    oneindex = 0
  elif one == "A":
    oneindex = 1
  elif one == "<":
    oneindex = 2
  elif one == "v":
    oneindex = 3
  elif one == ">":
    oneindex = 4

  directions = []

  if pos == "^":
    # this is how to get from ^ to
    directions = [[""],[">"],["v<"],["v"],["v>"]] # ^,A,<,v,>
  elif pos == "A":
    # this is how to get from A to
    directions = [["<"],[""],["v<<"],["<v"],["v"]]
  elif pos == "<":
    # this is how to get from < to
    directions = [[">^"],[">>^"],[""],[">"],[">>"]]
  elif pos == "v":
    # this is how to get from v to
    directions = [["^"],["^>"],["<"],[""],[">"]]
  elif pos == ">":
    # this is how to get from > to
    directions = [["<^"],["^"],["<<"],["<"],[""]]

  return [(x+"A",one) for x in directions[oneindex]][0]

@functools.cache
def calc_sequence(sequence,step):

  #print("Sequence: "+sequence)
  #print("Step: "+str(step))

  # if there is something to process, do so

  if len(sequence) > 0:

    segments = sequence.split("A")
    segments = segments[:-1]

    total_length = 0

    for segment in segments:
      seq = ""
      segment += "A"
      pos = "A"
      #print("Segment: "+segment)

      for char in segment:
        (ins,pos) = move_one_dir(pos,char)
        seq += ins

      #print("Output for segment: "+seq)

      if step == 0:
        total_length += len(seq)
      else:
        total_length += calc_sequence(seq,step-1)

    return total_length

  else:
    return 0

def run(howoften):

  sequences = []
  total = []
  numbers = []
  lengths = []

  for code in codes:

    seq = ""
    pos = "A"

    for char in code:
      (ins,pos) = move_one_num(pos,char)
      seq += ins

    sequences.append(seq)

    numbers.append(int("".join([x for x in code if x.isdigit()])))

  for seq in sequences:
    lengths.append(calc_sequence(seq,howoften-1))

  print(sequences)

  for i,val in enumerate(lengths):
    total.append(val * numbers[i])

  return total

def run_part1():

  total = run(2)

  print(total)
  print(sum(total))

def run_part2():

  total = run(25)

  print(total)
  print(sum(total))


run_part1()
run_part2()


#295003095768390 too high (run(25))
#117757367217530 too low (run(24))
