elves = []
directions = ["N","S","W","E"]

with open("input23.txt","r") as input:

  row = 0

  for line in input:
    for i,char in enumerate(line.strip()):
      if char == "#":
        elves.append((i,row))
    row += 1

def free_north(elfx,elfy,elves):
#  print("Free north "+str(elfx)+" "+str(elfy)+" "+str(elves))
#  print(not ((elfx-1,elfy-1) in elves or (elfx,elfy-1) in elves or (elfx+1,elfy-1) in elves))
  return not ((elfx-1,elfy-1) in elves or (elfx,elfy-1) in elves or (elfx+1,elfy-1) in elves)

def free_south(elfx,elfy,elves):
#  print("Free south "+str(elfx)+" "+str(elfy)+" "+str(elves))
#  print(not ((elfx-1,elfy+1) in elves or (elfx,elfy+1) in elves or (elfx+1,elfy+1) in elves))
  return not ((elfx-1,elfy+1) in elves or (elfx,elfy+1) in elves or (elfx+1,elfy+1) in elves)

def free_west(elfx,elfy,elves):
#  print("Free west "+str(elfx)+" "+str(elfy)+" "+str(elves))
#  print(not ((elfx-1,elfy-1) in elves or (elfx-1,elfy) in elves or (elfx-1,elfy+1) in elves))
  return not ((elfx-1,elfy-1) in elves or (elfx-1,elfy) in elves or (elfx-1,elfy+1) in elves)

def free_east(elfx,elfy,elves):
#  print("Free east "+str(elfx)+" "+str(elfy)+" "+str(elves))
#  print(not ((elfx+1,elfy-1) in elves or (elfx+1,elfy) in elves or (elfx+1,elfy+1) in elves))
  return not ((elfx+1,elfy-1) in elves or (elfx+1,elfy) in elves or (elfx+1,elfy+1) in elves)

def lonely(elfx,elfy,elves):
  return not (
    (elfx-1,elfy-1) in elves or
    (elfx,elfy-1) in elves or
    (elfx+1,elfy-1) in elves or
    (elfx-1,elfy) in elves or
    (elfx+1,elfy) in elves or
    (elfx-1,elfy+1) in elves or
    (elfx,elfy+1) in elves or
    (elfx+1,elfy+1) in elves
    )


def propose_moves(elves,direction):
  proposals = []
#  print(direction)
  for (elfx,elfy) in elves:
    if lonely(elfx,elfy,elves):
      proposals.append(None)
      continue
    if direction == "N":
      if free_north(elfx,elfy,elves):
        proposals.append((elfx,elfy-1))
        continue
      if free_south(elfx,elfy,elves):
        proposals.append((elfx,elfy+1))
        continue
      if free_west(elfx,elfy,elves):
        proposals.append((elfx-1,elfy))
        continue
      if free_east(elfx,elfy,elves):
        proposals.append((elfx+1,elfy))
        continue
      proposals.append(None)
    elif direction == "S":
      if free_south(elfx,elfy,elves):
        proposals.append((elfx,elfy+1))
        continue
      if free_west(elfx,elfy,elves):
        proposals.append((elfx-1,elfy))
        continue
      if free_east(elfx,elfy,elves):
        proposals.append((elfx+1,elfy))
        continue
      if free_north(elfx,elfy,elves):
        proposals.append((elfx,elfy-1))
        continue
      proposals.append(None)
    elif direction == "W":
      if free_west(elfx,elfy,elves):
        proposals.append((elfx-1,elfy))
        continue
      if free_east(elfx,elfy,elves):
        proposals.append((elfx+1,elfy))
        continue
      if free_north(elfx,elfy,elves):
        proposals.append((elfx,elfy-1))
        continue
      if free_south(elfx,elfy,elves):
        proposals.append((elfx,elfy+1))
        continue
      proposals.append(None)
    elif direction == "E":
      if free_east(elfx,elfy,elves):
        proposals.append((elfx+1,elfy))
        continue
      if free_north(elfx,elfy,elves):
        proposals.append((elfx,elfy-1))
        continue
      if free_south(elfx,elfy,elves):
        proposals.append((elfx,elfy+1))
        continue
      if free_west(elfx,elfy,elves):
        proposals.append((elfx-1,elfy))
        continue
      proposals.append(None)
    else:
      raise Exception("huh?")

  return proposals

def move(elves, proposals):
  new_elves = []
  for i,prop in enumerate(proposals):
    if prop == None or len([x for x in proposals if x == prop]) > 1:
      new_elves.append(elves[i])
    else:
      new_elves.append(prop)
  return new_elves

def find_empty(elves):
  xs = [x for (x,y) in elves]
  ys = [y for (x,y) in elves]

  total = (max(xs)-min(xs)+1) * (max(ys)-min(ys)+1)
#  print(xs)
#  print(ys)
#  print(total)
  return total - len(elves)

def run_part1():

  global elves, directions

  i = 0
  j = 0
  props = propose_moves(elves,directions[i])
  check = [x for x in props if x == None]

  while len(check) < len(props) and j < 10:
    elves = move(elves,props)
    j += 1
    i = j % 4
    props = propose_moves(elves,directions[i])
    check = [x for x in props if x == None]
#    print("Elves: "+str(elves))
#    print("Proposals: "+str(props))

  print(find_empty(elves))

def run_part2():

  global elves, directions

  i = 0
  j = 0
  props = propose_moves(elves,directions[i])
  check = [x for x in props if x == None]

  while len(check) < len(props):
    elves = move(elves,props)
    j += 1
    i = j % 4
    props = propose_moves(elves,directions[i])
    check = [x for x in props if x == None]
    print("Round: "+str(j)+" Nones: "+str(len(check)))
#    print("Elves: "+str(elves))
#    print("Proposals: "+str(props))

  print(j+1)

#run_part1()
run_part2()
