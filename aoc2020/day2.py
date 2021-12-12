import re

def verify(full,min,max,char):

  if int(min) <= full.count(char) <= int(max):
    return 1
  else:
    return 0

def verify2(full,pos1,pos2,char):


  char1 = full[int(pos1)-1] == char
  char2 = full[int(pos2)-1] == char

  if (char1 or char2) and not (char1 and char2):
    return 1
  else:
    return 0


valid = 0

with open("input2.txt","r") as input:

  for line in input:

    match = re.match(r"^(\d+)-(\d+) (\w): (\w+)$", line)

    valid += verify2(match.group(4),match.group(1),match.group(2),match.group(3))


print(valid)
