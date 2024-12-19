import sys
import functools

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

designs = []
  
with open(inputfile,"r") as input:

  for line in input:
    line = line.rstrip()
    if "," in line:
      towels = sorted(line.split(", "), key=len)
    elif len(line) > 0:
      designs.append(line)

@functools.cache
def find(pattern):
  global towels

  #print(pattern)

  if len(pattern) == 0:
    return 1

  for t in towels:
    if pattern.startswith(t):
      if find(pattern[len(t):]):
        return 1

  return 0


@functools.cache
def count(pattern):
  global towels

  #print(pattern)

  result = 0

  if len(pattern) == 0:
    return 1

  for t in towels:
    if pattern.startswith(t):
      result += count(pattern[len(t):])
      
  return result
    
    
def run_part1():

  result = []

  for d in designs:
    result.append(find(d))
    print(result)

  print(result)
  print(sum(result))

def run_part2():

  result = []

  for d in designs:
    result.append(count(d))
    print(result)

  print(result)
  print(sum(result))

run_part1()
run_part2()
