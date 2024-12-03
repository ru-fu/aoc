import sys
import re

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

memory = ""
  
with open(inputfile,"r") as input:

  for line in input:
    memory += line.rstrip()

def run_part1():

  regex = r"mul\(\d\d?\d?,\d\d?\d?\)"

  ins = re.findall(regex,memory)

  total = 0
  
  for one in ins:
    factors = one[4:-1].split(",")
    total += int(factors[0]) * int(factors[1])

 # print(memory)
  print(total)

def run_part2():
  regex = r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)"

  ins = re.findall(regex,memory)

  total = 0
  process = 1
  
  for one in ins:
    if one.startswith("don't"):
      process = 0
    elif one.startswith("do"):
      process = 1
    elif process:
        factors = one[4:-1].split(",")
        total += int(factors[0]) * int(factors[1])

  print(total)

run_part1()
run_part2()
