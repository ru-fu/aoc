import sys
import numpy

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"


class Module:

  def __init__(self,name):
    self.name = name
    self.modules = []
    self.value = 0
    self.kind = "Module"

  def register_out(self, module):
    self.modules.append(module)

  def get_out(self):
    return self.modules

  def process(self,which):
    return None

  def read(self):
    return self.value

  def type(self):
    return self.kind

  def __str__(self):
    return self.kind+": "+self.name+" value: "+str(self.value)+" modules: "+str(self.modules)

class FlipFlop(Module):

  def __init__(self,name):
    super().__init__(name)
    self.kind = "FlipFlop"

  def process(self,which):
    if which == 0 and self.value == 1:
      self.value = 0
      return self.value
    elif which == 0 and self.value == 0:
      self.value = 1
      return self.value
    else:
      return None

class Broadcast(Module):

  def __init__(self,name):
    super().__init__(name)
    self.kind = "Broadcast"

  def process(self,which):
    self.value = which
    return self.value

class Conjunction(Module):

  def __init__(self,name):
    super().__init__(name)
    self.kind = "Conjunction"
    self.memory = {}

  def register_in(self,module):
    self.memory[module] = 0

  def process(self, module, which):
    self.memory[module] = which
    if len([x for x in self.memory.values() if x == 0]) == 0:
      self.value = 0
      return self.value
    else:
      self.value = 1
      return self.value

  def __str__(self):
    return self.kind+": "+self.name+" value: "+str(self.value)+" modules: "+str(self.modules)+" memory: "+str(self.memory)

modules = {}

with open(inputfile,"r") as input:

  for line in input:
    splt = line.strip().split(" -> ")
    if splt[0] == "broadcaster":
      name = splt[0]
      modules[name] = Broadcast(name)
    elif splt[0].startswith("%"):
      name = splt[0][1:]
      modules[name] = FlipFlop(name)
    elif splt[0].startswith("&"):
      name = splt[0][1:]
      modules[name] = Conjunction(name)
    for module in splt[1].split(", "):
      modules[name].register_out(module)

for m in list(modules.keys()):
  for outmodule in modules[m].get_out():
    if outmodule in modules:
      if modules[outmodule].type() == "Conjunction":
        modules[outmodule].register_in(m)
    else:
      modules[outmodule] = Module(outmodule)

def push_button(modules,part,count):

  to_process = [("button", "broadcaster", 0)]
  high = 0
  low = 1 # button press is low

  while len(to_process) > 0:
    process = to_process.pop(0)
    #print("Processing: "+str(process)+" queue: "+str(to_process))
    #print(modules[process[1]])
    if modules[process[1]].type() == "Conjunction":
      result = modules[process[1]].process(process[0],process[2])
      #if part == 2 and process[1] == "zh" and process[2] == 1:
       # print(modules["zh"],count)
        # dl: 3779
        # bh: 3761
        # ns: 3767
        # vd: 3881
    else:
      result = modules[process[1]].process(process[2])
    #print("Result: "+str(result))
    if not result == None:
      for m in modules[process[1]].get_out():
        if part == 2 and m == "rx" and result == 0:
          return True
        to_process.append((process[1],m,result))
        if result == 1:
          high += 1
        elif result == 0:
          low += 1

  if part == 1:
    return (low,high)
  else:
    return False

def run_part1():

  result_low = 0
  result_high = 0

  iterations = 1000

  for i in range(iterations):
    result = push_button(modules,1,0)
    result_low += result[0]
    result_high += result[1]


  print(result_low, result_high)
  print(result_low * result_high)
  #for m in modules:
  #  print(modules[m])


def run_part2():

  count = 0
  result = False

  #for m in modules:
  #  print(modules[m])

  #while not result:
  #  count += 1
  #  if count % 10000 == 0:
  #    print(count)
  #  result = push_button(modules,2,count)


  print(numpy.lcm.reduce([3779, 3761, 3767, 3881]))

#run_part1()
run_part2()
