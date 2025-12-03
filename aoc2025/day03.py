import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

banks = []
  
with open(inputfile,"r") as input:

  for line in input:
    if len(line) > 1:
      banks.append([int(x) for x in line.rstrip()])


def find_joltage(bank):

  num1 = max(bank[:-1])

  num2 = max(bank[bank.index(num1)+1:])

  return int(str(num1)+str(num2))

def find_joltage2(bank,howmany):

  nums = []

  start = 0
  
  for i in reversed(range(howmany)):

    #print(i)
    #print(bank[start:-i])

    if i == 0:
      num = max(bank[start:])
    else:
      num = max(bank[start:-i])
    nums.append(num)
    start = bank.index(num,start)+1

  print("Result: "+str(nums))

  return int("".join([str(x) for x in nums]))
      
      
def run_part1():

  joltages = []
  
  for bank in banks:
    joltages.append(find_joltage2(bank,2))

  print(joltages)
  print(sum(joltages))
  

def run_part2():


  joltages = []
  
  for bank in banks:
    joltages.append(find_joltage2(bank,12))

  print(joltages)
  print(sum(joltages))

run_part1()
run_part2()
