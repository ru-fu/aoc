import ast
from functools import cmp_to_key

pairs = []
signals = []

with open("input13.txt","r") as input:

  line = input.readline()

  while(line):
    if line.strip():
      list1 = ast.literal_eval(line.strip())
      signals.append(list1)
      line = input.readline()
      list2 = ast.literal_eval(line.strip())
      signals.append(list2)
      line = input.readline()
      pairs.append((list1,list2))
    else:
      line = input.readline()

def compare(left,right,indent = ""):
  print(indent+"Compare "+str(left)+" vs "+str(right))
  if isinstance(left, int) and isinstance(right, int):
    if left < right:
      print(indent+"Left side is smaller, so inputs are in the right order")
      return 1
    elif left > right:
      print(indent+"Right side is smaller, so inputs are not in the right order")
      return -1
    else:
      return 0
  elif isinstance(left, list) and isinstance(right, list):
    for i,l in enumerate(left):
      if i >= len(right):
        print(indent+"Right side ran out of items, so inputs are not in the right order")
        return -1
      else:
        res = compare(left[i],right[i],indent+"  ")
        if res == 1 or res == -1:
          return res
    if len(left) == len(right):
      return 0
    else:
      print(indent+"Left side ran out of items, so inputs are in the right order")
      return 1
  elif isinstance(left, int) and isinstance(right, list):
    return compare([left],right,indent+"  ")
  elif isinstance(left, list) and isinstance(right, int):
    return compare(left,[right],indent+"  ")

def run_part1():

  correct = []
  correctsum = 0

  for pair in pairs:
    res = compare(pair[0],pair[1],"")
    if res == 1:
      correct.append(True)
    else:
      correct.append(False)

  for i,x in enumerate(correct):
    if x:
      correctsum += i+1

  print(correct)
  print(correctsum)

def run_part2():

  signals.append([[2]])
  signals.append([[6]])

  sortedlist = sorted(signals, key=cmp_to_key(compare))
  sortedlist.reverse()
  print(sortedlist)

  deckey = 1

  for i,x in enumerate(sortedlist):
    if x == [[2]] or x == [[6]]:
      deckey = deckey * (i+1)

  print(deckey)

run_part1()
run_part2()
