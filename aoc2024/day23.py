import sys
import networkx as nx
import matplotlib.pyplot as plt

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

connections = {}
  
with open(inputfile,"r") as input:

  for line in input:
    pcs = line.rstrip().split("-")

    if pcs[0] in connections:
      connections[pcs[0]].add(pcs[1])
    else:
      connections[pcs[0]] = {pcs[1]}

    if pcs[1] in connections:
      connections[pcs[1]].add(pcs[0])
    else:
      connections[pcs[1]] = {pcs[0]}

def find_triplets():
  global connections

  triplets = set()

  for one in connections.keys():
    for two in connections[one]:
      commons = connections[two].intersection(connections[one])
      for c in commons:
        triplets.add(tuple(sorted([one,two,c])))

  return triplets

def find_options():
  global connections

  options = set()

  for one in connections.keys():
    for two in connections[one]:
      commons = connections[two].intersection(connections[one])
      if len(commons) > 1:
        options.add(one)
        options.add(two)
        options.update(commons)

  return options

def find_t(triplets):

  result = []

  for three in triplets:
    if three[0][0] == "t" or three[1][0] == "t" or three[2][0] == "t":
      result.append(three)

  return result

def run_part1():

  print(connections)
  triplets = find_triplets()
  result1 = find_t(triplets)

  print(result1)
  print(len(result1))

def run_part2():
  global connections

  options = find_options()

  G = nx.Graph()
  G.add_nodes_from(options)

  for o in options:
    for edge in connections[o]:
      G.add_edge(o,edge)
      
  print(G)
  pos=nx.spring_layout(G)
  nx.draw(G, pos)
  nx.draw_networkx_labels(G, pos)
 # plt.show()

  longest = []
  for c in nx.find_cliques(G):
    if len(c) > len(longest):
      longest = c

  print(",".join(sorted(longest)))

run_part1()
run_part2()
