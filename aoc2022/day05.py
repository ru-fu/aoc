import re

crates = []
cratestrings = []
instructions = []

regex = r"^move (\d+) from (\d+) to (\d+)$"

with open("input05.txt","r") as input:

  for line in input:
    if line.strip() == "":
      continue
    elif line.startswith("move"):
      ins = re.match(regex,line.strip())
      instructions.append(ins.groups())
    else:
      cratestrings.append(line)

cratestrings.reverse()

for line in cratestrings:
  count = 0
  while line:
    process = line[:4]
    line = line[4:]
    if process.strip().isnumeric():
      crates.append([])
    elif process and (not process == "    ") and (not process.startswith(" ")):
      crates[count].append(process[1])
    count += 1

def move(crates):

  for (num,fr,to) in instructions:
    num = int(num)-1
    fr = int(fr)-1
    to = int(to)-1
    while num >= 0:
      crate = crates[fr].pop()
      crates[to].append(crate)
      num -= 1

  return crates

def move2(crates):

  for (num,fr,to) in instructions:
    num = int(num)-1
    fr = int(fr)-1
    to = int(to)-1
    movingcrates = []
    while num >= 0:
      movingcrates.append(crates[fr].pop())
      num -= 1
    movingcrates.reverse()
    crates[to].extend(movingcrates)

  return crates

def run_part1():

  print(crates)
  print(instructions)
  newcrates =  [x[:] for x in crates]
  newcrates = move(newcrates)
  print(newcrates)

  message = ""
  for i in range(len(newcrates)):
    message += newcrates[i][-1]

  print(message)

def run_part2():

  newcrates =  [x[:] for x in crates]
  newcrates = move2(newcrates)
  print(newcrates)

  message = ""
  for i in range(len(newcrates)):
    message += newcrates[i][-1]

  print(message)

run_part1()
run_part2()
