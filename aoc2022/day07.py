class Dir:

  def __init__(self,name):
    self.name = name+"/"
    self.size = -1
    self.files = {}
    self.subdir = {}

  def __str__(self):
    ret = self.name
    ret += " ("+str(self.size)+")\n"
    for x in self.files:
      ret += "-"+x
      ret += " ("+str(self.files[x])+")\n"
    for x in self.subdir:
      ret += str(self.subdir[x])
    return ret

  def add_file(self,name,size):
    self.files[name] = int(size)

  def add_dir(self,name):
    self.subdir[name] = Dir(self.name+name)

  def has_subdir(self,name):
    return name in self.subdir

  def has_file(self,name):
    return name in self.files

  def get_dir(self,name):
    return self.subdir[name]

  def get_subdirs(self):
    return list(self.subdir.values())

  def get_size(self):
    if self.size == -1:
      self.calc_size()
    return self.size

  def calc_size(self):
    size = 0
    for x in self.files:
      size += self.files[x]
    for x in self.subdir:
      size += self.subdir[x].get_size()
    self.size = size

pwd = []

with open("input07.txt","r") as input:

  for line in input:
    if line.startswith("$ cd .."):
      pwd.pop()
    elif line.startswith("$ cd "):
      if len(pwd) > 0 and pwd[-1].has_subdir(line.strip()[5:]):
        pwd.append(pwd[-1].get_dir(line.strip()[5:]))
      else:
        newDir = Dir("")
        pwd.append(newDir)
    elif line.startswith("$ ls"):
      continue
    elif line.startswith("dir "):
      if not pwd[-1].has_subdir(line.strip()[4:]):
        pwd[-1].add_dir(line.strip()[4:])
    else:
      info = line.strip().split(" ")
      if not pwd[-1].has_file(info[1]):
        pwd[-1].add_file(info[1],info[0])


def run_part1():

  test = Dir("")
  test.add_file("a","123")
  test.add_dir("b")
  test2 = test.get_dir("b")
  test2.add_file("a","456")
  test.get_size()

  pwd[0].get_size()

  small_dirs = []
  check = [pwd[0]]

  while len(check) > 0:
    one = check.pop()
    if one.get_size() <= 100000:
      small_dirs.append(one.get_size())
    check = check + one.get_subdirs()

  print(pwd[0])
  print(small_dirs)
  print(sum(small_dirs))

def run_part2():

  big_dirs = []
  check = [pwd[0]]
  needed = pwd[0].get_size() - 40000000

  while len(check) > 0:
    one = check.pop()
    if one.get_size() >= needed:
      big_dirs.append(one.get_size())
    check = check + one.get_subdirs()

  print(needed)
  print(big_dirs)
  print(min(big_dirs))

run_part1()
run_part2()
