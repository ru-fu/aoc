class Tree:

  def __init__(self,height):
    self.height = int(height)
    self.left = []
    self.right = []
    self.up = []
    self.down = []
    self.visible_left = False
    self.visible_right = False
    self.visible_up = False
    self.visible_down = False
    self.count_left = 0
    self.count_right = 0
    self.count_up = 0
    self.count_down = 0

  def __str__(self):
    return str(self.height)

  def set(self,direction,data):
    if direction == "left":
      self.left = data
    elif direction == "right":
      self.right = data
    elif direction == "up":
      self.up = data
    elif direction == "down":
      self.down = data
    else:
      raise Exception("typo")

  def get(self,direction):
    if direction == "left":
      return self.left
    elif direction == "right":
      return self.right
    elif direction == "up":
      return self.up
    elif direction == "down":
      return self.down
    else:
      raise Exception("typo")

  def check(self):
    if len(self.left) == 0 or self.height > max([int(x) for x in self.left]):
      self.visible_left = True
    elif len(self.right) == 0 or self.height > max([int(x) for x in self.right]):
      self.visible_right = True
    elif len(self.up) == 0 or self.height > max([int(x) for x in self.up]):
      self.visible_up = True
    elif len(self.down) == 0 or self.height > max([int(x) for x in self.down]):
      self.visible_down = True
    return (self.visible_left or self.visible_right or self.visible_up or self.visible_down)

  def count(self):
    self.count_left = 0
    self.count_right = 0
    self.count_up = 0
    self.count_down = 0
    for treeheight in self.left:
      self.count_left += 1
      if int(treeheight) >= self.height:
        break
    for treeheight in self.right:
      self.count_right += 1
      if int(treeheight) >= self.height:
        break
    for treeheight in self.up:
      self.count_up += 1
      if int(treeheight) >= self.height:
        break
    for treeheight in self.down:
      self.count_down += 1
      if int(treeheight) >= self.height:
        break

    return self.count_left * self.count_right * self.count_up * self.count_down


def print_wood(wood):
  out = ""
  out2 = ""
  for row in wood:
    for tree in row:
      out += str(tree)
#      out2 += str(tree.get("up"))
#      print(str(tree.check()))
#      tree.count()
#      print(str(tree.count_down))
    out += "\n"

  print(out)
#  print(out2)

wood = []

with open("input08.txt","r") as input:

  for line in input:
    row = []
    for char in line.strip():
      row.append(Tree(char))
    wood.append(row)

for row in wood:
  for i,tree in enumerate(row):
    rowheights = [str(x) for x in row]
    left = rowheights[:i]
    left.reverse()
    tree.set("left",left)
    tree.set("right",rowheights[i+1:])

for i in range(len(wood[0])):
  col = []
  for j in range(len(wood)):
    col.append(str(wood[j][i]))
  for k,row in enumerate(wood):
    up = col[:k]
    up.reverse()
    row[i].set("up",up)
    row[i].set("down",col[k+1:])

def run_part1():

  print_wood(wood)
  visible = 0

  for row in wood:
    for tree in row:
      if tree.check():
        visible += 1

  print(visible)

def run_part2():

  scenic_score = []

  for row in wood:
    for tree in row:
      scenic_score.append(tree.count())

  print(max(scenic_score))

run_part1()
run_part2()
