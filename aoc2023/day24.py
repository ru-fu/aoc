import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

lines = []

with open(inputfile,"r") as input:

  for line in input:
    data = line.strip().split(" @ ")
    lines.append((tuple([int(x) for x in data[0].split(", ")]),tuple([int(x) for x in data[1].split(", ")])))

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None, None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def solve(start,factor,result):

  return (result - start) / factor

def find_and_check(line1,line2,boundaries):

  a1 = line1[0][0]
  b1 = line1[0][1]
  a2 = line1[0][0] + line1[1][0]
  b2 = line1[0][1] + line1[1][1]
  c1 = line2[0][0]
  d1 = line2[0][1]
  c2 = line2[0][0] + line2[1][0]
  d2 = line2[0][1] + line2[1][1]

  (x,y) = line_intersection(((a1,b1),(a2,b2)),((c1,d1),(c2,d2)))


  if x == None or y == None:
    return (None,None)

  if x < boundaries[0] or x > boundaries[1] or \
     y < boundaries[0] or y > boundaries[1]:
    return (None,None)

  when1 = solve(a1, line1[1][0], x)
  when2 = solve(c1, line2[1][0], x)

#  print(when1,when2)

  if when1 < 0 or when2 < 0:
    return (None, None)

  return (x,y)

def run_part1():


  pairs = [(a, b) for i, a in enumerate(lines) for b in lines[i + 1:]]

  if inputfile == "test.txt":
    boundaries = (7,27)
  else:
    boundaries = (200000000000000,400000000000000)

  count = 0

  for pair in pairs:

    (x,y) = find_and_check(pair[0],pair[1],boundaries)

    if not x == None and not y == None:
      count += 1

  print(count)

def run_part2():

  print("result")

  output = ""

  for i,hail in enumerate(lines):
    if i >= 3:
      break
    output += str(hail[0][0])+" + "+str(chr(97+i))+" * "+str(hail[1][0])+" = x + "+str(chr(97+i))+" * s"+"\n"
    output += str(hail[0][1])+" + "+str(chr(97+i))+" * "+str(hail[1][1])+" = y + "+str(chr(97+i))+" * t"+"\n"
    output += str(hail[0][2])+" + "+str(chr(97+i))+" * "+str(hail[1][2])+" = z + "+str(chr(97+i))+" * u"+"\n"

  print(output)

  # use https://quickmath.com/webMathematica3/quickmath/equations/solve/advanced.jsp to solve
  # 159417177895037+391842070130986+214376796307819
  # 765636044300000 too low - calculator rounds, use Wolfram Alpha
  # 765636044333842

run_part1()
run_part2()
