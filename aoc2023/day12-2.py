import sys
from functools import cache

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

@cache
def count_arrs(rec,cond,found):
  #print("rec: "+rec+" cond: "+str(cond)+" found: "+str(found))

  if rec == "":
    if cond == ():
      return 1
    elif len(cond) == 1 and cond[0] == found:
      return 1
    else:
      return 0

  if cond == ():
    if len([x for x in rec if x == "#"]) == 0:
      return 1
    else:
      return 0

  if rec[0] == ".":
    if found == 0:
      return count_arrs(rec[1:],cond,found)
    elif found == cond[0]:
      return count_arrs(rec[1:],cond[1:],0)
    else:
      return 0
  elif rec[0] == "#":
    if cond[0] >= found + 1:
      return count_arrs(rec[1:],cond,found+1)
    else:
      return 0
  elif rec[0] == "?":
    # Pick "."
    if found == 0:
      opt1 = count_arrs(rec[1:],cond,found)
    elif found == cond[0]:
      opt1 = count_arrs(rec[1:],cond[1:],0)
    else:
      opt1 = 0
    # Pick "#"
    if cond[0] >= found + 1:
      opt2 = count_arrs(rec[1:],cond,found+1)
    else:
      opt2 = 0

    return opt1 + opt2

  print("NOPE!!!!")


def run_part1():

  result = []

  for i,record in enumerate(records):
    print(str(i)+": "+record)
    potentials = count_arrs(record,tuple(conditions[i]),0)
    result.append(potentials)

  print(result)
  print(sum(result))

def expand(rec,cond):

  record = ""
  condition = []

  for i in range(5):
    record += rec + "?"
    condition += cond

  return (record[:-1], condition)

def run_part2():

  result = []

  for i,record in enumerate(records):
    (rec,cond) = expand(record,conditions[i])
#    print(rec)
#    print(cond)
    potentials = count_arrs(rec,tuple(cond),0)
    result.append(potentials)

  print(result)
  print(sum(result))

#run_part1()
run_part2()
