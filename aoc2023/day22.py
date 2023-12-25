import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

class Brick:

  def __init__(self,coord1,coord2):
    (self.x1,self.y1,self.z1) = coord1
    (self.x2,self.y2,self.z2) = coord2
    self.cubes = set()
    self.update()

  def copy(self):
    return Brick((self.x1,self.y1,self.z1),(self.x2,self.y2,self.z2))

  def update(self):

    self.resting_on = []
    if self.z1 == 1:
      self.resting_on.append("ground")
    self.cubes.clear()

    if self.x1 == self.x2:
      if self.y1 == self.y2 and self.z1 == self.z2:
        self.orientation = "cube"
        self.cubes.add((self.x1,self.y1,self.z1))
      elif self.y1 == self.y2:
        self.orientation = "vertical"
        for i in range(self.z2 - self.z1 + 1):
          self.cubes.add((self.x1,self.y1,self.z1+i))
      elif self.z1 == self.z2:
        self.orientation = "horizontal-y"
        for i in range(self.y2 - self.y1 + 1):
          self.cubes.add((self.x1,self.y1+i,self.z1))
      else:
        print("HUUUUUUUUUH?")
    elif self.y1 == self.y2 and self.z1 == self.z2:
      self.orientation = "horizontal-x"
      for i in range(self.x2 - self.x1 + 1):
          self.cubes.add((self.x1+i,self.y1,self.z1))
    else:
      print("NOOOOOOOOOOOO!")

  def get_cubes(self):
    return list(self.cubes)

  def get_orientation(self):
    return self.orientation

  def get_lowest(self):
    return self.z1

  def stable(self):
    if len(self.resting_on) > 0:
      return True
    else:
      return False

  def drop(self,cubes):
    #print("Dropping "+str(self)+" Cubes: "+str(cubes))
    if self.orientation == "cube" or self.orientation == "vertical":
      repeat = True
      while repeat:
        if self.z1-1 > 0 and not (self.x1,self.y1,self.z1-1) in cubes:
          self.z1 = self.z1 - 1
          self.z2 = self.z2 - 1
          self.update()
        else:
          repeat = False
    elif self.orientation == "horizontal-x" or self.orientation == "horizontal-y":
      repeat = True
      while repeat:
        free = False
        for (x,y,z) in self.cubes:
          if z-1 > 0 and not (x,y,z-1) in cubes:
            free = True
          else:
            free = False
            break
        if free:
          self.z1 = self.z1 - 1
          self.z2 = self.z2 - 1
          self.update()
        else:
          repeat = False


  def __str__(self):
    coords = ((self.x1,self.y1,self.z1),(self.x2,self.y2,self.z2))
    string = str(coords)+" "+self.orientation+": "+str(self.cubes)
    if self.stable():
      return string+" STABLE"
    else:
      return string

bricks = []

with open(inputfile,"r") as input:

  for line in input:
    coords = line.strip().split("~")
    coord1= coords[0].split(",")
    coord2= coords[1].split(",")

    bricks.append(Brick((int(coord1[0]),int(coord1[1]),int(coord1[2])),
                        (int(coord2[0]),int(coord2[1]),int(coord2[2]))))

def all_cubes(bricks):

  cubes = []
  for x in [x.get_cubes() for x in bricks]:
    cubes.extend(x)

  return cubes

def settle(bricks):

  bricks.sort(key=lambda x:x.get_lowest())

  cubes_before = all_cubes(bricks)
  cubes_after = []

  while not cubes_before == cubes_after:

    bricks.sort(key=lambda x:x.get_lowest())

    cubes_before = all_cubes(bricks)

    for brick in bricks:
      #print(brick)

      if not brick.stable():
        brick.drop(all_cubes(bricks))

      #print(brick)

    cubes_after = all_cubes(bricks)

def test(brick,count):

  print(count)

  global bricks

  testbricks = []
  for b in bricks:
    if not b == brick:
      testbricks.append(b.copy())

  cubes_before = all_cubes(testbricks)
  settle(testbricks)
  cubes_after = all_cubes(testbricks)

  if cubes_before == cubes_after:
    return True
  else:
    return False

def test2(brick,count):

  print(count)

  global bricks

  testbricks = []
  for b in bricks:
    if not b == brick:
      testbricks.append(b.copy())

  result = 0

  for b in testbricks:

    cubes_before = b.get_cubes()

    if not b.stable():
      b.drop(all_cubes(testbricks))
      cubes_after = b.get_cubes()

      if not cubes_before == cubes_after:
        result += 1

  #print(result)
  return result

def run_part1():

  global bricks

  print("BEFORE")
  for brick in bricks:
    print(brick)

  settle(bricks)

  print("AFTER")
  for brick in bricks:
    print(brick)

  print("Total bricks: "+str(len(bricks)))

  count = 0
#  for i,brick in enumerate(bricks):
#    if test(brick,i):
#      count += 1

#  print("Result part 1: "+str(count))

def run_part2():

  count = 0

  for i,brick in enumerate(bricks):
    count += test2(brick,i)

  print("Result part 2: "+str(count))

run_part1()
run_part2()
