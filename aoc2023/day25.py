import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

graph = {}
graphsimple = {}

with open(inputfile,"r") as input:

  for line in input:
    data = line.strip().split(": ")
    tos = data[1].split()

    if not data[0] in graph:
      graph[data[0]] = []
    if not data[0] in graphsimple:
      graphsimple[data[0]] = []

    for t in tos:
      graph[data[0]].append(t)
      graphsimple[data[0]].append(t)
      if not t in graph:
        graph[t] = [data[0]]
      else:
        graph[t].append(data[0])

def remove(a,b):

  global graph

  graph[a].remove(b)
  graph[b].remove(a)

def count(start):

  global graph

  found = set()

  process = [start]

  while process:

    one = process.pop(0)

    if not one in found:
      for t in graph[one]:
        process.append(t)

      found.add(one)

  print(found)

  return(len(found))






def run_part1():

  print(graph)

  for a in graphsimple:
    for b in graphsimple[a]:
      print(a+" -> "+b+";")

  # use neato (from graphviz) to visualize

  if inputfile == "test.txt":
    remove("hfx","pzl")
    remove("bvb","cmg")
    remove("nvd","jqt")

    res1 = count("rhn")
    res2 = count("lsr")

  else:
    remove("nxk","dfk")
    remove("hcf","lhn")
    remove("ldl","fpg")

    res1 = count("lkp")
    res2 = count("gmx")



  print(res1)
  print(res2)
  print(res1*res2)

def run_part2():

  print("result")

run_part1()
run_part2()
