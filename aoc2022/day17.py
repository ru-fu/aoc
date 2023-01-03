with open("test.txt","r") as input:

  movement = input.readline().strip()

class Shape:

  def __init__(self, which):
    self.which = which
    self.left = 0
    if which == 1:
      self.width = 4
      self.fields = [(0,0),(1,0),(2,0),(3,0)]
    elif which == 2:
      self.width = 3
      self.fields = [(1,0),(0,1),(1,1),(2,1),(1,2)]
    elif which == 3:
      self.width = 3
      self.fields = [(0,0),(1,0),(2,0),(2,1),(2,2)]
    elif which == 4:
      self.width = 1
      self.fields = [(0,0),(0,1),(0,2),(0,3)]
    elif which == 5:
      self.width = 2
      self.fields = [(0,0),(1,0),(0,1),(1,1)]
    else:
      print (which)
      raise Exception("huh?")

  def __str__(self):
    return str(self.fields)+str(self.left)

  def place(self,a,b):
    self.fields = [(x+a,y+b) for (x,y) in self.fields]
    self.left += a

  def move(self,direction,floor):
    if direction == "right":
      if (self.left + self.width) > 6:
        return
      else:
        new_fields = []
        for (x,y) in self.fields:
          if floor[x+1] >= y:
            return
          else:
            new_fields.append((x+1,y))
        self.fields = new_fields
        self.left += 1
    else:
      if self.left - 1 < 0:
        return
      else:
        new_fields = []
        for (x,y) in self.fields:
          if floor[x-1] >= y:
            return
          else:
            new_fields.append((x-1,y))
        self.fields = new_fields
        self.left += -1

  def fall(self):
    self.fields = [(x,y-1) for (x,y) in self.fields]

  def can_fall(self, floor):
    for (x,y) in self.fields:
      if floor[x] == y-1:
        return x
    return None

  def stack(self, x):
    add = []
    for i in range(self.left):
      add.append(0)
    if self.which == 1:
      add.extend([1,1,1,1])
    elif self.which == 2:
      if (x - self.left) == 1:
        add.extend([2,3,2])
      else:
        add.extend([1,2,1])
    elif self.which == 3:
      add.extend([1,1,3])
    elif self.which == 4:
      add.extend([4])
    elif self.which == 5:
      add.extend([2,2])
    for i in range(self.left+self.width,7):
      add.append(0)
    return add

def create_shape(shape_no, floor):

  shape = Shape(shape_no % 5 + 1)
  shape.place(2,max(floor)+4)
#  print(shape)

  return shape

def run_part1():

  floor = [0,0,0,0,0,0,0]

  shape_no = 0
  shape = create_shape(shape_no, floor)

  i = -1

  while shape_no < 2023:
    i += 1
    if i >= len(movement):
      i = i - len(movement)
    if movement[i] == ">":
      shape.move("right",floor)
    else:
      shape.move("left",floor)
    print("move"+movement[i]+str(shape))
    res = shape.can_fall(floor)
    if res:
      stuck_at = floor[res]
      for x, offset in enumerate(shape.stack(res)):
        if offset > 0:
          floor[x] = stuck_at + offset
      print(floor)
      shape_no += 1
      shape = create_shape(shape_no, floor)
    else:
      shape.fall()
#    print("fall"+str(shape))

def run_part2():

  print("result")

run_part1()
run_part2()
