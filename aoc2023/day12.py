import sys
import exrex, re

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

records = []
conditions = []

with open(inputfile,"r") as input:

  for line in input:
    both = line.strip().split()
    records.append(both[0])
    conditions.append([int(x) for x in both[1].split(",")])

def gen_arrs(record,condition,lineno):

  expression = ""
  for char in record:
    if char == ".":
      expression += "o"
    elif char == "#":
      expression +="X"
    elif char == "?":
      expression += "[oX]"

  regex = "^o*"
  for num in condition:
    for i in range(num):
      regex += "X"
    regex += "o+"

  regex = regex[:-1]+"*$"
  print(str(lineno)+": "+regex)
  pattern = re.compile(regex)

  potentials = []

  for pot in exrex.generate(expression):
    if pattern.match(pot):
      potentials.append(pot)

  return potentials

def run_part1():

  result = []

  for i,record in enumerate(records):
    potentials = gen_arrs(record,conditions[i],i)
    result.append(len(potentials))

  print(result)
  print(sum(result))

def expand(rec,cond):

  record = ""
  condition = []

  for i in range(5):
    record += rec
    condition += cond

  return (record, condition)

def run_part2():

  result = []

  for i,record in enumerate(records):
    (rec,cond) = expand(record,conditions[i])
    print(rec)
    print(cond)
    potentials = gen_arrs(rec,cond,i)
    result.append(len(potentials))

  print(result)
  print(sum(result))

#run_part1()
run_part2()
