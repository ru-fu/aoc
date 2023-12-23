import sys

sys.setrecursionlimit(100000)
# ulimit -s  16000


inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

forest = []
slopes = {"up": [],
          "down": [],
          "right": [],
          "left":[]}

with open(inputfile,"r") as input:

  for x,line in enumerate(input):
    line = line.strip()
    for y, char in enumerate(line):
      if char == "#":
        forest.append((x,y))
      elif char == "^":
        slopes["up"].append((x,y))
      elif char == "v":
        slopes["down"].append((x,y))
      elif char == ">":
        slopes["right"].append((x,y))
      elif char == "<":
        slopes["left"].append((x,y))

  max_x = x
  max_y = y

  clean = {}

def visualize(choices):

  global forest, slopes, max_x, max_y

  line = " "
  for y in range(max_y+1):
    line +=str(y)[-1:]
  print(line)
  for x in range(max_x+1):
    line = str(x)[-1:]
    for y in range(max_y+1):
      if (x,y) in choices:
        line += "O"
      elif (x,y) in forest:
        line += "#"
      elif (x,y) in slopes["up"]:
        line += "^"
      elif (x,y) in slopes["down"]:
        line += "v"
      elif (x,y) in slopes["left"]:
        line += "<"
      elif (x,y) in slopes["right"]:
        line += ">"
      else:
        line += "."
    print(line)

  print()

def find_nb(spot, visited, part):

  nbs = []

  options = [(spot[0]-1,spot[1]),
             (spot[0]+1,spot[1]),
             (spot[0],spot[1]-1),
             (spot[0],spot[1]+1)]

  for one in options:
    if 0 <= one[0] <= max_x and \
       0 <= one[1] <= max_y:
      if not one in visited and not one in forest:
        if part == 2:
          nbs.append(one)
        else:
          if (one in slopes["up"] and one[0] < spot[0]) \
             or (one in slopes["down"] and one[0] > spot[0]) \
             or (one in slopes["left"] and one[1] < spot[1]) \
             or (one in slopes["right"] and one[1] > spot[1]):
            nbs.append(one)
          elif not one in slopes["up"] and \
               not one in slopes["down"] and \
               not one in slopes["left"] and \
               not one in slopes["right"]:
            nbs.append(one)

  return nbs

def find_nb2(spot, visited):

  global clean

  nbs = []

  options = list(clean[spot].keys())

  for one in options:
    if not one in visited:
      nbs.append(one)

  return nbs


def find_path(start,visited,part):

  if start == (max_x,max_y - 1):
    return len(visited)

  nbs = find_nb(start,visited,part)

  options = [0]
  for nb in nbs:
    options.append(find_path(nb,visited + [start], part))

  return max(options)

def find_path2(start,visited, result, end):

  if start == end:
    return result

  nbs = find_nb2(start,visited)

  options = [0]
  for nb in nbs:
    #print("Neighbor: "+str(nb))
    options.append(find_path2(nb,visited + [start], clean[start][nb], end))

 # print("visited: "+str(visited)+" result: "+str(result + max(options)))
  return result + max(options)

saved_lowest = None

def find_current(unvisited,distances):
    global saved_lowest
    lowest_val = None
    lowest = None
    for x in unvisited:
        if x in distances:
            if (not lowest_val) or distances[x] < lowest_val:
                lowest_val = distances[x]
                lowest = x
            if saved_lowest and lowest_val == saved_lowest:
                return lowest
    if lowest:
        saved_lowest = lowest_val
        return lowest
    else:
        return None

compressed = {}

def compress(start,spot,distance,visited):

  global compressed, max_x, max_y

  #print("Compress from "+str(start)+" at "+str(spot)+" with distance "+str(distance)+ " visited: "+str(visited))

  options = [(spot[0]-1,spot[1]),
             (spot[0]+1,spot[1]),
             (spot[0],spot[1]-1),
             (spot[0],spot[1]+1)]

  realoptions = []

  for one in options:
    if 0 <= one[0] <= max_x and \
       0 <= one[1] <= max_y:
      if not one in visited and not one in forest:
        realoptions.append(one)

  if len(realoptions) == 0:
    return
  elif len(realoptions) == 1:
    compress(start,realoptions[0],distance+1,visited+[realoptions[0]])
  else:
  #  print(realoptions)
    for one in realoptions:
      if spot in compressed:
        if start in compressed[spot]:
          if one in compressed[spot][start]:
            continue
          else:
            compressed[spot][start][one] = distance + 1
        else:
          compressed[spot][start] = {one: distance + 1}
      else:
        compressed[spot] = {start: {one: distance + 1}}
      if start in compressed:
        if spot in compressed[start]:
          if start in compressed[spot]:
            if one in compressed[start][spot]:
              continue
            else:
              compressed[start][spot][one] = distance + 1
          else:
            compressed[start][spot] = {one: distance + 1}
        else:
          compressed[start][spot] = {one: distance + 1}
      else:
        compressed[start] = {spot: {one: distance + 1}}

      compress(spot,one,0,[spot,one])


def run_part1():


  start = (0,1)

  print(find_path(start,[],1))

def run_part2():

  start = (0,1)

  print(find_path(start,[],2))

def run_part2_d():

  unvisited = []
  for x in range(max_x+1):
    for y in range(max_y+1):
      if not (x,y) in forest:
        unvisited.append((x,y))

  visited = []
  distances = {(0,1): 0}

  current = find_current(unvisited,distances)

  while current and not (max_x,max_y - 1) in distances:
    if len(visited) % 1000 == 0:
        print(len(visited))
    neighbors = [x for x in find_nb(current,visited,2) if x not in visited]

    for nb in neighbors:
        distance = distances[current] - 1
        if nb in distances and distances[nb] > distance:
            distances[nb] = distance
        elif not nb in distances:
            distances[nb] = distance

    print(current)
    print(distances)

    visited.append(current)
    unvisited.remove(current)
    distances.pop(current)

    current = find_current(unvisited,distances)

def run_part2_2():

  global clean

  start = (0,1)

  compress(start,start,0,[start])

  for fr in compressed:
    clean[fr] = {}
    for t in compressed[fr]:
      if fr == start or t == start:
        clean[fr][t] = list(compressed[fr][t].values())[0] - 1
      else:
        clean[fr][t] = list(compressed[fr][t].values())[0]

  print(clean)
  visualize(compressed)

  if inputfile == "test.txt":

    start = (0,1)
    end = (19,19)
    final = 5

  else:

    start = (0,1)
    end = (135,133)
    final = 31



  print(find_path2(start,[],final,end))

#run_part1()
run_part2_2()
