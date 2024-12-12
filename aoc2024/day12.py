import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

plants = {}
regions = {}
fences = {}
corners = {}
  
with open(inputfile,"r") as input:

  for i,line in enumerate(input):
    for j, plant in enumerate(line.rstrip()):
      if plant in plants:
        plants[plant].append((i,j))
      else:
        plants[plant] = [(i,j)]

def calc_regions(plant):
  (which,plots) = plant

  while len(plots) > 0:
    plot = plots.pop(0)
    region = [plot]
    toprocess = [plot]
    while len(toprocess) > 0:
      plot = toprocess.pop(0)
      for nb in [(plot[0]-1,plot[1]),(plot[0]+1,plot[1]),(plot[0],plot[1]-1),(plot[0],plot[1]+1)]:
        if nb in plots:
          plots.remove(nb)
          region.append(nb)
          toprocess.append(nb)
          
    if which in regions:
      regions[which].append(region)
    else:
      regions[which] = [region]

def calc_fences(plant):
  (which,regs) = plant

  for reg in regs:
    total = 0
    for plot in reg:
      for nb in [(plot[0]-1,plot[1]),(plot[0]+1,plot[1]),(plot[0],plot[1]-1),(plot[0],plot[1]+1)]:
        if not nb in reg:
          total += 1
    if which in fences:
      fences[which].append(total)
    else:
      fences[which]=[total]

def calc_corners(plant):
  (which,regs) = plant

  for reg in regs:
    total = 0
    for plot in reg:
      for corner in [((plot[0],plot[1]-1),(plot[0]-1,plot[1]),(plot[0]-1,plot[1]-1)),
                     ((plot[0]-1,plot[1]),(plot[0],plot[1]+1),(plot[0]-1,plot[1]+1)),
                     ((plot[0],plot[1]+1),(plot[0]+1,plot[1]),(plot[0]+1,plot[1]+1)),
                     ((plot[0]+1,plot[1]),(plot[0],plot[1]-1),(plot[0]+1,plot[1]-1))]:
        if (not corner[0] in reg) and (not corner[1] in reg):
          total += 1
        elif corner[0] in reg and corner[1] in reg and not corner[2] in reg:
          total += 1
    if which in corners:
      corners[which].append(total)
    else:
      corners[which]=[total]

def calc_price(which,plant):

  total = 0

  for i,reg in enumerate(regions[plant]):
    area = len(reg)
    fence = fences[plant][i]
    if which == 2:
      fence = corners[plant][i]
    total += area * fence

  return total

def run_part1():

  print(plants)

  for plant in plants.items():
    calc_regions(plant)

  for regs in regions.items():
    calc_fences(regs)

  print(regions)
  print(fences)

  total = []
  for plant in plants.keys():
    total.append(calc_price(1,plant))

  print(total)
  print(sum(total))

def run_part2():

  for regs in regions.items():
    calc_corners(regs)

  print(corners)
  
  total = []
  for plant in plants.keys():
    total.append(calc_price(2,plant))

  print(total)
  print(sum(total))
  
run_part1()
run_part2()
