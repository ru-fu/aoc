import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

order = {}
updates = []
  
with open(inputfile,"r") as input:

  for line in input:
    if '|' in line:
      spl = line.rstrip().split('|')
      if spl[0] in order:
        order[spl[0]].append(spl[1])
      else:
        order[spl[0]] = [spl[1]]
    elif ',' in line:
      updates.append(line.rstrip().split(','))

def valid_pos(seen,now):
  global order

  if now in order:
    for later in order[now]:
      if later in seen:
        return False

  return True

def valid_pos2(seen,now):
  global order

  if now in order:
    for later in order[now]:
      if later in seen:
        return later

  return "OK"

def sortit(pages):

  out = []
  todo = pages

  while len(todo) > 0:
    page = todo.pop(0)

    result = valid_pos2(out,page)

    while not result == "OK":
      out.remove(result)
      todo.insert(0, result)
      result = valid_pos2(out,page)

    out.append(page)
    
  return out
      
valid = []

def run_part1():

  for one in updates:
    seen = []
    ok = 1
    for page in one:
      if valid_pos(seen,page):
        seen.append(page)
      else:
        ok = 0
        break
    if ok:
      valid.append(one)

  print(valid)
  middle = [int(x[int((len(x)-1)/2)]) for x in valid]
  print(sum(middle))

  
def run_part2():

  correct = []

  for one in updates:
    if not one in valid:
      correct.append(sortit(one))

  print(correct)
  middle = [int(x[int((len(x)-1)/2)]) for x in correct]
  print(sum(middle))

run_part1()
run_part2()
