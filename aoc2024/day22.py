import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  buyers = [int(line.rstrip()) for line in input]


def mix(secret,val):
  return secret ^ val

def prune(secret):
  return secret % 16777216

def next_number(secret):

  step1 = prune(mix(secret,secret * 64))
  step2 = prune(mix(step1,int(step1/32)))
  step3 = prune(mix(step2,step2 * 2048))

  return step3

def get_sequence(secret):

  prev_value = secret % 10
  seq = []
  out = {}

  for i in range(1999):
    secret = next_number(secret)
    val = secret % 10
    if len(seq) == 4:
      seq.pop(0)
    seq.append(val - prev_value)
    if len(seq) == 4:
      if tuple(seq) in out:
        prev_value = val
        continue
      else:
        out[tuple(seq)] = val
    prev_value = val

  return out

def calc_total(seq,sequences):
  total = 0

  for s in sequences:

    if seq in s:
      total += s[seq]

  return total


def run_part1():

 # print(mix(42,15))
 # print(prune(100000000))

  numbers = []

  for secret in buyers:
    for i in range(2000):
      secret = next_number(secret)

    numbers.append(secret)

  #print(numbers)
  print(sum(numbers))

def run_part2():

  sequences = []

 # buyers = [123]

  for secret in buyers:
    sequences.append(get_sequence(secret))

  to_evaluate = set()
  for seq in sequences:
    to_evaluate.update(seq.keys())

  totals = []

  for seq in to_evaluate:
    totals.append(calc_total(seq,sequences))

  print(totals)
  print(max(totals))

#run_part1()
run_part2()
