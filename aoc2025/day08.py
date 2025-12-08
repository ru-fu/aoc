import sys, math

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

points = dict()
closests = dict()
circuits = []
  
with open(inputfile,"r") as input:

  for line in input:
    points[tuple([int(x) for x in line.rstrip().split(",")])] = dict()


def calc_distances():
  global points,closests

  for fromp in points:
    for top in points:
      if fromp == top:
        pass
      elif fromp in points[top]:
        pass
      else:
        dist = math.dist(fromp,top)
        points[fromp][top] = dist
        points[top][fromp] = dist

  for one in points:
    closestval = min(points[one].values())
    closests[closestval] = ([x for x in points[one] if points[one][x] == closestval][0],one)
    circuits.append([one])

calc_distances()

print(points)
print(closests)

def find_closest():
  global closests, points

  for one in points:
    closestval = min(points[one].values())
    closests[closestval] = ([x for x in points[one] if points[one][x] == closestval][0],one)
  
  twopoints = closests[min(closests.keys())]
  
  points[twopoints[0]].pop(twopoints[1])
  points[twopoints[1]].pop(twopoints[0])

  closests = dict()

  return twopoints

def connect(twopoints, count=True):

  global circuits

  print("Connect "+str(twopoints[0])+" and "+str(twopoints[1]))

  found1 = "nope"
  found2 = "nope"
  
  for i,c in enumerate(circuits):
    if (not found1 == "nope") and (not found2 == "nope"):
      break
    if twopoints[0] in c:
      found1 = i
    if twopoints[1] in c:
      found2 = i

 # if (not found1 == "nope") and (found2 == "nope"):
 #   print("Add to existing circuit.")
 #   circuits[found1].append(twopoints[1])
 # elif (found1 == "nope") and (not found2 == "nope"):
 #   print("Add to existing circuit.")
 #   circuits[found2].append(twopoints[0])
 # elif (found1 == "nope") and (found2 == "nope"):
 #   print("Add new circuit.")
 #   circuits.append([twopoints[0], twopoints[1]])
 # el
  if (found1 == found2):
    print("Already connected.")
  else:
    print("Merge circuits.")
    circuit1 = circuits[found1]
    circuit2 = circuits[found2]

    if not count:

      for a in circuit1:
        for b in circuit2:
          if a in points and b in points[a]:
            points[a].pop(b)
          if b in points and a in points[b]:
            points[b].pop(a)
        
    circuits.pop(found1)
    circuits.remove(circuit2)
    circuit1.extend(circuit2)
    circuits.append(circuit1)

    
  return 1
  
  
def run_part1():

  count = 0

  while count < 1000:

    print(count)

    toconnect = find_closest()

    count += connect(toconnect)

    #print(circuits)

  sizes = [len(x) for x in circuits]

  result = max(sizes)

  sizes.remove(max(sizes))

  result = result * max(sizes)

  sizes.remove(max(sizes))

  result = result * max(sizes)

  print(result)

def run_part2():

  count = 0

  while len(circuits) > 1 :

    print(str(count)+" - "+str(len(circuits)))

    toconnect = find_closest()

    count += connect(toconnect,False)


#run_part1()
run_part2()
