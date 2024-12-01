import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

#  for line in input:
#  lines = [line.rstrip() for line in input]

def run_part1():

  print("result")

def run_part2():

  print("result")

run_part1()
run_part2()
