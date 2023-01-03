thegrid = {}
emptyfields = []
gridminute = 0
found = {}

with open("input24.txt","r") as input:

  i = 0
  for line in input:
    for j,char in enumerate(line.strip()):
      if char == "#":
        thegrid[(j,i)] = None
      elif char == ".":
        thegrid[(j,i)] = []
      else:
        thegrid[(j,i)] = [char]
    i += 1

start = [(x,y) for ((x,y),val) in thegrid.items() if y == 0 and not val == None][0]
end = [(x,y) for ((x,y),val) in thegrid.items() if y == i-1 and not val == None][0]
max_y = end[1]
max_x = end[0]+1

def empty_fields(minute):
  global emptyfields

  if len(emptyfields) > minute:
    return emptyfields[minute]
  else:
    calc_empty_fields()
    return empty_fields(minute)

def calc_empty_fields():
  global emptyfields, gridminute

  result = []
  for (coord,val) in thegrid.items():
    if val == []:
      result.append(coord)
  emptyfields.append(result)

  update_grid()

def update_grid():
  global thegrid, gridminute, max_x, max_y

  new_grid = {}

  for coord in thegrid.keys():
    if thegrid[coord] == None:
      new_grid[coord] = None
    elif len(thegrid[coord]) == 0:
      if not coord in new_grid:
        new_grid[coord] = []
    else:
      for char in thegrid[coord]:
        (x,y) = coord
        if char == "^":
          if y-1 <= 0:
            y = max_y
          if (x,y-1) in new_grid and not new_grid[(x,y-1)] == None:
            new_grid[(x,y-1)].append(char)
          else:
            new_grid[(x,y-1)] = [char]
        elif char == "v":
          if y+1 >= max_y:
            y = 0
          if (x,y+1) in new_grid and not new_grid[(x,y+1)] == None:
            new_grid[(x,y+1)].append(char)
          else:
            new_grid[(x,y+1)] = [char]
        elif char == "<":
          if x-1 <= 0:
            x = max_x
          if (x-1,y) in new_grid and not new_grid[(x-1,y)] == None:
            new_grid[(x-1,y)].append(char)
          else:
            new_grid[(x-1,y)] = [char]
        elif char == ">":
          if x+1 >= max_x:
            x = 0
          if (x+1,y) in new_grid and not new_grid[(x+1,y)] == None:
            new_grid[(x+1,y)].append(char)
          else:
            new_grid[(x+1,y)] = [char]
        else:
          raise Exception("huh?")
      if not coord in new_grid:
        new_grid[coord] = []

  thegrid = new_grid.copy()
  gridminute += 1

  print("Grid minute: "+str(gridminute))
#  print_grid()


def print_grid():
  global thegrid

  for i in range(max_y+1):
    row = ""
    for j in range(max_x+1):
      if not (j,i) in thegrid or thegrid[(j,i)] == None:
        row += "#"
      elif len(thegrid[(j,i)]) == 0:
        row += "."
      elif len(thegrid[(j,i)]) == 1:
        row += thegrid[(j,i)][0]
      else:
        row += str(len(thegrid[(j,i)]))
    print(row)


def run_part1():

  options = [[start]]
  min_steps = -1

  while options:
    option = options.pop(0)
#    print(len(options))

    if min_steps > 0 and len(option) > min_steps:
      continue
    else:
      (posx,posy) = option[-1]
#      print(len(option))
      empty = empty_fields(len(option))
      if (posx,posy+1) == end or (posx+1,posy) == end or (posx,posy-1) == end or (posx-1,posy) == end:
        if min_steps < 0 or len(option)+1 < min_steps:
          min_steps = len(option)+1
          print("###################################################"+str(min_steps))
          print(option)
        continue
      if len(option) in found:
        if (posx,posy) in found[len(option)]:
          continue
        else:
          found[len(option)].append((posx,posy))
      else:
        found[len(option)] = [(posx,posy)]
      if (posx,posy+1) in empty:
        op1 = option.copy()
        op1.append((posx,posy+1))
        options.append(op1)
      if (posx+1,posy) in empty:
        op1 = option.copy()
        op1.append((posx+1,posy))
        options.append(op1)
      if (posx,posy-1) in empty:
        op1 = option.copy()
        op1.append((posx,posy-1))
        options.append(op1)
      if (posx-1,posy) in empty:
        op1 = option.copy()
        op1.append((posx-1,posy))
        options.append(op1)
      if (posx,posy) in empty:
        op1 = option.copy()
        op1.append((posx,posy))
        options.append(op1)


  print(min_steps-1)


def run_part2():

  options = [[start]]
  min_steps = -1

  first_pass = []

  while options:
    option = options.pop(0)
