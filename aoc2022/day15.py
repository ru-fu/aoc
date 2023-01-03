sensors = []
beacons = set(())

class Sensor:

  def __init__(self,x,y,beacon):
    self.x = int(x)
    self.y = int(y)
    self.beacon = [int(x) for x in beacon]
    self.md = Sensor.manhattan([self.x,self.y],self.beacon)
    self.min_x = self.x - self.md
    self.max_x = self.x + self.md
    self.min_y = self.y - self.md
    self.max_y = self.y + self.md

  def __str__(self):
    return "X: "+str(self.x)+" Y: "+str(self.y)+" Beacon: "+str(self.beacon)+" Manhattan: "+str(self.md)

  def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

  def line_coverage(self,line,covered):
    if line < self.min_y or line > self.max_y:
      return []
    else:
      collect = []
      for i in range(self.min_x,self.max_x+1):
        if (i,line) in covered:
          continue
        elif Sensor.manhattan([i,line],[self.x,self.y]) <= self.md:
          collect.append((i,line))
      return collect

  def line_coverage2(self,line):
    if line < self.min_y or line > self.max_y:
      return None
    else:
      if self.y > line:
        offset = self.y - line
      else:
        offset = line - self.y
      return (self.min_x + offset, self.max_x - offset)

  def check(self,x):
    return Sensor.manhattan(x,[self.x,self.y]) <= self.md

class Line:

  def __init__(self):
    self.coverage = []

  def __str__(self):
    return str(self.coverage)

  def add(self,fr,to):
    self.coverage.append((fr,to))
    self.coverage.sort(key = lambda a : a[0])
    length = 0
    while not length == len(self.coverage):
      length = len(self.coverage)
      self.cleanup_coverage()

  def cleanup_coverage(self):
    new_coverage = []
    while len(self.coverage) > 0:
      curr = self.coverage.pop(0)
      if len(self.coverage) > 0 and curr[1]+1 >= self.coverage[0][0]:
        nxt = self.coverage.pop(0)
        if curr[1] > nxt[1]:
          new_coverage.append((curr[0],curr[1]))
        else:
          new_coverage.append((curr[0],nxt[1]))
      else:
        new_coverage.append(curr)
    self.coverage = new_coverage

  def included(self,i):
    for x in self.coverage:
      if x[0] <= i <= x[1]:
        return True
    return False

with open("input15.txt","r") as input:

  for line in input:
    split = line.strip().split(":")
    split1 = split[0].split("=")
    x1 = split1[1][:-3]
    y1 = split1[2]
    split2 = split[1].split("=")
    x2 = split2[1][:-3]
    y2 = split2[2]
    sensors.append(Sensor(x1,y1,(x2,y2)))
    beacons.add((int(x2),int(y2)))

def get_md(x):
  return x.md


def run_part1():

  covered = set(())
  checkline = 2000000

  sensors.sort(key = get_md)

  for sensor in sensors:
    if sensor.y == checkline:
      covered.add([sensor.x,sensor.y])
    covered.update(sensor.line_coverage(checkline,covered))
    print(sensor)

  for beacon in beacons:
    covered.discard(beacon)

#  print(covered)
  print(len(covered))

def run_part1_2():

  covered = Line()
  checkline = 2000000

  sensors.sort(key = get_md)
  sensors.reverse()

  for sensor in sensors:
    rnge = sensor.line_coverage2(checkline)
    print(rnge)
    if rnge:
      covered.add(rnge[0],rnge[1])
    print(sensor)

  count = 0
  for i in range(covered.coverage[0][0],covered.coverage[0][1]+1):
    count += 1

  sub = 0

  for beacon in beacons:
    if beacon[1] == checkline and covered.included(beacon[0]):
      print(beacon)
      sub += 1

  print(covered)
  print(count-sub)

def run_part2():

  sensors.sort(key = get_md)
  sensors.reverse()

  potentially = {}

  for i in range(4000001):
    if i % 100000 == 0:
      print(i)
    covered = Line()

    for sensor in sensors:
      rnge = sensor.line_coverage2(i)
      if rnge:
        if rnge[0] < 0:
          fr = 0
        else:
          fr = rnge[0]
        if rnge[1] > 4000000:
          to = 4000000
        else:
          to = rnge[1]
        covered.add(fr,to)
      #print(sensor)

    if len(covered.coverage) == 1 and covered.coverage[0][0] == 0 and covered.coverage[0][1] == 4000000:
      continue
    else:
      potentially[i] = covered

  for maybe in potentially:
    print(maybe)
    print(potentially[maybe])

#run_part1()
#run_part1_2()
run_part2()
