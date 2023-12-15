import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  sequence = ""

  for line in input:
    sequence += line.strip()

seq = sequence.split(",")

def calc_hash(s):

  value = 0

  for char in s:
    value += ord(char)
    value = value * 17
    value = value % 256

  return value

def parse(inst):

  if inst.endswith("-"):
    return ("remove",{"label":inst[:-1],"box":calc_hash(inst[:-1])})
  else:
    splt = inst.split("=")
    return ("add",{"label":splt[0],"box":calc_hash(splt[0]),"strength":int(splt[1])})

def score(boxes):

  result = []

  for box in boxes:
    for i,lens in enumerate(boxes[box]):
      one = (1 + box) * (i + 1) * lens[1]
      print(str(1 + box)+" * "+str(i + 1)+" * "+str(lens[1])+" = "+str(one))
      result.append(one)

  return result


def run_part1():

  print(sequence)

  result = []

  for s in seq:
    result.append(calc_hash(s))

  print(result)
  print(sum(result))

def run_part2():

  boxes = {}

  for s in seq:
    inst = parse(s)
    print(inst)


    if inst[0] == "add":
      if inst[1]["box"] in boxes:
        found = 0
        for i,(l,n) in enumerate(boxes[inst[1]["box"]]):
          found = 0
          print(found)
          if l == inst[1]["label"]:
            boxes[inst[1]["box"]][i] = (l,inst[1]["strength"])
            print("Updated strength of "+l+" from "+str(n)+" to "+str(inst[1]["strength"]))
            print(boxes)
            found = 1
            break
        print("Found: "+str(found))
        if not found:
          print("here")
          boxes[inst[1]["box"]].append((inst[1]["label"],inst[1]["strength"]))
          print("Added "+inst[1]["label"]+" with strength "+str(inst[1]["strength"]))
          print(boxes)
      else:
          boxes[inst[1]["box"]] = [(inst[1]["label"],inst[1]["strength"])]
          print("Added new box with "+inst[1]["label"]+" with strength "+str(inst[1]["strength"]))
          print(boxes)
    elif inst[0] == "remove":
      if inst[1]["box"] in boxes:
        found = [(l,n) for (l,n) in boxes[inst[1]["box"]] if l == inst[1]["label"]]
        if len(found) > 0:
          boxes[inst[1]["box"]].remove(found[0])
        print("Removed "+inst[1]["label"])
        print(boxes)
      else:
        print("Nothing to do.")



  print(sum(score(boxes)))


run_part1()
run_part2()
