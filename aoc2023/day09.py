import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

histories = []

with open(inputfile,"r") as input:

  for line in input:
    histories.append([int(x) for x in line.strip().split()])

def get_next(history):

  current = history
  lasts = []
  count = 0
  nextline = []

  while nextline == [] or len([x for x in nextline if not x == 0]) > 0:
    count += 1
    nextline = []
    lasts.append(current[-1])
    first = current.pop(0)

    while current:
      second = current.pop(0)
      nextline.append(second - first)
      first = second

    current = nextline
    print("current: "+str(current))
    print(lasts)

  return sum(lasts)

def get_previous(history):

  current = history
  firsts = []
  nextline = []

  while nextline == [] or len([x for x in nextline if not x == 0]) > 0:
    nextline = []
    print(current)
    firsts.append(current[0])
    last = current.pop(-1)

    while current:
      second = current.pop(-1)
      nextline.append(last - second)
      last = second

    nextline.reverse()
    current = nextline
    print("current: "+str(current))

  firsts.reverse()
  print("firsts: "+str(firsts))
  result = 0
  for i in firsts:
    result = i - result

  return result

def run_part1():

  values = []
  histories1 = []
  for history in histories:
    histories1.append(list(history))
  for history in histories1:
    values.append(get_next(history))

  print(values)
  print(sum(values))

def run_part2():

  values = []

  for history in histories:
    values.append(get_previous(history))

  print(values)
  print(sum(values))

run_part1()
run_part2()
