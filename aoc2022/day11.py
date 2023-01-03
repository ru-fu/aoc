monkeys = []
divisors = set(())

class Monkey:

  def __init__(self,items,op,test,true,false):
    self.items = [int(i) for i in items]
    self.op = op
    self.test = test
    self.true = int(true)
    self.false = int(false)
    self.count = 0

  def __str__(self):
    return str(self.items)

  def testf(self):
    return self.test(39)

  def act(self):
    while(self.items):
      item = self.items.pop(0)
      item = self.op(item)
      item = item // 3
      if self.test(item):
        monkeys[self.true].new_item(item)
      else:
        monkeys[self.false].new_item(item)
      self.count += 1

  def act2(self):
    while(self.items):
      item = self.items.pop(0)
      item = self.op(item)
      if item > self.div:
        item = item % self.div
      if self.test(item):
        monkeys[self.true].new_item(item)
      else:
        monkeys[self.false].new_item(item)
      self.count += 1

  def new_item(self, item):
    self.items.append(item)

  def set_div(self,div):
    self.div = div

def make_op(opstr):
  oplist = opstr[6:].split(" ")
  if oplist[1] == "+":
    if oplist[2] == "old":
      return lambda x : x + x
    else:
      return lambda x : x + int(oplist[2])
  elif oplist[1] == "*":
    if oplist[2] == "old":
      return lambda x : x * x
    else:
      return lambda x : x * int(oplist[2])
  else:
    raise Exception("huh?")

def make_test(teststr):
  global divisors
  divisors.add(int(teststr[13:]))
  return lambda x : (x % int(teststr[13:]) == 0)

with open("input11.txt","r") as input:

  line = input.readline()

  while(line):
    if line.startswith("Monkey "):
      items = input.readline().strip()[16:].split(", ")
      op = make_op(input.readline().strip()[11:])
      test = make_test(input.readline().strip()[6:])
      true = input.readline().strip()[25:]
      false = input.readline().strip()[26:]
      monkeys.append(Monkey(items,op,test,true,false))
    line = input.readline()

def run_part1():


  for i in range(20):
    print("Round "+str(i+1))

    for monkey in monkeys:
      monkey.act()

#    for monkey in monkeys:
#      print(monkey)

  counts = sorted([m.count for m in monkeys])
  print(counts[-1]*counts[-2])


def run_part2():

  print(divisors)
  div = 1
  for x in divisors:
    div = div * x
  print(div)
  for monkey in monkeys:
    monkey.set_div(div)

  for i in range(10000):
    print("Round "+str(i+1))

    for monkey in monkeys:
      monkey.act2()

#    print([m.count for m in monkeys])

  counts = sorted([m.count for m in monkeys])
  print(counts)
  print(counts[-1]*counts[-2])

#run_part1()
run_part2()
