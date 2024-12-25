import sys
import networkx as nx
import matplotlib.pyplot as plt

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

startvals = {}
inputs = {}
gates = {}

class Gate:

  def __init__(self, name, gatetype):
    self.name = name
    self.gatetype = gatetype
    self.in1 = None
    self.in2 = None
    self.outval = None

  def get_name(self):
    return self.name

  def get_val(self):
    return self.outval

  def preset_in1(self,val):
    self.in1 = val

  def preset_in2(self,val):
    self.in2 = val

  def set_in1(self,val):
    self.in1 = val
    if not self.in2 == None:
      self.calc()
      self.write()

  def set_in2(self,val):
    self.in2 = val
    if not self.in1 == None:
      self.calc()
      self.write()

  def write(self):
    global inputs, gates

    if self.name in inputs and not self.outval == None:

      for one in inputs[self.name]:
        (no,wire) = one

#        print("Setting "+wire+" to "+str(self.outval))

        if no == 1:
          gates[wire].set_in1(self.outval)
        else:
          gates[wire].set_in2(self.outval)

      #self.reset()

  def copy(self):

    gate = Gate(self.name,self.gatetype)
    return gate

  def calc(self):

    if (not self.in1 == None) and (not self.in2 == None) and (self.outval == None):

      if self.gatetype == "AND":
        result = self.in1 and self.in2
      elif self.gatetype == "OR":
        result = self.in1 or self.in2
      elif self.gatetype == "XOR":
        result = self.in1 ^ self.in2
      self.outval = result
      print("Calculated "+self.name)
      print(self)

  def __str__(self):
    return "Gate "+self.name+" ("+self.gatetype+") in1: "+str(self.in1)+" in2: "+str(self.in2)+" out: "+str(self.outval)

G = nx.Graph()

with open(inputfile,"r") as input:

  for line in input:
    line = line.rstrip()
    if ":" in line:
      val = line.split(": ")
      startvals[val[0]] = int(val[1])
    elif ">" in line:
      val = line.split(" ")
      gate = Gate(val[4],val[1])
      gates[val[4]] = gate
      #G.add_node(val[4])
      if val[0] in inputs:
        inputs[val[0]].append((1, val[4]))
      else:
        inputs[val[0]] = [(1, val[4])]
       # G.add_node(val[0])
      if val[2] in inputs:
        inputs[val[2]].append((2, val[4]))
      else:
        inputs[val[2]] = [(2, val[4])]
        #G.add_node(val[2])
      G.add_edge(val[0],val[4])
      G.add_edge(val[2],val[4])

def get_result(which = 1):
  global gates

  zs = sorted([gate for gate in gates if gates[gate].get_name().startswith("z")], reverse=True)

  out = ""

  for z in zs:
    out += str(gates[z].get_val())

  if which == 1:
    return int(out,2)
  else:
    return out

def what_we_want():
  global startvals

  xs = sorted([key for key in startvals if key.startswith("x")], reverse=True)
  ys = sorted([key for key in startvals if key.startswith("y")], reverse=True)


  outx = ""
  outy = ""

  for x in xs:
    outx += str(startvals[x])
  for y in ys:
    outy += str(startvals[y])

  return (outx,outy,str(bin(int(outx, 2) + int(outy, 2)))[2:])

def swap(one,two):

  global gates

  keep = gates[one]

  gates[one] = gates[two]
  gates[two] = keep

def run_part1():

  #print(startvals)
  #print(inputs)
#  print(gates)

  for wire,val in startvals.items():
    #print("Presetting "+wire+" to "+str(val))
    for writeto in inputs[wire]:
      (no,where) = writeto
      if no == 1:
        gates[where].set_in1(val)
      else:
        gates[where].set_in2(val)
      #print(gates[where])

#  for gate in gates:
#    print("Check "+gate)
#    gates[gate].calc()
#    gates[gate].write()

#  for gate in gates:
#    print(gates[gate])

  print(get_result())

def run_part2():

  global inputs, startvals, G

  added = set()

  for node in sorted(inputs):
    if not node in added:
      G.add_node(node)
      added.add(node)
      if node.startswith('x'):
        G.nodes[node]['subset'] = 0
      elif node.startswith('y'):
        G.nodes[node]['subset'] = 1
      elif node.startswith('z'):
        G.nodes[node]['subset'] = 3
      else:
        G.nodes[node]['subset'] = 2
    for outs in inputs[node]:
      outnode = outs[1]

      #print("\t"+node+" --> "+outnode)

      if not outnode in added:
        G.add_node(outnode)
        added.add(outnode)
        if outnode.startswith('x'):
          G.nodes[outnode]['subset'] = 0
        elif outnode.startswith('y'):
          G.nodes[outnode]['subset'] = 1
        elif outnode.startswith('z'):
          G.nodes[outnode]['subset'] = 3
        else:
          G.nodes[outnode]['subset'] = 2
        G.add_edge(node,outnode)
       # print("\t"+node+" --> "+outnode)
#    if node.startswith("x") or node.startswith("y") :
#      printnode="id2("+node+")"
#    elif node.startswith("y"):
#      printnode="id2("+node+")"
#    else:
#      printnode="id3("+node+")"
#    if outnode.startswith("z"):
#      print("\t"+printnode+" --> id1("+outnode+")")
#    elif outnode.startswith("x") or outnode.startswith("y"):
#      print("\t"+printnode+" --> id2("+outnode+")")
#    else:
#      print("\t"+printnode+" --> id3("+outnode+")")



  for i in range(44):
    G.add_edge("x"+f"{i:02d}","x"+f"{i+1:02d}")
    print("\t"+"z"+f"{i:02d}"+" --> "+"z"+f"{i+1:02d}")
    print("\t"+"x"+f"{i:02d}"+" --> "+"x"+f"{i+1:02d}")
    print("\t"+"y"+f"{i:02d}"+" --> "+"y"+f"{i+1:02d}")

  pos=nx.multipartite_layout(G)
  #nx.draw(G, pos)
  #nx.draw_networkx_labels(G, pos)
  #plt.show()

  gates_backup = {}
  for gate in gates:
    gates_backup[gate] = gates[gate].copy()

  for gate in gates:
    if gates[gate].gatetype == "OR":
      print(gate)

 # swap("z08","thm")
 # swap("z29","hwq")
 # swap("z22","wrm")
  run_part1()
  www = what_we_want()
  print(www[2])
  print(get_result(2))

  ok = False
  testnum = 10

  while ok:

    startvals = {}
    for i in range(45):
      startvals["x"+f"{i:02d}"] = 0
      startvals["y"+f"{i:02d}"] = 0

    for i,char in enumerate(str(bin(testnum))[2:]):
      startvals["x"+f"{i:02d}"] = int(char)
      startvals["y"+f"{i:02d}"] = int(char)

    run_part1()
    www = what_we_want()
    if int(www[2],2) == int(get_result(2),2):
      testnum += 1
    else:
      ok = False
      for gate in sorted(gates.keys()):
        print(gates[gate])
      print(inputs)

      print(www[2])
      print(get_result(2))

#run_part1()
run_part2()


# Manual inspection according to
# https://www.reddit.com/r/adventofcode/comments/1hla5ql/2024_day_24_part_2_a_guide_on_the_idea_behind_the/
# Rule 1: Z29 Z22 Z08
# Rule 2: hwq thm gbs
# Last pair: wss wrm
# => gbs,hwq,thm,wrm,wss,z08,z22,z29
