import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

shapes = []
sizes = []
areas = []
  
with open(inputfile,"r") as input:

  shape = []
  
  for line in input:
    if "x" in line:
      one = line.rstrip().split(": ")
      size = [int(x) for x in one[0].split("x")]
      amounts = [int(x) for x in one[1].split(" ")]
      areas.append((size[0],size[1],amounts))
    elif ":" in line:
      shape = []
    elif len(line.rstrip()) == 0:
      shapes.append(shape)
    else:
      shape.append(line.rstrip())

for shape in shapes:
  count = 0
  for one in shape:
    for char in one:
      if char == "#":
        count +=1
  sizes.append(count)
    
def run_part1():

  print(shapes)
  print(sizes)
  print(areas)

  fits = 0
  doesnt = 0

  for area in areas:
    if sum(area[2]) * 9 <= area[0] * area[1]:
      #print("Big enough! Available: "+str(area[0] * area[1])+" Needed at max: "+str(sum(area[2]) * 9))
      fits += 1
    else:
      needed = 0
      for i,size in enumerate(sizes):
        needed += area[2][i] * size
      if needed > area[0] * area[1]:
        #print("Too small. Available: "+str(area[0] * area[1])+" Needed at least: "+str(needed))
        doesnt += 1
      else:
        print(area)
        print("Hmm ... Available: "+str(area[0] * area[1])+" Needed at least: "+str(needed)+" Needed at max: "+str(sum(area[2]) * 9))

  print("Fits: "+str(fits)+" Doesn't: "+str(doesnt))
  

def run_part2():

  print("result")

run_part1()
run_part2()
