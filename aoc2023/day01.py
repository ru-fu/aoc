import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

print(inputfile)

lines = []

with open(inputfile,"r") as input:

  lines = [line.rstrip() for line in input]

def eval(lines):

  numbers = []

  for line in lines:
    a = 0
    b = 0

    for char in line:
      if char.isdigit():
        a = char
        break

    for char in line[::-1]:
      if char.isdigit():
        b = char
        break

    numbers.append(int(a + b))

  return numbers

def run_part1():

  numbers = eval(lines)

  print(numbers)
  print(sum(numbers))

def run_part2():

  lines_fixed = []

  for line in lines:
    newline = ""
    i = 0
    while i < len(line):
      if line[i].isdigit():
        newline += line[i:]
        break
      if line[i:].startswith("one"):
        newline += "1"
        newline += line[i+3:]
        break
      elif line[i:].startswith("two"):
        newline += "2"
        newline += line[i+3:]
        break
      elif line[i:].startswith("three"):
        newline += "3"
        newline += line[i+5:]
        break
      elif line[i:].startswith("four"):
        newline += "4"
        newline += line[i+4:]
        break
      elif line[i:].startswith("five"):
        newline += "5"
        newline += line[i+4:]
        break
      elif line[i:].startswith("six"):
        newline += "6"
        newline += line[i+3:]
        break
      elif line[i:].startswith("seven"):
        newline += "7"
        newline += line[i+5:]
        break
      elif line[i:].startswith("eight"):
        newline += "8"
        newline += line[i+5:]
        break
      elif line[i:].startswith("nine"):
        newline += "9"
        newline += line[i+4:]
        break
      else:
        newline += line[i]
        i += 1

    i = len(newline) - 1
    while i >= 0:
      if newline[i].isdigit():
        lines_fixed.append(newline)
        break
      if newline[i:].startswith("one"):
        lines_fixed.append(newline[:i]+"1"+newline[i+3:])
        break
      if newline[i:].startswith("two"):
        lines_fixed.append(newline[:i]+"2"+newline[i+3:])
        break
      if newline[i:].startswith("three"):
        lines_fixed.append(newline[:i]+"3"+newline[i+5:])
        break
      if newline[i:].startswith("four"):
        lines_fixed.append(newline[:i]+"4"+newline[i+4:])
        break
      if newline[i:].startswith("five"):
        lines_fixed.append(newline[:i]+"5"+newline[i+4:])
        break
      if newline[i:].startswith("six"):
        lines_fixed.append(newline[:i]+"6"+newline[i+3:])
        break
      if newline[i:].startswith("seven"):
        lines_fixed.append(newline[:i]+"7"+newline[i+5:])
        break
      if newline[i:].startswith("eight"):
        lines_fixed.append(newline[:i]+"8"+newline[i+8:])
        break
      if newline[i:].startswith("nine"):
        lines_fixed.append(newline[:i]+"9"+newline[i+4:])
        break
      else:
        i = i - 1



  print(lines_fixed)
  numbers = eval(lines_fixed)

  print(numbers)
  print(sum(numbers))

run_part1()
run_part2()
