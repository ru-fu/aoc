def touching(head, tail):
  if (head[0]-1 <= tail[0] <= head[0]+1) and (head[1]-1 <= tail[1] <= head[1]+1):
    return True
  else:
    return False

def move(which,direction):
  if direction == "R":
    which = (which[0]+1,which[1])
  elif direction == "L":
    which = (which[0]-1,which[1])
  if direction == "U":
    which = (which[0],which[1]+1)
  elif direction == "D":
    which = (which[0],which[1]-1)
  return which

def follow(head, tail, record):
  global trail
  if touching(head,tail):
    return tail
  else:
    if tail[1] == head[1]:
      if tail[0]+2 == head[0]:
        tail = move(tail,"R")
      elif tail[0]-2 == head[0]:
        tail = move(tail,"L")
      else:
        raise Exception("cannot reach")
    elif tail[0] == head[0]:
      if tail[1]+2 == head[1]:
        tail = move(tail,"U")
      elif tail[1]-2 == head[1]:
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
      ### diagonal 1
    elif tail[0]+1 == head[0]:
      if tail[1]+2 == head[1]:
        tail = move(tail,"R")
        tail = move(tail,"U")
      elif tail[1]-2 == head[1]:
        tail = move(tail,"R")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
    elif tail[0]-1 == head[0]:
      if tail[1]+2 == head[1]:
        tail = move(tail,"L")
        tail = move(tail,"U")
      elif tail[1]-2 == head[1]:
        tail = move(tail,"L")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
    elif tail[1]+1 == head[1]:
      if tail[0]+2 == head[0]:
        tail = move(tail,"R")
        tail = move(tail,"U")
      elif tail[0]-2 == head[0]:
        tail = move(tail,"L")
        tail = move(tail,"U")
      else:
        raise Exception("cannot reach")
    elif tail[1]-1 == head[1]:
      if tail[0]+2 == head[0]:
        tail = move(tail,"R")
        tail = move(tail,"D")
      elif tail[0]-2 == head[0]:
        tail = move(tail,"L")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
      ### diagonal 2
    elif tail[0]+2 == head[0]:
      if tail[1]+2 == head[1]:
        tail = move(tail,"R")
        tail = move(tail,"U")
      elif tail[1]-2 == head[1]:
        tail = move(tail,"R")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
    elif tail[0]-2 == head[0]:
      if tail[1]+2 == head[1]:
        tail = move(tail,"L")
        tail = move(tail,"U")
      elif tail[1]-2 == head[1]:
        tail = move(tail,"L")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
    elif tail[1]+2 == head[1]:
      if tail[0]+2 == head[0]:
        tail = move(tail,"R")
        tail = move(tail,"U")
      elif tail[0]-2 == head[0]:
        tail = move(tail,"L")
        tail = move(tail,"U")
      else:
        raise Exception("cannot reach")
    elif tail[1]-2 == head[1]:
      if tail[0]+2 == head[0]:
        tail = move(tail,"R")
        tail = move(tail,"D")
      elif tail[0]-2 == head[0]:
        tail = move(tail,"L")
        tail = move(tail,"D")
      else:
        raise Exception("cannot reach")
    else:
      raise Exception("huh?")

    if record:
      record.add(tail)
    return tail

def run_part1():

  head = (0,0)
  tail = (0,0)
  trail = set(())
  trail.add(tail)

  with open("test.txt","r") as input:

    for line in input:
      ins = line.strip().split(" ")
      print(ins)
      for i in range(int(ins[1])):
        head = move(head,ins[0])
        print("Head: "+str(head))
        tail = follow(head, tail, trail)
        print("Tail: "+str(tail))

  print(len(trail))

def run_part2():

  head = (0,0)
  tail = (0,0)
  knot1 = (0,0)
  knot2 = (0,0)
  knot3 = (0,0)
  knot4 = (0,0)
  knot5 = (0,0)
  knot6 = (0,0)
  knot7 = (0,0)
  knot8 = (0,0)
  trail = set(())
  trail.add(tail)

  with open("input09.txt","r") as input:

    for line in input:
      ins = line.strip().split(" ")
      print(ins)
      for i in range(int(ins[1])):
        head = move(head,ins[0])
        print("Head: "+str(head))
        knot1 = follow(head, knot1, False)
        knot2 = follow(knot1, knot2, False)
        knot3 = follow(knot2, knot3, False)
        knot4 = follow(knot3, knot4, False)
        knot5 = follow(knot4, knot5, False)
        knot6 = follow(knot5, knot6, False)
        knot7 = follow(knot6, knot7, False)
        knot8 = follow(knot7, knot8, False)
        tail = follow(knot8, tail, trail)
        print("Tail: "+str(tail))

  print(len(trail))

run_part1()
run_part2()
