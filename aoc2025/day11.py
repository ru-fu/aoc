import sys
from functools import cache

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

connections = dict()
  
with open(inputfile,"r") as input:

  for line in input:
    one = line.split(":")
    connections[one[0]] = one[1].strip().split(" ")

@cache
def find(fr):
  global connections

  result = 0
  
  if fr == "out":
    return 1
  else:
    for one in connections[fr]:
      result += find(one)
    return result

@cache
def find2(fr,dac = False, fft = False):
  global connections

  result = 0
  
  if (fr == "dac"):
    dac = True
  elif (fr == "fft"):
    fft = True
  
  if fr == "out":
    if dac and fft:
      return 1
    else:
      return 0
  else:
    for one in connections[fr]:
      result += find2(one,dac,fft)
    return result  

def run_part1():

  print(connections)
  print(find("you"))

def run_part2():

  print(find2("svr"))

#run_part1()
run_part2()
