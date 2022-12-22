grid = []
instructions = []

with open("input22.txt","r") as input:
  end = False

  for line in input:
    if line.strip() == "":
      end = True
    elif end:
      direction = "X"
      count = ""
      for x in line.strip():
        if x.isdigit():
          count += x
        else:
          instructions.append((direction,int(count)))
          direction = x
          count = ""
      instructions.append((direction,int(count)))
    else:
      row = []
      for x in line.rstrip():
        row.append(x)
      grid.append(row)

  lengths = [len(x) for x in grid]
  max_length = max(lengths)+1

  empty_row = []
  for x in range(max_length):
    empty_row.append(" ")
  new_grid = [empty_row]
  for row in grid:
    if len(row) < max_length:
      new_row = [" "]
      for i in range(max_length):
        if i < len(row):
          new_row.append(row[i])
        else:
          new_row.append(' ')
      new_grid.append(new_row)
    else:
      new_grid.append(row)
  grid = new_grid
  grid.append(empty_row)


def move(position,direction):
  if direction == "right":
    new_x = position[0]+1
    new_y = position[1]
    if new_x < len(grid[new_y]):
      if grid[new_y][new_x] == ".":
        return (new_x,new_y)
      elif grid[new_y][new_x] == "#":
        return position
      elif grid[new_y][new_x] == " ":
        new_pos = move((new_x,new_y),"right")
        if grid[new_pos[1]][new_pos[0]] == ".":
          return new_pos
        else:
          return position
    else:
      new_pos = move((-1,new_y),"right")
      if grid[new_pos[1]][new_pos[0]] == ".":
        return new_pos
      else:
        return position
  elif direction == "left":
    new_x = position[0]-1
    new_y = position[1]
    if new_x >= 0:
      if grid[new_y][new_x] == ".":
        return (new_x,new_y)
      elif grid[new_y][new_x] == "#":
        return position
      elif grid[new_y][new_x] == " ":
        new_pos = move((new_x,new_y),"left")
        if grid[new_pos[1]][new_pos[0]] == ".":
          return new_pos
        else:
          return position
    else:
      new_pos = move((len(grid[new_y])-1,new_y),"left")
      if grid[new_pos[1]][new_pos[0]] == ".":
        return new_pos
      else:
        return position
  if direction == "down":
    new_x = position[0]
    new_y = position[1]+1
    if new_y < len(grid):
      if grid[new_y][new_x] == ".":
        return (new_x,new_y)
      elif grid[new_y][new_x] == "#":
        return position
      elif grid[new_y][new_x] == " ":
        new_pos = move((new_x,new_y),"down")
        if grid[new_pos[1]][new_pos[0]] == ".":
          return new_pos
        else:
          return position
    else:
      new_pos = move((new_x,-1),"down")
      if grid[new_pos[1]][new_pos[0]] == ".":
        return new_pos
      else:
        return position
  if direction == "up":
    new_x = position[0]
    new_y = position[1]-1
    if new_y >= 0:
      if grid[new_y][new_x] == ".":
        return (new_x,new_y)
      elif grid[new_y][new_x] == "#":
        return position
      elif grid[new_y][new_x] == " ":
        new_pos =  move((new_x,new_y),"up")
        if grid[new_pos[1]][new_pos[0]] == ".":
          return new_pos
        else:
          return position
    else:
      new_pos = move((new_x,len(grid)-1),"up")
      if grid[new_pos[1]][new_pos[0]] == ".":
        return new_pos
      else:
        return position

def score(position,facing):
  if facing == "right":
    score = 0
  elif facing == "down":
    score = 1
  elif facing == "left":
    score = 2
  elif facing == "up":
    score = 3
  return score + 1000 * (position[1]) + 4 * (position[0])

def run_part1():

#  print(grid)
#  print(instructions)

  position = (0,0)
  for i,x in enumerate(grid[1]):
    if x == ".":
      position = (i,1)
      break
  facing = "right"

  for (direction,count) in instructions:
    if not direction == "X":
      if facing == "right":
        if direction == "R":
          facing = "down"
        else:
          facing = "up"
      elif facing == "down":
        if direction == "R":
          facing = "left"
        else:
          facing = "right"
      elif facing == "left":
        if direction == "R":
          facing = "up"
        else:
          facing = "down"
      elif facing == "up":
        if direction == "R":
          facing = "right"
        else:
          facing = "left"
    print("Move "+str(count)+" "+facing)
    for i in range(count):
      new_pos = move(position,facing)
      if new_pos == position:
        break
      else:
        position = new_pos

    print(position)

  print(score(position,facing))

def run_part2():

  print("result")

run_part1()
run_part2()
