import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

walls = []
start = None
end = None
max_x = 0
max_y = 0
  
with open(inputfile,"r") as input1:

  for i,line in enumerate(input1):
    line = line.rstrip()
    for j,val in enumerate(line):
      if val == "#":
        walls.append((i,j))
      elif val == "S":
        start = (i,j)
      elif val == "E":
        end = (i,j)
      if j > max_y:
        max_y = j
    max_x = i

def find_path():
  global start, end, walls, max_x, max_y

  where = start
  path = []

  while not where == end:
    (x,y) = where
    for step in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
      if ((0 <= step[0] <= max_x) and
          (0 <= step[1] <= max_y) and
          (not step == start) and
          (not step in path) and
          (not step in walls)):
        path.append(step)
        where = step
        break

  return path

def find_shortcuts(where):
  global walls, max_x, max_y, start

  options = []
  (x,y) = where
  for stepone in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if stepone in walls:
      (x1,y1) = stepone
      for steptwo in [(x1+1,y1),(x1-1,y1),(x1,y1+1),(x1,y1-1)]:
        if ((0 <= steptwo[0] <= max_x) and
            (0 <= steptwo[1] <= max_y) and
            (not steptwo == start) and
            (not steptwo == where) and
            (not steptwo in walls)):
          options.append(steptwo)

  return options


def find_shortcutsx(fr):
  global walls, max_x, max_y, start, time

  #print("Check "+str(fr)+" ("+str(steps)+") "+str(path))

  options = set()
  (x,y) = fr

  for stepone in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if stepone in walls:
      (x1,y1) = stepone
  
      for i in range(0,time-1):
        for j in range(0,time-1):
          if i+j <= time-1:
        
            for step in [ (x1+i,y1+j), (x1+i,y1-j), (x1-i,y1+j), (x1-i,y1-j)]:
              if ((0 <= step[0] <= max_x) and
                  (0 <= step[1] <= max_y) and
                  (not step == start)):
                  options.add((step,i+j+1))
                  if fr == (3,1) or fr == (2,1):
                    print(str(fr)+" "+str(step))
                    print(str(i+j))
        
  return options

def find_shortcuts3(fr):
  global walls, max_x, max_y, start, time

  #print("Check "+str(fr)+" ("+str(steps)+") "+str(path))

  options = set()
  (x,y) = fr
  
  for i in range(0,time+1):
    for j in range(0,time+1):
      if i+j <= time:
        #print(str(i)+" "+str(j))
        
        for step in [ (x+i,y+j), (x+i,y-j), (x-i,y+j), (x-i,y-j)]:
          #if i+j == 1 and not step in walls:
          #  continue
          if ((0 <= step[0] <= max_x) and
              (0 <= step[1] <= max_y) and
              (not step == start) and
              (not step in walls)):
            options.add((step,i+j+1))
            #if fr == (3,1) or fr == (2,1):
            #  print(str(fr)+" "+str(step))
            #  print(str(i+j))
        
  return options

def eval_shortcuts():

  global savehowmuch, path

  shortcuts = []

  for i,field in enumerate(path):
    options = find_shortcuts(field)
    
    for o in options:
      print(field)
      print(o)
      print(path[i+savehowmuch+1:])
      if o in path[i+savehowmuch+1:]:
        print("Can cut from "+str(field)+" to "+str(o))
        #print(path)
        #print(path[i+savehowmuch+1:])
        shortcuts.append((field,o))

  return shortcuts

def eval_shortcuts2():

  global path

  shortcuts = {}

  for i,field in enumerate(path):
    print(i)
    options = find_shortcuts3(field)
    #print(str(field)+" - "+str(options))
      
    for o in options:
      if o[0] in path[i+1:]:
        #print("Can cut from "+str(field)+" to "+str(o))
        fullpath = path[:path.index(field)]
        fullpath = fullpath + path[path.index(o[0])+1:]
        #print(path)
        #print(fullpath)
        #print(len(fullpath)+o[1])
        if (not (field,o[0]) in shortcuts) or len(fullpath)+o[1] < shortcuts[(field,o[0])]:
          shortcuts[(field,o[0])] = len(fullpath)+o[1]
       

  return shortcuts
  
savehowmuch = 2
time = 2

path = find_path()
path.insert(0,start)
print(path)
print(len(path))

def run_part1():

  shortcuts = eval_shortcuts()

  print(len(shortcuts))

def run_part2():
  global savehowmuch, time

  savehowmuch = 100
  time = 20

  shortcuts = eval_shortcuts2()
  result = [shortcuts[x] for x in shortcuts if len(path) - shortcuts[x] >= savehowmuch]

 # print(shortcuts)
 # print(result)

  count = {}
  for r in result:
    if r in count:
      count[r] += 1
    else:
      count[r] = 1
  
  print(len(result))
  #print([x for x in shortcuts if shortcuts[x] == 13])


#run_part1()
run_part2()

# 864271 too low
# 980629 too low
# 1070213 too high