#    print(len(options))

    if min_steps > 0 and len(option) > min_steps:
      continue
    else:
      (posx,posy) = option[-1]
#      print(len(option))
      empty = empty_fields(len(option))
      if (posx,posy+1) == end or (posx+1,posy) == end or (posx,posy-1) == end or (posx-1,posy) == end:
        if min_steps < 0 or len(option)+1 < min_steps:
          min_steps = len(option)+1
          first_pass = option.copy()
          first_pass.append(end)
          print("###################################################"+str(min_steps))
          print(option)
        continue
      if len(option) in found:
        if (posx,posy) in found[len(option)]:
          continue
        else:
          found[len(option)].append((posx,posy))
      else:
        found[len(option)] = [(posx,posy)]
      if (posx,posy+1) in empty:
        op1 = option.copy()
        op1.append((posx,posy+1))
        options.append(op1)
      if (posx+1,posy) in empty:
        op1 = option.copy()
        op1.append((posx+1,posy))
        options.append(op1)
      if (posx,posy-1) in empty:
        op1 = option.copy()
        op1.append((posx,posy-1))
        options.append(op1)
      if (posx-1,posy) in empty:
        op1 = option.copy()
        op1.append((posx-1,posy))
        options.append(op1)
      if (posx,posy) in empty:
        op1 = option.copy()
        op1.append((posx,posy))
        options.append(op1)

  options = [first_pass]
  steps1 = min_steps - 1
  min_steps = -1
  found.clear()

  second_pass = []

  while options:
    option = options.pop(0)
#    print(len(options))

    if min_steps > 0 and len(option) > min_steps:
      continue
    else:
      (posx,posy) = option[-1]
#      print(len(option))
      empty = empty_fields(len(option))
      if (posx,posy+1) == start or (posx+1,posy) == start or (posx,posy-1) == start or (posx-1,posy) == start:
        if min_steps < 0 or len(option)+1 < min_steps:
          min_steps = len(option)+1
          second_pass = option.copy()
          second_pass.append(start)
          print("###################################################"+str(min_steps))
          print(option)
        continue
      if len(option) in found:
        if (posx,posy) in found[len(option)]:
          continue
        else:
          found[len(option)].append((posx,posy))
      else:
        found[len(option)] = [(posx,posy)]
      if (posx,posy-1) in empty:
        op1 = option.copy()
        op1.append((posx,posy-1))
        options.append(op1)
      if (posx-1,posy) in empty:
        op1 = option.copy()
        op1.append((posx-1,posy))
        options.append(op1)
      if (posx,posy) in empty:
        op1 = option.copy()
        op1.append((posx,posy))
        options.append(op1)
      if (posx,posy+1) in empty:
        op1 = option.copy()
        op1.append((posx,posy+1))
        options.append(op1)
      if (posx+1,posy) in empty:
        op1 = option.copy()
        op1.append((posx+1,posy))
        options.append(op1)

  options = [second_pass]
  steps2 = min_steps - 1
  min_steps = -1
  found.clear()

  third_pass = []

  while options:
    option = options.pop(0)
#    print(len(options))

    if min_steps > 0 and len(option) > min_steps:
      continue
    else:
      (posx,posy) = option[-1]
#      print(len(option))
      empty = empty_fields(len(option))
      if (posx,posy+1) == end or (posx+1,posy) == end or (posx,posy-1) == end or (posx-1,posy) == end:
        if min_steps < 0 or len(option)+1 < min_steps:
          min_steps = len(option)+1
          third_pass = option.copy()
          third_pass.append(end)
          print("###################################################"+str(min_steps))
          print(option)
        continue
      if len(option) in found:
        if (posx,posy) in found[len(option)]:
          continue
        else:
          found[len(option)].append((posx,posy))
      else:
        found[len(option)] = [(posx,posy)]
      if (posx,posy+1) in empty:
        op1 = option.copy()
        op1.append((posx,posy+1))
        options.append(op1)
      if (posx+1,posy) in empty:
        op1 = option.copy()
        op1.append((posx+1,posy))
        options.append(op1)
      if (posx,posy-1) in empty:
        op1 = option.copy()
        op1.append((posx,posy-1))
        options.append(op1)
      if (posx-1,posy) in empty:
        op1 = option.copy()
        op1.append((posx-1,posy))
        options.append(op1)
      if (posx,posy) in empty:
        op1 = option.copy()
        op1.append((posx,posy))
        options.append(op1)

  print(steps1)
  print(first_pass)
  print(steps2)
  print(second_pass)
  print(min_steps - 1)
  print(third_pass)


#run_part1()
run_part2()
