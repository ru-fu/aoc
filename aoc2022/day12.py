themap = []
fr = (0,0)
to = (0,0)
max_x = 0
max_y = 0

with open("input12.txt","r") as input:

  for line in input:
    themap.append(['a' if x == "S" else 'z' if x == "E" else x for x in line.strip()])
    findS = line.find("S")
    findE = line.find("E")
    if findS >= 0:
      fr = (findS,len(themap)-1)
    if findE >= 0:
      to = (findE,len(themap)-1)

  max_x = len(themap[0])-1
  max_y = len(themap)-1

def where_to_go(curr,been_to):
  options = []
  real_options = []
  if curr[0] > 0:
    options.append((curr[0]-1,curr[1]))
  if curr[0] < max_x:
    options.append((curr[0]+1,curr[1]))
  if curr[1] > 0:
    options.append((curr[0],curr[1]-1))
  if curr[1] < max_y:
    options.append((curr[0],curr[1]+1))
  for option in options:
    if option in been_to:
      continue
    if ord(themap[option[1]][option[0]]) <= ord(themap[curr[1]][curr[0]])+1:
      real_options.append(option)
  return real_options


def run_part1(fr):

  paths = [[fr]]
  been_to = set(())
  steps = 0

  while paths:
    x = paths.pop(0)
    options = where_to_go(x[-1],been_to)
#    print("Check: "+str(x))
#    print("Paths: "+str(paths))
#    print("Options: "+str(options))
    for option in options:
      if option == to:
        paths = []
        steps = len(x)
        break
      else:
        been_to.add(option)
        new_x = x.copy()
        new_x.append(option)
        paths.append(new_x)

  print(steps)
  return steps

def run_part2():

  all_As = []

  for i,row in enumerate(themap):
    for j,col in enumerate(row):
      if themap[i][j] == "a":
        all_As.append((j,i))

  result = []

  for fr in all_As:
    result.append(run_part1(fr))

  print(min([x for x in result if x > 0]))


#run_part1(fr)
run_part2()
