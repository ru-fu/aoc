import sys
import numpy

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"


class Node:

    def __init__(self,name):
      self.name = name
      self.left = None
      self.right = None

    def set_left(self,left):
      self.left = left

    def set_right(self,right):
      self.right = right

    def __str__(self):
      return "name: "+self.name+" left: "+self.left.get_name()+" right: "+self.right.get_name()

    def move(self,which):
      if which == "L":
        return self.left
      else:
        return self.right

    def get_name(self):
      return self.name

nodes = []

with open(inputfile,"r") as input:

  directions = input.readline().strip()

  for line in input:
    line = line.strip()
    if line:
      a = line.split(" = ")
      b = a[1].strip("()").split(", ")
      this = [x for x in nodes if x.get_name() == a[0]]
      if len(this) == 1:
        node = this[0]
      else:
        node = Node(a[0])
        nodes.append(node)
      left = [x for x in nodes if x.get_name() == b[0]]
      if len(left) == 1:
        node.set_left(left[0])
      else:
        new = Node(b[0])
        node.set_left(new)
        nodes.append(new)
      right = [x for x in nodes if x.get_name() == b[1]]
      if len(right) == 1:
        node.set_right(right[0])
      else:
        new = Node(b[1])
        node.set_right(new)
        nodes.append(new)

def run_part1():

  global directions

#  for node in nodes:
#    print(node)

  start = "AAA"
  end = "ZZZ"

  find = [x for x in nodes if x.get_name() == start]
  node = find[0]
  count = 0

  while not start == end:
    count += 1
    print(node)
    go = directions[0]
    directions = directions[1::]+go
    node = node.move(go)
    start = node.get_name()

  print(count)

def run_part2():

  global directions

#  for node in nodes:
#    print(node)

  start = [x for x in nodes if x.get_name().endswith("A")]
  end = [x.get_name() for x in nodes if x.get_name().endswith("Z")]

  counts = []
  seqs = []
  for x in start:
    seqs.append(0)
    counts.append(0)

## each start node leads to only one end node in the input data, in regular intervals ...

  while 0 in seqs:
    go = directions[0]
    directions = directions[1::]+go
    for i,node in enumerate(start):
      counts[i] += 1
      node = node.move(go)
      start[i] = node
      if node.get_name() in end:
 #       print(str(i) + " "+ node.get_name())
        seqs[i] = counts[i]
        counts[i] = 0

  print(seqs)
  print(numpy.lcm.reduce(seqs))

#run_part1()
run_part2()
