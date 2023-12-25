import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

ins = []

with open(inputfile,"r") as input:

  for line in input:
    instructions = line.strip().split()
    ins.append((instructions[0],int(instructions[1]),instructions[2].strip("()#")))

def visualize(dug):

  min_x = 0
  min_y = 0
  max_x = 0
  max_y = 0

  for one in dug:
    if one[0] < min_x:
      min_x = one[0]
    if one[0] > max_x:
      max_x = one[0]
    if one[1] < min_y:
      min_y = one[1]
    if one[1] > max_y:
      max_y = one[1]

  for x in range(min_x,max_x+1):
    line = ""
    for y in range(min_y,max_y+1):
      if (x,y) in dug:
        line += "#"
      else:
        line += "."
    print(line)

  print()

def create_path(ins):

  path = []

  current = (0,0)

  while not ins == []:
    instruction = ins.pop(0)
    if instruction[0] == "R":
      for i in range(instruction[1]):
        path.append((current[0],current[1]+i+1))
      current = (current[0],current[1]+i+1)
    elif instruction[0] == "L":
      for i in range(instruction[1]):
        path.append((current[0],current[1]-i-1))
      current = (current[0],current[1]-i-1)
    elif instruction[0] == "U":
      for i in range(instruction[1]):
        path.append((current[0]-i-1,current[1]))
      current = (current[0]-i-1,current[1])
    elif instruction[0] == "D":
      for i in range(instruction[1]):
        path.append((current[0]+i+1,current[1]))
      current = (current[0]+i+1,current[1])

  return path

def create_path2(ins):

  corners = []
  length = 0

  current = (0,0)

  while not ins == []:
    instruction = ins.pop(0)
    distance = int(instruction[2][:-1], 16)
    direction = "R"
    if instruction[2][-1] == "1":
      direction = "D"
    elif  instruction[2][-1] == "2":
      direction = "L"
    elif  instruction[2][-1] == "3":
      direction = "U"
    if direction == "R":
      corners.append((current[0],current[1]+distance))
      current = (current[0],current[1]+distance)
      length += distance
    elif direction == "L":
      corners.append((current[0],current[1]-distance))
      current = (current[0],current[1]-distance)
      length += distance
    elif direction == "U":
      corners.append((current[0]-distance,current[1]))
      current = (current[0]-distance,current[1])
      length += distance
    elif direction == "D":
      corners.append((current[0]+distance,current[1]))
      current = (current[0]+distance,current[1])
      length += distance

  return (corners,length)

def run_part1():

  print(ins)
  path = create_path(list(ins))
 # print(path)
 # visualize(path)
  print("Created path")

  polygon = Polygon(path)
#  area = polygon.bounds
#  print(area)
  print("Created polygon")
  print(int(polygon.area + len(path) // 2 + 1.0))

#  count = 0
#  for x in range(int(area[0]),int(area[2])+1):
#    for y in range(int(area[1]),int(area[3])+1):
#      if (x,y) in path:
#        count += 1
        #        contains.append((x,y))
#      else:
#        point = Point(x,y)
#        if polygon.contains(point):
#          count += 1
   #       contains.append((x,y))
   #     else:
   #       print("NOPE! "+str((x,y)))

  #print(contains)
  #visualize(contains)

#  print(len(path))
#  print(count)

def run_part2():

  (corners, length) = create_path2(ins)
  print("Created path")
  print(length)

  polygon = Polygon(corners)
  print("Created polygon")
  print(int(polygon.area + length // 2 + 1.0))

run_part1()
run_part2()
