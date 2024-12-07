import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

equations = []

with open(inputfile,"r") as input:

  for line in input:
    eq = line.rstrip().split(":")
    operands = [int(x) for x in eq[1].lstrip().split(" ")]
    operands.reverse()
    equations.append((int(eq[0]), operands))

def check(start):

  tocheck = [start]
  print(tocheck)

  while len(tocheck) > 0:
    eq = tocheck.pop(0)

    if len(eq[1]) > 1:

      if eq[0]/eq[1][0] == int(eq[0]/eq[1][0]):
        newresult = int(eq[0]/eq[1][0])
        tocheck.insert(0,(newresult,eq[1][1:]))
        if eq[0] - eq[1][0] > 0:
          tocheck.insert(1,(eq[0] - eq[1][0],eq[1][1:]))
      else:
        if eq[0] - eq[1][0] > 0:
          tocheck.insert(1,(eq[0] - eq[1][0],eq[1][1:]))

    else:
      if eq[0]/eq[1][0] == int(eq[0]/eq[1][0]) == 1:
        return True
      if eq[0] - eq[1][0] == 0:
        return True

  return False

def check2(start):

  tocheck = [start]
 # print(tocheck)

  while len(tocheck) > 0:
    eq = tocheck.pop(0)
    print(eq)

    if len(eq[1]) > 1:

      if eq[0]/eq[1][0] == int(eq[0]/eq[1][0]):
        newresult = int(eq[0]/eq[1][0])
        tocheck.insert(0,(newresult,eq[1][1:]))
        if eq[0] - eq[1][0] > 0:
          tocheck.insert(1,(eq[0] - eq[1][0],eq[1][1:]))
      else:
        if eq[0] - eq[1][0] > 0:
          tocheck.insert(1,(eq[0] - eq[1][0],eq[1][1:]))

      if str(eq[0]).endswith(str(eq[1][0])) and not eq[0] == eq[1][0]:
        tocheck.insert(1,(int(str(eq[0])[:-len(str(eq[1][0]))]),eq[1][1:]))

    else:
      if eq[0]/eq[1][0] == int(eq[0]/eq[1][0]) == 1:
        return True
      if eq[0] - eq[1][0] == 0:
        return True

  return False

nope = []
total1 = 0

def run_part1():
  global total1

  print(equations)

  for eq in equations:
    if check(eq):
      total1 += eq[0]
    else:
      nope.append(eq)

  print(total1)

def run_part2():
  global total1

  total2 = 0

  for eq in nope:
    if check2(eq):
      total2 += eq[0]
     # print("OK" + str(eq))

  print(total2)
  print(total1+total2)

run_part1()
run_part2()
