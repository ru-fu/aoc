import sys
import functools

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  codes = [line.rstrip() for line in input]

@functools.cache
def move_one_num(pos,one):

  if one == "A":
    oneindex = 10
  else:
    oneindex = int(one)

  directions = []

  if pos == "A":
    # this is how to get from A to
    directions = [["<"],["<^<","^<<"],["<^","^<"], ["^"], #0,1,2,3
                  ["<^<^","<^^<","^<<^","^<^<","^^<<"], #4
                  ["<^^","^<^","^^<"], ["^^"], #5,6
                  ["<^<^^","<^^<^","<^^^<","^<<^^","^<^<^","^<^^<","^^<<^","^^<^<","^^^<<"], #7
                  ["<^^^","^<^^","^^<^","^^^<"],["^^^"],[""]] #8,9,A
  elif pos == "0":
    # this is how to get from 0 to
    directions = [[""],["^<"],["^"], ["^>",">^"], #0,1,2,3
                  ["^<^","^^<"], #4
                  ["^^"], ["^^>","^>^",">^^"], #5,6
                  ["^<^^","^^<^","^^^<"], #7
                  ["^^^"],["^^^>","^^>^","^>^^",">^^^"],[">"]] #8,9,A
  elif pos == "1":
    # this is how to get from 1 to
    directions = [[">v"],[""],[">"], [">>"], #0,1,2,3
                  ["^"], ["^>",">^"], [">>^",">^>","^>>"], #4, 5,6
                  ["^^"], ["^^>","^>^",">^^"], #7,8
                  ["^^>>","^>^>","^>>^",">^>^",">^^>",">>^^"],[">>v",">v>"]] #9,A
  elif pos == "2":
    # this is how to get from 2 to
    directions = [["v"],["<"],[""],[">"],["<^","^<"],["^"], #0,1,2,3,4,5
                  ["^>",">^"],["<^^","^<^","^^<"],["^^"], #6,7,8
                  ["^^>","^>^",">^^"],["v>",">v"]] #9,A
  elif pos == "3":
    # this is how to get from 3 to
    directions = [["<v","v<"],["<<"],["<"],[""], #0,1,2,3
                  ["<<^","<^<","^<<"],["<^","^<"],["^"], #4,5,6
                  ["<<^^","<^<^","<^^<","^<<^","^<^<","^^<<"], #7
                  ["<^^","^<^","^^<"],["^^"],["v"]] #8,9,A
  elif pos == "4":
    # this is how to get from 4 to
    directions = [["v>v>",">vv"],["v"],["v>",">v"],["v>>",">v>",">>v"], #0,1,2,3
                  [""],[">"],[">>"],["^"],["^>",">^"], #7,8
                  ["^>>",">^>",">>^"],["v>v>","v>>v",">vv>",">v>v",">>vv"]] #9,A
  elif pos == "5":
    # this is how to get from 5 to
    directions = [["vv"],["<v","v<"],["v"],["v>",">v"],["<"], #0,1,2,3,4
                  [""],[">"],["<^","^<"],["^"],["^>",">^"], #5,6,7,8,9
                  ["vv>","v>v",">vv"]] #A
  elif pos == "6":
    # this is how to get from 6 to
    directions = [["vv<","v<v","<vv"],["v<<","<v<","<<v"], #0,1
                  ["<v","v<"],["v"],["<<"],["<"],[""], #2,3,4,5,6
                  ["<<^","<^<","^<<"],["<^","^<"],["^"],["vv"]] #7,8,9,A
  elif pos == "7":
    # this is how to get from 7 to
    directions = [["vv>v","v>vv",">vvv"],["vv"],["<vv","v>v","vv>"], #0,1,2
                  ["vv>>","v>v>","v>>v",">vv>",">v>v",">>vv"], #3
                  ["v"],[">v","v>"],["v>>",">v>",">>v"],[""], #4,5,6,7
                  [">"],[">>"], #8,9
                  ["vv>v>","vv>>v","v>vv>","v>v>v","v>>vv",">vvv>",">vv>v",">v>v>",">>vvv"]] #A
  elif pos == "8":
    # this is how to get from 8 to
    directions = [["vvv"],["vv<","v<v","<vv"],["vv"],["vv>","v>v",">vv"], #0,1,2,3
                  ["v<","<v"],["v"],["v>",">v"],["<"],[""],[">"], #4,5,6,7,8,9
                  ["vvv>","vv>v","v>vv",">vvv"]] #A
  elif pos == "9":
    # this is how to get from 9 to
    directions = [["vvv<","vv<v","v<vv","<vvv"], #0
                  ["vv<<","v<v<","v<<v","<v<v","<vv<","<<vv"], #1
                  ["vv<","v<v","<vv"],["vv"],["v<<","<v<","<<v"], #2,3,4
                  ["v<","<v"],["v"],["<<"],["<"],[""],["vvv"]] #5,6,7,8,9,A

  return [(x+"A",one) for x in directions[oneindex]]

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
    directions = [["<"],[""],["v<<","<v<"],["<v","v<"],["v"]]
  elif pos == "<":
    # this is how to get from < to
    directions = [[">^"],[">>^",">^>"],[""],[">"],[">>"]]
  elif pos == "v":
    # this is how to get from v to
    directions = [["^"],["^>",">^"],["<"],[""],[">"]]
  elif pos == ">":
    # this is how to get from > to
    directions = [["^<","<^"],["^"],["<<"],["<"],[""]]

  return [(x+"A",one) for x in directions[oneindex]]


