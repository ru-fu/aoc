import sys
from sympy import symbols, Eq, solve

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

equations = []
  
with open(inputfile,"r") as input:

  for line in input:
    line = line.rstrip()
    if line.startswith("Button"):
      coords = line[10:].split(", ")
      if line[7] == "A":
        a_x = int(coords[0][2:])
        a_y = int(coords[1][2:])
      elif line[7] == "B":
        b_x = int(coords[0][2:])
        b_y = int(coords[1][2:])
      else:
        print("huh? "+line[7])
    elif line.startswith("Prize"):
      coords = line[7:].split(", ")
      A, B = symbols('A B')
      eq1 = A * a_x + B * b_x - int(coords[0][2:])
      eq2 = A * a_y + B *b_y - int(coords[1][2:]) 
      equations.append((eq1,eq2))
    elif len(line) == 0:
      continue
    else:
      print("wtf?")

def run_part1():

  print(equations)

  total = 0
  
  for eqs in equations:
   sols = solve(eqs, A, B, dict=True, rational=True)
   if len(sols) > 1:
     print("wow")
   else:
     for sol in sols:
       if int(sol[A]) == sol[A] and int(sol[B]) == sol[B]:
         if int(sol[A]) > 100 or int(sol[B]) > 100:
           print("too many!")
           break
         else:
           cost = int(sol[A]) * 3 + int(sol[B])
           print(cost)
           total += cost

  print(total)

def run_part2():

  total = 0
  
  for eqs in equations:
    new_eqs = (eqs[0] - 10000000000000, eqs[1] - 10000000000000)
    sols = solve(new_eqs, A, B, dict=True, rational=True)
    if len(sols) > 1:
      print("wow")
    else:
      for sol in sols:
        if int(sol[A]) == sol[A] and int(sol[B]) == sol[B]:
        
          cost = int(sol[A]) * 3 + int(sol[B])
          print(cost)
          total += cost

  print(total)

run_part1()
run_part2()
