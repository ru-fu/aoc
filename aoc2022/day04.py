assignments = []
containment = []
intersection = []

with open("input04.txt","r") as input:

  for line in input:
    elves = line.strip().split(",")
    elfsets = []
    for elf in elves:
      info = elf.split("-")
      elfset = set(())
      elfset.update(range(int(info[0]),int(info[1])+1))
      elfsets.append(elfset)

    assignments.append(elfsets)

for a in assignments:

  if a[0].issubset(a[1]) or a[1].issubset(a[0]):
    containment.append(1)
  else:
    containment.append(0)

  if len(a[0].intersection(a[1])) == 0:
    intersection.append(0)
  else:
    intersection.append(1)


def run_part1():

   print(sum(containment))

def run_part2():

   print(sum(intersection))

run_part1()
run_part2()
