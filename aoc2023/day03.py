import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

numbers = {}
symbols = {}
ID = 0

def write_num(number,where):

  global numbers, ID

  if number:

    for w in where:
      if w in numbers:
        print("HUH?! "+str(w)+" "+number+" "+str(where))
        exit(0)
      else:
        numbers[w] = (int(number),ID)

    ID += 1

with open(inputfile,"r") as input:

  for x,line in enumerate(input):

    number = ""
    where = []

    for y,char in enumerate(line.strip()):

      if char.isdigit():

        number += char
        where.append((x,y))

      elif char == ".":

        if number:

          write_num(number, where)
          number = ""
          where = []

      else:

        symbols[(x,y)] = char
        write_num(number, where)
        number = ""
        where = []

    write_num(number, where)

def run_part1():

 # print(numbers)
 # print(symbols)

  adjacent = set()

  for symbol in symbols:

    for coord in [(symbol[0]-1,symbol[1]-1),(symbol[0]-1,symbol[1]),(symbol[0]-1,symbol[1]+1),
                  (symbol[0],symbol[1]-1),(symbol[0],symbol[1]+1),
                  (symbol[0]+1,symbol[1]-1),(symbol[0]+1,symbol[1]),(symbol[0]+1,symbol[1]+1)]:
      if coord in numbers:
        adjacent.add(numbers[coord])


  nums = [x for (x,y) in adjacent]
  print(sorted(nums))
  print(sum(nums))

def run_part2():

  gears = []

  for symbol in symbols:

    adjacent = set()

    if symbols[symbol] == "*":

      for coord in [(symbol[0]-1,symbol[1]-1),(symbol[0]-1,symbol[1]),(symbol[0]-1,symbol[1]+1),
                    (symbol[0],symbol[1]-1),(symbol[0],symbol[1]+1),
                    (symbol[0]+1,symbol[1]-1),(symbol[0]+1,symbol[1]),(symbol[0]+1,symbol[1]+1)]:
        if coord in numbers:
          adjacent.add(numbers[coord])

      if len(adjacent) == 2:

        nums = [x for (x,y) in adjacent]
        gears.append(nums[0] * nums[1])

  print(gears)
  print(sum(gears))

run_part1()
run_part2()
