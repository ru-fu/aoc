import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

keys = []
locks = []
keyvals = []
lockvals = []

with open(inputfile,"r") as input:

  find = None
  key = []
  lock = []

  for line in input:
    line = line.rstrip()
    if not find and line.startswith("#"):
      find = "Lock"
    elif not find and line.startswith("."):
      find = "Key"
    elif find == "Lock" and len(line) == 0:
      locks.append(lock)
      lock = []
      find = None
    elif find == "Key" and len(line) == 0:
      keys.append(key)
      key = []
      find = None
    elif find == "Lock":
      lock.append(line)
    elif find == "Key":
      key.append(line)

  if find == "Lock":
    locks.append(lock)
  elif find == "Key":
    keys.append(key)

def convert(which):

  val = []
  vals = []

  for one in which:
    for i in range(len(one[0])):
      count = 0
      for line in one:
        if line[i] == "#":
          count += 1
      val.append(count)
      count = 0

    vals.append(tuple(val))
    val = []

  return vals

def run_part1():

  print(locks)
  print(keys)
  keyvals = convert(keys)
  lockvals = convert(locks)
  print(lockvals)

  max = len(keys[0])

  valid = 0
  for lock in lockvals:
    for key in keyvals:
      ok = True
      for i,val in enumerate(lock):
        if val + key[i] > max:
          ok = False
      if ok:
        valid += 1

  print(valid)


def run_part2():

  print("result")

run_part1()
run_part2()
