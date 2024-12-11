import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

stones = []
cache = {}
cache2 = {}
  
with open(inputfile,"r") as input:

  for line in input:
    stones += [int(x) for x in line.rstrip().split(" ")]

def blink(stones):

  new_stones = []

  for stone in stones:
    if stone == 0:
      new_stones.append(1)
    elif len(str(stone)) % 2 == 0:
      firstval = str(stone)[:int(len(str(stone))/2)]
      secondval = str(stone)[int(len(str(stone))/2):]
      new_stones.append(int(firstval))
      new_stones.append(int(secondval))
    else:
      new_stones.append(stone * 2024)

  return new_stones

def blinkx(num,stones):
  global cache

  total = []
  
  for stone in stones:
    if stone in cache:
      total += cache[stone]
    else:
      process = [stone]
      for i in range(num):
        process = blink(process)
      cache[stone] = process
      total += process

  return(total)

def blink_depth(num,stones):

  total = 0
  
  for stone in stones:

    if stone[0] == num - 1:
      this = 1
    if stone in cache:
      this = cache[stone][1]
    elif num > 0:
      new_stones = blink([stone[1]])
      this = blink_depth(num-1,[(num+1,x) for x in new_stones])
    else:
      this = 1
      
    cache[stone] = (num,this)
    total += this
        
  return total
    

  

  print(stone)

def run_part1():

#  print(blinkx(25,stones))
  print(len(blinkx(25,stones)))
#  print("212655")


def run_part2():

  stones2 = [(0,x) for x in stones]

  result = blink_depth(75,stones2)

  print(result)


run_part1()
run_part2()
