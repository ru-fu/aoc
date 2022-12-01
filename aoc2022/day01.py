elves = []

with open("input01.txt","r") as input:

  cals = 0
  for line in input:
    if (line.strip() == ""):
      elves.append(cals)
      cals = 0
    else:
      cals += int(line.strip())

  elves.append(cals)
  cals = 0

def run_part1():

   print(max(elves))

def run_part2():

  elves.sort(reverse=True)
  print(sum(elves[:3]))

run_part1()
run_part2()
