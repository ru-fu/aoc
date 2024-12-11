import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

stones = ""

class Stone:

  def __init__(self, value):
    self.value = value
    self.next = None

  def set_next(self,next):
    self.next = next

  def __str__(self):
    return "value: "+str(self.value)

  def blink(self):
    if self.value == 0:
      self.value = 1
      if self.next:
        self.next.blink()
    elif len(str(self.value)) % 2 == 0:
      print(self.value)
      firstval = str(self.value)[:int(len(str(self.value))/2)]
      secondval = str(self.value)[int(len(str(self.value))/2):]
      self.value = int(firstval)
      st = Stone(int(secondval))
      st.set_next(self.next)
      self.next = st
      if st.get_next():
        st.get_next().blink()
    else:
      self.value = self.value * 2024
      if self.next:
        self.next.blink()

  def get_next(self):
    return self.next

  def get_value(self):
    return self.value

def print_chain(start):
  ret = str(start.get_value())
  add = start.get_next()
  
  while add:
    ret += " "+str(add.get_value())
    add = add.get_next()

  print(ret)

def count_chain(start):
  ret = 1
  add  = start.get_next()
  
  while add:
    ret += 1
    add = add.get_next()

  return ret
  
with open(inputfile,"r") as input:

  for line in input:
    stones += line.rstrip()
    stones = [int(x) for x in stones.split(" ")]

def run_part1():

  firstval = stones.pop(0)

  first = Stone(firstval)

  prev = first
  
  for val in stones:
    stone = Stone(val)
    prev.set_next(stone)
    prev = stone

  for i in range(25):
    print("Blink "+str(i+1))
    first.blink()
    print_chain(first)
    print("Number of stones: "+str(count_chain(first)))

def run_part2():

  print("result")

run_part1()
run_part2()
