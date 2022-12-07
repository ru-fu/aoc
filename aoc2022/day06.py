with open("input06.txt","r") as input:

  messages = input.readlines()

message = messages[0]

def check(string, pos, num):
  checkset = set(())
  for i in range(0,num):
    checkset.add(string[pos-i])
  if len(checkset) == num:
    return True
  else:
    return False

def run_part1():

  for i in range(4, len(message)):
    if check(message,i-1,4):
      print(i)
      break

def run_part2():

  for i in range(14, len(message)):
    if check(message,i-1,14):
      print(i)
      break

run_part1()
run_part2()
