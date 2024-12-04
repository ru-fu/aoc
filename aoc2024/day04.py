import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  sheet = [line.rstrip() for line in input]
  sheet = [x for x in sheet if not x == ""]

def get(x,y):
  global sheet
  
  if 0 <= x < len(sheet):
    if 0 <= y < len(sheet[x]):
      return sheet[x][y]

  return 0

def nextletter(x):
  if x == "X":
    return "M"
  elif x == "M":
    return "A"
  elif x =="A":
    return "S"
  else:
    print("huh??")

def check(direction, lookingfor, x, y):
  global sheet

  new_x = x
  new_y = y

  if direction == 0:
    new_x += -1 
    new_y += -1
  elif direction == 1:
    new_x += -1
  elif direction == 2:
    new_x += -1 
    new_y += 1
  elif direction == 3:
    new_y += -1
  elif direction == 4:
    new_y += 1
  elif direction == 5:
    new_x += 1 
    new_y += -1
  elif direction == 6:
    new_x += 1
  elif direction == 7:
    new_x += 1 
    new_y += 1

  found = get(new_x,new_y)

  if found == 0 or not found == lookingfor:
    return False

  if lookingfor == "S":
    return True
  else:
    return check(direction, nextletter(lookingfor), new_x, new_y)

def check2(x,y):

  ok1 = 0
  
  if get(x-1,y-1) == "M" and get(x+1,y+1) == "S":
    ok1 = 1
  elif get(x-1,y-1) == "S" and get(x+1,y+1) == "M":
    ok1 = 1

  if not ok1:
    return False

  if get(x+1,y-1) == "M" and get(x-1,y+1) == "S":
    return True
  elif get(x+1,y-1) == "S" and get(x-1,y+1) == "M":
    return True

  return False
  
    
def run_part1():

  total = 0

  for x in range(len(sheet)):
    for y in range(len(sheet[x])):
      for direction in range(8):
        if get(x,y) == "X" and check(direction,"M",x,y):
          #print("direction: "+str(direction)+" Coords: "+str(x)+","+str(y))
          total += 1

  print(total)

def run_part2():

  total = 0

  for x in range(len(sheet)):
    for y in range(len(sheet[x])):
      if get(x,y) == "A" and check2(x,y):
        total += 1
        

  print(total)

run_part1()
run_part2()
