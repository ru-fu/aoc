themap = {}
valves = {}

with open("input16.txt","r") as input:
#with open("test.txt","r") as input:

  for line in input:
    split = line.strip().split(";")
    valve = split[0][6:8]
    rate = split[0].split("=")[1]
    split1 = split[1].split(", ")
    leads_to = [split1[0][-2:]]
    split1.pop(0)
    leads_to.extend(split1)
    themap[valve]=leads_to
    valves[valve]=int(rate)

class State:

  def __init__(self):
    self.openvalves = [x for x in valves if valves[x] == 0]
    self.position = "AA"
    self.elposition = "AA"
    self.visited_open = []
    self.el_visited = []
    self.released = 0
    self.minute = 0
    self.max_inc = sum(valves.values())

  def __str__(self):
    return "Minute: "+str(self.minute)+" Open valves: "+str(self.openvalves)+" Visited open: "+str(self.visited_open)+" Released: "+str(self.released)+" You: "+self.position+" Elephant: "+self.elposition

  def copy(self):
    new_state = State()
    new_state.openvalves = self.openvalves.copy()
    new_state.position = self.position
    new_state.elposition = self.elposition
    new_state.visited_open = self.visited_open.copy()
    new_state.el_visited = self.el_visited.copy()
    new_state.released = self.released
    new_state.minute = self.minute
    return new_state

  def where_to_go(self, who = "you"):
    if who == "you":
      next_moves = [x for x in themap[self.position] if not x in self.visited_open]
    else:
      next_moves = [x for x in themap[self.elposition] if not x in self.el_visited]
    return next_moves

  def openvalve(self, who = "you"):
    if who == "you":
      self.new_minute()
      self.openvalves.append(self.position)
      self.visited_open = []
    else:
      self.openvalves.append(self.elposition)
      self.el_visited = []

  def move(self,where, who = "you"):
    if who == "you":
      self.new_minute()
      self.visited_open.append(self.position)
      self.position = where
    else:
      self.el_visited.append(self.position)
      self.elposition = where

  def stay(self, who = "you"):
    if who == "you":
      self.new_minute()

  def new_minute(self):
    self.minute += 1
    for valve in self.openvalves:
      self.released += valves[valve]

  def check(self,max_value):
    if self.minute == 26:
#      print(self.released)
      return self.released
    if self.minute > 26:
      raise Exception("huh?")
    if self.released + ((26 - self.minute) * self.max_inc) < max_value:
      return -1
    if len(self.openvalves) == len(valves):
      self.released += (26 - self.minute) * self.max_inc
      self.minute = 26
      return self.released
    return 0

def run_part1(minutes = 30):

  print(themap)
  print(valves)

  paths = [State()]
  max_value = 0
  max_openvalves = []
  steps = 0
  max_inc = sum(valves.values())

  while paths:
    path = paths.pop()
    steps += 1
    if steps % 50000 == 0:
      print("*"+str(len(paths))+"*")
    if path.minute == minutes:
      if path.released > max_value:
        max_value = path.released
        max_openvalves = path.openvalves
        print(max_value)
    elif path.released + ((minutes - path.minute) * max_inc) < max_value:
      continue
    elif path.minute > minutes:
      raise Exception("huh?")
    elif len(path.openvalves) == len(valves):
      path.stay()
      paths.append(path)
    else:
      if not path.position in path.openvalves:
        newpath = path.copy()
        newpath.openvalve()
        paths.append(newpath)
      nextmoves = path.where_to_go()
      if path.minute == minutes:
        values.append(path.released)
        continue
      if len(nextmoves) == 0:
        path.stay()
        paths.append(path)
      else:
        for move in nextmoves:
          newpath = path.copy()
          newpath.move(move)
          paths.append(newpath)

  print(max_value)
  print(max_openvalves)
  return (max_value,max_openvalves)


def run_part2():

  paths = [State()]
  max_value = 0
  steps = 0
  max_inc = sum(valves.values())
  total_max = 2087
#  total_max = 1651

  while paths:
    #paths.sort(key = lambda a : a.released)
    path = paths.pop()
    themax = max([max_value,total_max])
    thecheck = path.check(themax)
    if thecheck > max_value:
      max_value = thecheck
      print("####################################### "+str(max_value))
    elif thecheck == -1:
      continue
    else:
      steps += 1
      if steps % 50000 == 0:
        print("*"+str(len(paths))+"* Minute: "+str(path.minute)+" Released: "+str(path.released))
#        print("Potential "+ str(path.released + ((26 - path.minute) * path.max_inc)))
        print(len(path.openvalves))

      new_paths_you = []
      if not path.position in path.openvalves:
        if max([valves[x] for x in valves if x not in path.openvalves]) > valves[path.position]:
          newpath = path.copy()
          newpath.openvalve("you")
          new_paths_you.append(newpath)
        else:
          path.openvalve("you")
      nextmoves = path.where_to_go("you")
      for y in nextmoves:
        if not y in path.openvalves and valves[y] == max([valves[x] for x in valves if x not in path.openvalves]):
          nextmoves = [y]
          break
      if path.minute == 26:
        if path.released > max_value:
          max_value = path.released
          print("#######################################"+str(max_value))
        continue
      if len(nextmoves) == 0:
        path.stay("you")
        new_paths_you.append(path)
      else:
        for move in nextmoves:
          newpath = path.copy()
          newpath.move(move,"you")
          new_paths_you.append(newpath)
      for your_path in new_paths_you:
        if not your_path.elposition in your_path.openvalves:
          if max([valves[x] for x in valves if x not in your_path.openvalves]) > valves[your_path.position]:
            newpath = your_path.copy()
            newpath.openvalve("el")
            paths.append(newpath)
          else:
            path.openvalve("el")
        nextmoves = your_path.where_to_go("el")
        for y in nextmoves:
          if not y in your_path.openvalves and valves[y] == max([valves[x] for x in valves if x not in your_path.openvalves]):
            nextmoves = [y]
            break
        if your_path.minute == 26:
          if your_path.released > max_value:
            max_value = your_path.released
            print("#######################################"+str(max_value))
          continue
        if len(nextmoves) == 0:
          your_path.stay("el")
          paths.append(your_path)
        else:
          for move in nextmoves:
            newpath = your_path.copy()
            newpath.move(move,"el")
            paths.append(newpath)

  print(max_value)


def run_part2_2():

  (res1,open1) = run_part1(26)

#  res1 = 1515
#  open1 = ['OR', 'VO', 'BV', 'OF', 'YZ', 'EJ', 'FM', 'QD', 'XC', 'WZ', 'AT', 'MZ', 'WI', 'YD', 'QX', 'AA', 'VX', 'VN', 'RD', 'QR', 'CD', 'RJ', 'MC', 'FH', 'DE', 'DY', 'UU', 'CS', 'KY', 'KK', 'ZV', 'QQ', 'OH', 'ZP', 'AR', 'GV', 'PE', 'ZE', 'XL', 'OQ', 'MG', 'LS', 'YI', 'UA', 'AW', 'EL', 'OY', 'FL', 'EG']

  new_valves = {}
  for x in valves:
    if valves[x] == 0:
      new_valves[x] = valves[x]
    elif not x in open1:
      new_valves[x] = valves[x]

  valves.clear()
  valves.update(new_valves)

  for x in themap:
    for nxt in themap[x]:
      if not nxt in valves:
        themap[x].remove(nxt)

  (res2, open2) = run_part1(26)

  print(str(res1 + res2))


#run_example()
#run_part1()
#run_part2()
run_part2_2()
