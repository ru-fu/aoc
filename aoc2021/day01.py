value = -1
sums = []
minus1 = 0
minus2 = 0
incs = 0

with open("input01.txt","r") as input:

  for line in input:

    current = int(line.strip())

    if minus2 == 0:
      minus2 = current
    elif minus1 == 0:
      minus1 = current
    else:
      sums.append(minus2+minus1+current)
      minus2 = minus1
      minus1 = current

for current in sums:
    if value >= 0 and current > value:
      incs +=1

    value = current


print(sums)
print(incs)
