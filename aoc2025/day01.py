import sys, math

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

dial = 50
count = 0
zeros = 0

def turn(which, howmany):
  global dial, count, zeros

  if which == "L":
      num = dial - howmany
  elif which == "R":
      num = dial + howmany

  rounds = math.floor(howmany /100)

  num = num % 100

  if (num == 0 or dial == 0):
    pass
  elif (which == "R" and num < dial):
    rounds += 1
  elif (which == "L" and dial < num):
    rounds += 1
  
  print("Turn "+which+" from "+str(dial)+ " to "+str(num))
  print("zeros: "+str(rounds))
  print()

  if num == 0:
    count += 1
  
  dial = num
  zeros += rounds

with open(inputfile,"r") as input:

  for line in input:
    turn(line[0],int(line[1:].rstrip()))
       
def run_part1():

  print(count)

def run_part2():

  print(zeros+count)

run_part1()
run_part2()