def calc(which,sequence,options):

  if len(sequence) == 0:
    return options
  else:
    one = sequence[:1]
    sequence = sequence[1:]
    new_options = []
    if len(options) == 0:
      if (which == "numeric"):
        new_options = move_one_num("A",one)
      else:
        new_options = move_one_dir("A",one)
    else:
      for o in options:
        (output,pos) = o
        if (which == "numeric"):
          result = move_one_num(pos,one)
        else:
          result = move_one_dir(pos,one)
        #print(result)
        for r in result:
          (newout,newpos) = r
          new_options.append((output+newout,newpos))
    return calc(which,sequence,new_options)



def run_part1():

  lengths = []
  shortests = []
  numbers = []
  total = []

  for code in codes:
    number1 = calc("numeric",code,[])
    length = -1
    shortest = ""
    for one in number1:
      number2 = calc("directional",one[0],[])
      for two in number2:
        number3 = calc("directional",two[0],[])
        for three in number3:
          if length == -1 or len(three[0]) < length:
            length = len(three[0])
            shortest = three[0]

    shortests.append(shortest)
    lengths.append(length)
    numbers.append(int("".join([x for x in code if x.isdigit()])))

  print(shortests)
  print(lengths)
  print(numbers)

  for i,val in enumerate(lengths):
    total.append(val * numbers[i])

  print(total)
  print(sum(total))


def recurse(inp,step):

  options = []
  if step == 0:
    options = inp
  elif step == 26:
     options = recurse(calc("numeric",inp,[]),step-1)
  else:
    for one in inp:
      options += recurse(calc("directional",one[0],[]),step-1)

  return options

def run_part2():

  lengths = []
  total = []
  numbers = []

  for code in codes:

    length = -1

    for option in recurse(code,26):
      if length == -1 or len(option[0]) < length:
        length = len(option[0])

    lengths.append(length)
    numbers.append(int("".join([x for x in code if x.isdigit()])))

  print(lengths)
  for i,val in enumerate(lengths):
    total.append(val * numbers[i])

  print(total)
  print(sum(total))

#  for i,val in enumerate(lengths):
#    total.append(val * numbers[i])

#  print(total)
#  print(sum(total))


#run_part1()
run_part2()
