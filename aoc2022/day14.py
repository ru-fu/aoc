themap = {}

with open("input14.txt","r") as input:

  for line in input:
    coords = line.strip().split(" -> ")
    for i,x in enumerate(coords):
      if i+1 < len(coords):
        coord1 = [int(c) for c in x.split(",")]
        coord2 = [int(c) for c in coords[i+1].split(",")]
        if coord1[0] == coord2[0]:
          if coord1[1] < coord2[1]:
            for j in range(coord1[1],coord2[1]+1):
              themap[(coord1[0],j)] = "#"
          else:
            for j in range(coord2[1],coord1[1]+1):
              themap[(coord1[0],j)] = "#"
        elif coord1[1] == coord2[1]:
          if coord1[0] < coord2[0]:
            for j in range(coord1[0],coord2[0]+1):
              themap[(j,coord1[1])] = "#"
          else:
            for j in range(coord2[0],coord1[0]+1):
              themap[(j,coord1[1])] = "#"
        else:
          raise Exception("huh?")

  maxdepth = max([x[1] for x in themap])

def fall(start = (500,0)):
  global maxdepth
  if start[1] > maxdepth:
    return "thevoid"
  if (start[0],start[1]+1) in themap:
    if (start[0]-1,start[1]+1) in themap:
      if (start[0]+1,start[1]+1) in themap:
        themap[start] = "o"
        return start
      else:
        return fall((start[0]+1,start[1]+1))
    else:
      return fall((start[0]-1,start[1]+1))
  else:
    return fall((start[0],start[1]+1))

def fall2(start = (500,0)):
  global maxdepth
  if (500,0) in themap:
    return "done"
  if start[1]+1 == maxdepth+2 or (start[0],start[1]+1) in themap:
    if start[1]+1 == maxdepth+2 or (start[0]-1,start[1]+1) in themap:
      if start[1]+1 == maxdepth+2 or (start[0]+1,start[1]+1) in themap:
        themap[start] = "o"
        return start
      else:
        return fall2((start[0]+1,start[1]+1))
    else:
      return fall2((start[0]-1,start[1]+1))
  else:
    return fall2((start[0],start[1]+1))


def run_part1():

  result = 0
  while not result == "thevoid":
    result = fall()

  print(themap)
  print(len([x for x in themap if themap[x] == "o"]))

def run_part2():

  result = 0
  while not result == "done":
    result = fall2()

  print(themap)
  print(len([x for x in themap if themap[x] == "o"]))

run_part1()
run_part2()
