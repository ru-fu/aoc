import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

themap = []
rolls = set()
  
with open(inputfile,"r") as input:

  for line in input:
    if len(line) > 1:
      themap.append(line.rstrip())

  
max_rows = len(themap)
max_cols = len(themap[0])
      
for r,row in enumerate(themap):
  print(row)
  for c,col in enumerate(row):
    if col == "@":
      rolls.add((r,c))

def check(roll):

  global rolls

  nbs = [(roll[0]-1,roll[1]-1), (roll[0]-1,roll[1]), (roll[0]-1,roll[1]+1),
         (roll[0],roll[1]-1), (roll[0],roll[1]+1),
         (roll[0]+1,roll[1]-1), (roll[0]+1,roll[1]), (roll[0]+1,roll[1]+1)]

  count = 0
  
  for nb in nbs:
    if count >= 4:
      return 0
    if nb in rolls:
      count += 1

  if count >= 4:
    return 0
  else:
    return 1
      
def run_part1():

  accessible = set()

  for roll in rolls:
    if check(roll):
      accessible.add(roll)
    
  print(accessible)
  print(len(accessible))

def run_part2():

  removed = 0

  while 1:

    accessible = set()

    for roll in rolls:
      if check(roll):
        accessible.add(roll)

    if len(accessible) == 0:
      break
    else:
      print("Removing "+str(len(accessible)))
      removed += len(accessible)
      rolls.difference_update(accessible)

  print(removed)
  
run_part1()
run_part2()
