import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

maps = []
seeds = []

with open(inputfile,"r") as input:

  fr = ""
  to = ""

  for line in input:
    line = line.strip()

    if "-" in line:
      x = line[:-5].split("-")
      fr = x[0]
      to = x[2]
    elif ":" in line:
      seeds = [int(x) for x in line[7:].split()]
    elif line == "":
      continue
    else:
      x = line.split()
      maps.append({
        'from': fr,
        'to': to,
        'dest': int(x[0]),
        'src': int(x[1]),
        'range': int(x[2])
        })

def run_part1():

  print(seeds)
  print(maps)

  source = "seed"
  target = "location"
  seeds1 = seeds.copy()

  while not source == target:
      relevant_map = [x for x in maps if x['from'] == source]

      for i,num in enumerate(seeds1):
        range_start = max([x['src'] for x in relevant_map if x['src'] <= num] + [0])
        therange = [x for x in relevant_map if x['src'] == range_start]
#        print(therange)

        if len(therange) == 1:
          if therange[0]['src'] <= num <= therange[0]['src'] + therange[0]['range']:
            seeds1[i] = num - therange[0]['src'] + therange[0]['dest']

      source = relevant_map[0]['to']

      print(seeds1)
      print(source)

  print(min(seeds1))

def run_part2():

  ranges = {}

  while seeds:
    start = seeds.pop(0)
    length = seeds.pop(0)
    ranges[start] = length

  i = 0

  while True:
    if (i % 100000) == 0:
      print(i)

    source = "seed"
    target = "location"

    check = i

    while not source == target:

      relevant_map = [x for x in maps if x['to'] == target]

      range_start = max([x['dest'] for x in relevant_map if x['dest'] <= check] + [0])
      therange = [x for x in relevant_map if x['dest'] == range_start]

      if len(therange) == 1:
          if therange[0]['dest'] <= check <= therange[0]['dest'] + therange[0]['range']:
            check = check - therange[0]['dest'] + therange[0]['src']

      target = relevant_map[0]['from']

    #print(source+" "+ str(check))

    ranges_start = max([x for x in ranges.keys() if x <= check] + [0])
    if ranges_start in ranges and ranges_start <= check < ranges_start + ranges[ranges_start]:
      print (str(ranges_start)+" <= "+str(check)+" < "+ str(ranges_start + ranges[ranges_start]))
      print("result "+source+" "+str(check)+" for location "+str(i))
      break

    i += 1

#  print(ranges)

#run_part1()
run_part2()
