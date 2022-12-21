numbers = {}
calc = {}

with open("input21.txt","r") as input:

  for line in input:
    line = line.strip()
    if len(line) < 17:
      numbers[line[:4]] = int(line[6:])
    else:
      calc[line[:4]] = (line[6:10],line[11],line[13:17])

def run_part1():

  while "root" in calc:
    to_delete = []
    for monkey in calc:
      if calc[monkey][0] in numbers and calc[monkey][2] in numbers:
        if calc[monkey][1] == "+":
          numbers[monkey] = numbers[calc[monkey][0]] + numbers[calc[monkey][2]]
        elif calc[monkey][1] == "-":
          numbers[monkey] = numbers[calc[monkey][0]] - numbers[calc[monkey][2]]
        elif calc[monkey][1] == "*":
          numbers[monkey] = numbers[calc[monkey][0]] * numbers[calc[monkey][2]]
        elif calc[monkey][1] == "/":
          numbers[monkey] = int(numbers[calc[monkey][0]] / numbers[calc[monkey][2]])
        else:
          raise Exception("huh?")
        to_delete.append(monkey)
    for monkey in to_delete:
        del calc[monkey]

  print(numbers["root"])

def run_part2():

  numbers["humn"] = "x"
  calc["root"] = (calc["root"][0],"=",calc["root"][2])

  while "root" in calc:
    to_delete = []
    for monkey in calc:
      if calc[monkey][0] in numbers and calc[monkey][2] in numbers:
        if isinstance(calc[monkey][0], int) and isinstance(calc[monkey][1], int):
          if calc[monkey][1] == "+":
            numbers[monkey] = numbers[calc[monkey][0]] + numbers[calc[monkey][2]]
          elif calc[monkey][1] == "-":
            numbers[monkey] = numbers[calc[monkey][0]] - numbers[calc[monkey][2]]
          elif calc[monkey][1] == "*":
            numbers[monkey] = numbers[calc[monkey][0]] * numbers[calc[monkey][2]]
          elif calc[monkey][1] == "/":
            numbers[monkey] = int(numbers[calc[monkey][0]] / numbers[calc[monkey][2]])
          else:
            raise Exception("huh?")
        else:
          numbers[monkey] = "("+str(numbers[calc[monkey][0]])+str(calc[monkey][1])+str(numbers[calc[monkey][2]])+")"
        to_delete.append(monkey)
    for monkey in to_delete:
        del calc[monkey]

  print(numbers["root"])
  # https://www.mathpapa.com/equation-solver/

#run_part1()
run_part2()
