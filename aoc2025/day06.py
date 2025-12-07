import sys
import re
import math

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

numbers = []
numbers2 = []

with open(inputfile,"r") as input:

  for line in input:

    regex = r" *(.+?)\s+"
    nums = re.findall(regex,line)

    if nums[0].isdigit():
      numbers.append(list([int(x) for x in nums]))
      numbers2.append(line.rstrip()+" ")
    else:
      operators = list(nums)
      operators2 = line.rstrip()

def calculate(i):
  global numbers, operators

  nums = [x[i] for x in numbers]

  if operators[i] == "+":
    return sum(nums)
  else:
    return math.prod(nums)

def calculate2(i):
  global numbers2, operators2

  j = i

  newnums = []
  nums = ["dummy"]

  while len(nums) > 0:

    nums = [str(x[j]) for x in numbers2 if len(x) > j and x[j].isdigit()]
    if len(nums) > 0:
      newnums.append(int("".join([x for x in nums])))
    j += 1

  print(newnums)

  if operators2[i] == "+":
    return sum(newnums)
  else:
    return math.prod(newnums)

def run_part1():

  print(numbers)
  print(operators)

  result = []

  for i in range(len(operators)):
    result.append(calculate(i))

  print(result)
  print(sum(result))

def run_part2():

  result = []
  print(numbers2)
  print(operators2)

  for i in range(len(operators2)):
    if operators2[i] == "*" or operators2[i] == "+":
      result.append(calculate2(i))

  print(result)
  print(sum(result))

run_part1()
run_part2()
