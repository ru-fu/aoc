import sys
import re
from sympy import Symbol, Add, solve, Eq

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

endstates = []
buttonsets = []
joltagesets = []

with open(inputfile,"r") as input:

  for line in input:
    regex = r"^\[([\.#]+)\] (\(.+\)) {(.*)}"
    found = re.findall(regex,line)

    endstates.append(found[0][0])
    buttonsets.append([tuple([int(y) for y in x[1:-1].split(",")]) for x in found[0][1].split(" ")])
    joltagesets.append([int(x) for x in found[0][2].split(",")])

def press(button, state):

  for b in button:
    if state[b] == "#":
      state = state[:b]+"."+state[b+1:]
    else:
      state = state[:b]+"#"+state[b+1:]

  return state
    
def mysolve(endstate, buttons):

  firststate = ""

  for i in range(len(endstate)):
    firststate += "."
    
  states = [firststate]

  count = 0

  while True:
    count += 1
    newstates = []
    for state in states:
      for button in buttons:
        newstate = press(button, state)
        if newstate == endstate:
          return count
        newstates.append(newstate)
    states = newstates

def valid(newstate, endstate):

  for i in range(len(newstate)):
    if newstate[i] > endstate[i]:
      #print("Not valid: "+str(newstate))
      return False

  #print("Valid: "+str(newstate))
  return True
    
def solve2(joltages, buttons):

  equations = []

  for i in range(len(joltages)):
    collect = [str(j) for j,button in enumerate(buttons) if i in button]
    equations.append(Eq(Add(*[Symbol("b"+x) for x in collect]),joltages[i]))

  sols = solve(equations,dict=True)
  #print(equations)
  #print(sols)

  free = []
  for i in range(len(buttons)):
    if not "b"+str(i) in [str(x) for x in sols[0]]:
      free.append(i)

  print("Free: "+str(free))
  
  if len(free) == 0:
    #print(sum(sols[0].values()))
    return sum(sols[0].values())
  else:
    max_j = dict()
    for b in free:
      #print("Max joltage for "+str(b)+": "+str([joltages[j] for j in buttons[b]]))
      max_j[b] = min([joltages[j] for j in buttons[b]])
    print(max_j)
    if len(free) == 1:
      count = 0
      for i in range(max_j[free[0]]+1):
        if count > 0 and i > count:
          break
        eqs = equations.copy()
        eqs.append(Eq(Symbol("b"+str(free[0])),i))
  #      print(eqs)
        sol = solve(eqs,dict=True)
        total = sum(sol[0].values())
        minimum = min(sol[0].values())
        if not minimum < 0 and total.is_integer:
          if count == 0 or total < count:
            count = total
      return count
    elif len(free) == 2:
      count = 0
      for i in range(max_j[free[0]]+1):
        if count > 0 and i > count:
          break
        eqs = equations.copy()
        eqs.append(Eq(Symbol("b"+str(free[0])),i))
        for j in range(max_j[free[1]]+1):
          if count > 0 and i+j > count:
            break
          eqs1 = eqs.copy()
          eqs1.append(Eq(Symbol("b"+str(free[1])),j))
          
          sol = solve(eqs1,dict=True)
          total = sum(sol[0].values())
          minimum = min(sol[0].values())
          if not minimum < 0 and total.is_integer:
            if count == 0 or total < count:
              count = total
      return count
    elif len(free) == 3:
      count = 0
      for i in range(max_j[free[0]]+1):
        if count > 0 and i > count:
          break
        eqs = equations.copy()
        eqs.append(Eq(Symbol("b"+str(free[0])),i))
        for j in range(max_j[free[1]]+1):
          if count > 0 and i+j > count:
            break
          eqs1 = eqs.copy()
          eqs1.append(Eq(Symbol("b"+str(free[1])),j))
          for k in range(max_j[free[2]]+1):
            if count > 0 and i+j+k > count:
              break
            eqs2 = eqs1.copy()
            eqs2.append(Eq(Symbol("b"+str(free[2])),k))
          
            sol = solve(eqs2,dict=True)
            total = sum(sol[0].values())
            minimum = min(sol[0].values())
            if not minimum < 0 and total.is_integer:
              if count == 0 or total < count:
                count = total
      return count
        

def run_part1():

  print(buttonsets)
  print(endstates)

  counts = 0
  
  for i in range(len(endstates)):
    counts += mysolve(endstates[i],buttonsets[i])

  print(counts)
  
def run_part2():

  counts = 0

  print(joltagesets)
  
  for i in range(len(joltagesets)):
    result = solve2(joltagesets[i],buttonsets[i])
    print(result)
    counts += result

  print(counts)

#run_part1()
run_part2()
