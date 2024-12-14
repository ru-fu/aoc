import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
  max_x = 11
  max_y = 7
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"
  max_x = 101
  max_y = 103

class Robot:

  def __init__(self, x, y, move_x, move_y):
    self.x = x
    self.y = y
    self.move_x = move_x
    self.move_y = move_y

  def move(self,steps=1):
    self.x = normalize("x",self.x + steps * self.move_x)
    self.y = normalize("y",self.y + steps * self.move_y)

  def get_q(self):
    if self.x < int(max_x / 2):
      if self.y < int(max_y / 2):
        return 1
      elif self.y > int(max_y / 2):
        return 2
    elif self.x > int(max_x / 2):
      if self.y < int(max_y / 2):
        return 3
      elif self.y > int(max_y / 2):
        return 4
    return 0

  def get(self):
    return (self.x,self.y)

  def __str__(self):
    return "x: "+str(self.x)+" y: "+str(self.y)

def normalize(which,num):
  global max_x, max_y
#  print("normalize "+which+": "+str(num))
  if which == "x":
    return num % max_x
  else:
    return num % max_y


def print_robots(which=1):
  global robots, robots2, max_y, max_x

  if which==2:
    robs = robots2
  else:
    robs = robots

  pos = {}

  for r in robs:
    where = r.get()
 #   print(where)
    if where in pos:
      pos[where] += 1
    else:
      pos[where] = 1

  for y in range(max_y):
    row = ""
    for x in range(max_x):
      if (x,y) in pos:
        row += str(pos[(x,y)])
      else:
        row += "."
    print(row)

  print()


robots = []
robots2 = []

with open(inputfile,"r") as input1:

  for line in input1:
    fields = line.rstrip().split(",")
    x = fields[0][2:]
    y = fields[1].split(" ")[0]
    mx = fields[1].split(" ")[1][2:]
    my = fields[2]
    robots.append(Robot(int(x),int(y),int(mx),int(my)))
    robots2.append(Robot(int(x),int(y),int(mx),int(my)))

def run_part1():

#  test = Robot(2,4,2,-3)
#  print(test)
#  test.move()

  print_robots()
  quadrants = {0: 0,
               1: 0,
               2: 0,
               3: 0,
               4: 0}

  for r in robots:
    r.move(100)
    quadrants[r.get_q()] += 1
    print(r)

  print(quadrants)
  print(quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4])

def run_part2():

  for i in range(25000):
    for r in robots2:
      r.move()
    if i > 8086:
      break
    if i > 8000:
      print(i)
      print_robots(2)
      input('Nope ... ')

run_part1()
run_part2()
#15249-7163=8086 +1!
