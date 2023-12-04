import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

cards = []

with open(inputfile,"r") as input:

  for line in input:
    while "  " in line:
      line = line.replace("  "," ")
    vals = {}
    for i,valstring in enumerate(line.strip().split(": ")[1].split(" | ")):
      vals[i]=[int(x) for x in valstring.split(" ")]
    cards.append(vals)

def run_part1():

  print(cards)

  matches = []

  for card in cards:
    count = 0
    for number in card[1]:
      if number in card[0]:
        count += 1

    if count > 0:
      matches.append(2 ** (count - 1))
    else:
      matches.append(0)

  print(matches)
  print(sum(matches))

def run_part2():

  cards2 = [dict(item, **{'count': 1}) for item in cards]

  for i,card in enumerate(cards2):
    count = 0
    for number in card[1]:
      if number in card[0]:
        count += 1

    for j in range(count):
      cards2[i+j+1]['count'] = cards2[i+j+1]['count']+cards2[i]['count']

  print(cards2)

  nums = [x['count'] for x in cards2]
  print(nums)
  print(sum(nums))

run_part1()
run_part2()
