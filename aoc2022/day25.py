numbers = []

with open("input25.txt","r") as input:

  for line in input:
    numbers.append(line.strip())

def decode(number):

  total = 0
  for i,x in enumerate(number[::-1]):
    if x.isdigit():
      total += int(x) * (5 ** i)
    elif x == "-":
      total += -1 * (5 ** i)
    elif x == "=":
      total += -2 * (5 ** i)
    else:
      raise Exception("huh?")

  return total

def encode(number):

  total = []

  maxpower = 0

  while 5 ** maxpower <= number:
    maxpower += 1

  maxpower += -1

  while maxpower >= 0:
    curr = number // 5 ** maxpower
    total.append(curr)
    number = number - curr * (5 ** maxpower)
    maxpower += -1

  total.reverse()

  totalstr = ""
  carryover = 0

  print(total)

  for num in total:
#    print("Num: "+str(num)+" Carryover: "+str(carryover))
    num += carryover
    if num <= 2:
      totalstr += str(num)
      carryover = 0
    elif num == 3:
      totalstr += "="
      carryover = 1
    elif num == 4:
      totalstr += "-"
      carryover = 1
    elif num == 5:
      totalstr += "0"
      carryover = 1
    else:
      raise Exception("oh...")

  if not carryover == 0:
    totalstr += str(carryover)


  return totalstr[::-1]



def run_part1():

  result = []
  for x in numbers:
    result.append(decode(x))

  thesum = sum(result)

  print(encode(thesum))
#  print(encode(497))

def run_part2():

  print("result")

run_part1()
run_part2()
