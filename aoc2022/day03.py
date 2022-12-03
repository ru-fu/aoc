duplicates = []
allsets = []

with open("input03.txt","r") as input:

  for line in input:
    line = line.strip()
    left = line[:int(len(line)/2)]
    right = line[int(len(line)/2):]
    leftset = set(())
    leftset.update(left)
    rightset = set(())
    rightset.update(right)
    duplicates.append(leftset.intersection(rightset))

    full = set(())
    full.update(line)
    allsets.append(full)

def get_prio(setlist):

  outlist = []

  for x in setlist:
    for one in x:
      if one.isupper():
        outlist.append(ord(one)-38)
      else:
        outlist.append(ord(one)-96)

  return outlist

def run_part1():

  numbers = get_prio(duplicates)

  print(numbers)
  print(sum(numbers))

def run_part2():

  badges = []

  while len(allsets) > 2:
    one = allsets.pop(0)
    two = allsets.pop(0)
    three = allsets.pop(0)

    badges.append(one.intersection(two.intersection(three)))

  res = get_prio(badges)
  print(res)
  print(sum(res))

run_part1()
run_part2()
