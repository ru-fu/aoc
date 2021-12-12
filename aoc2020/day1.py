
inputlist = []

with open("input1.txt","r") as input:

  for line in input:

    inputlist.append(int(line))

def findsum(thelist, thesum):

  for number in thelist:

    lookfor = thesum - number

    if lookfor in thelist:

      return([number,lookfor])
      break

  return("not found")


result = findsum(inputlist, 2020)

if (result != "not found"):

  print(str(result[0]) + "+" + str(result[1]) + "= 2020")

  print(str(result[0]) + "*" + str(result[1])+ "=" + str(result[0]*result[1]))


for number in inputlist:

  lookfor = 2020 - number

  newlist = inputlist
  newlist.remove(number)

  result = findsum(newlist, lookfor)

  if (result != "not found"):

    print(str(number) + "+" + str(result[0]) + "+" + str(result[1]) + "= 2020")

    print(str(number) + "*" + str(result[0]) + "*" + str(result[1])+ "=" + str(number*result[0]*result[1]))
