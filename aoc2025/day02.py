import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  ranges = []
  
  for line in input:
    for r in line.rstrip().split(","):
      one = r.split("-")
      if len(one) > 1:
        ranges.append((int(one[0]), int(one[1])))

def check(num):
  num = str(num)
  length = len(num)

  if length % 2 == 0:
    middle = int(length/2)
  else:
     return None

  for i in range(middle):
    if num[i] == num[middle+i]:
      pass
    else:
      #print(num)
      return None

  return num

def check2(num):
  num = str(num)
  length = len(num)

  for div in range(2,length+1):

    if length % div == 0:
      middle = int(length/div)
    else:
      continue

    yep=True
    for i in range(middle):
      for j in range(1,div):
        #print("Check "+num+", divide by "+str(div)+": Compare pos "+str(i)+" and pos "+str(middle*j+i))
        if num[i] == num[middle*j+i]:
          pass
        else:
          #print(num)
          yep=False
          break

    if yep:
      return num

  return False
        
def run_part1():

  found = []

  for r in ranges:
    for num in range(r[0],r[1]+1):
      result = check(num)
      if result:
        found.append(int(result))

  print(found)
  print(sum(found))
  
def run_part2():

  
  found = []

  for r in ranges:
    for num in range(r[0],r[1]+1):
      result = check2(num)
      if result:
        found.append(int(result))

  print(found)
  print(sum(found))


run_part1()
run_part2()
