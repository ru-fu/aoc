import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"


parts = []
rules = {}

with open(inputfile,"r") as input:

  for line in input:
    line = line.strip()

    if line.startswith("{"):
      tuples = line.strip("{}").split(",")
      vals = {}
      for one in tuples:
        val = one.split("=")
        vals[val[0]] = int(val[1])
      parts.append(vals)

    elif not line == "":
      rule = line.split("{")
      fullrule = rule[1].strip("}").split(",")
      one = []
      for r in fullrule:
        if ":" in r:
          longrule = r.split(":")
          if "<" in longrule[0]:
            this = longrule[0].split("<")
            one.append((("<", this[0], int(this[1])), longrule[1]))
          elif ">" in longrule[0]:
            this = longrule[0].split(">")
            one.append(((">", this[0], int(this[1])), longrule[1]))
        else:
          one.append((None, r))
      rules[rule[0]] = one

def process_part(start,part):

  global rules

  goto = ""

  if not start in rules:
    print("NOOOOOOOOO! "+start)
  else:
    rule = rules[start]
    for r in rule:
      if r[0] == None or (r[0][0] == "<" and
                          part[r[0][1]] < r[0][2]) or (r[0][0] == ">" and
                                                       part[r[0][1]] > r[0][2]):
        goto = r[1]
        break
    print("Checking part "+str(part)+" from "+start+" - result: "+goto)
    if goto == "":
      print("AAAAAAAAARGH!!")
    elif goto == "A":
      return 1
    elif goto == "R":
      return 0
    else:
      return process_part(goto,part)

def score(part):

  result = 0
  for val in part.values():
    result += val

  return result

def find_combinations(start,values):

    if start == "R":
      print("Reject")
      return 0

    if start == "A":
      print("Accept: "+str(values))
      return (values["max_x"] - values["min_x"] + 1) * (
        values["max_m"] - values["min_m"] + 1) * (
          values["max_a"] - values["min_a"] + 1) * (
            values["max_s"] - values["min_s"] + 1)

    rule = list(rules[start])

    fullrule = 0

    for r in rule:
      if r[0] == None:
        return fullrule + find_combinations(r[1],values)
      elif r[0][0] == "<":
        print("Rule: "+str(r))
        if values["max_"+r[0][1]] > r[0][2] - 1:
          values1 = values.copy()
          values1["max_"+r[0][1]] = r[0][2] - 1
          fullrule += find_combinations(r[1],values1)
          values["min_"+r[0][1]] = r[0][2]
        else:
          print("HUUUUUUH1?")
      elif r[0][0] == ">":
        print("Rule: "+str(r))
        if values["min_"+r[0][1]] < r[0][2] + 1:
          values1 = values.copy()
          values1["min_"+r[0][1]] = r[0][2] + 1
          fullrule += find_combinations(r[1],values1)
          values["max_"+r[0][1]] = r[0][2]
        else:
          print("HUUUUUUH2?")


def run_part1():

  print(rules)
  print(parts)

  start = "in"
  good = []

  for part in parts:
    if process_part(start,part):
      good.append(part)

  print(good)

  result = 0
  for one in good:
    result += score(one)

  print(result)

def run_part2():

  result = find_combinations("in",{"min_x": 1, "max_x": 4000,
                                   "min_m": 1, "max_m": 4000,
                                   "min_a": 1, "max_a": 4000,
                                   "min_s": 1, "max_s": 4000})
  print(result)

run_part1()
run_part2()
