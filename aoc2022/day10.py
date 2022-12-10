record_when = [20,60,100,140,180,220]
signal_strengths = []

def record(cycle,x):
  global record_when, signal_strengths
  if cycle in record_when:
    signal_strengths.append(cycle * x)

with open("input10.txt","r") as input:

  x = 1
  cycle = 0
  sprite = []

  for line in input:
    if line.strip() == "noop":
      cycle += 1
#      record(cycle,x)
      sprite.append(x)
    elif line.startswith("addx"):
      cycle += 1
#      record(cycle,x)
      sprite.append(x)
      cycle += 1
#      record(cycle,x)
      sprite.append(x)
      x += int(line.strip()[5:])

def run_part1():

#  print(sum(signal_strengths))
#  print(signal_strengths)

  new_sum = 0
  for i in record_when:
    new_sum += i * sprite[i-1]

  print(new_sum)

def run_part2():

  out = ""

  for i in range(len(sprite)):
    cycle = i+1
    crt = i % 40
    if crt == 0:
      out += "\n"
    if sprite[i]-1 <= crt <= sprite[i]+1:
      out += "#"
    else:
      out += "."

  print(out)

run_part1()
run_part2()
