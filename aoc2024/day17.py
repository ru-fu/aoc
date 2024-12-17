import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

class Register:

  def __init__(self, val):
    self.val = val

  def get(self):
    return self.val

  def set(self,val):
    self.val = val
    
  def __str__(self):
    return "Value: "+str(self.val)

with open(inputfile,"r") as input:

  for line in input:
    line = line.rstrip()
    if line.startswith("Register A"):
      A = Register(int(line[12:]))
    elif line.startswith("Register B"):
      B = Register(int(line[12:]))
      b_init = int(line[12:])
    elif line.startswith("Register C"):
      C = Register(int(line[12:]))
      c_init = int(line[12:])
    elif line.startswith("Program"):
      program = [int(x) for x in line[9:].split(",")]

def get_combo_op(op):
  global A, B, C

  if op <= 3:
    return op
  elif op == 4:
    return A.get()
  elif op == 5:
    return B.get()
  elif op == 6:
    return C.get()
  else:
    print("huh?")
      
def div(register,op):
  global A,debug

  combo_op = get_combo_op(op)

  numerator = A.get()
  denominator = pow(2,combo_op)

  floatresult = numerator / denominator

  trunc = int(str(floatresult).split(".")[0])

  if debug:
    print("xdiv "+str(op)+" (resolves to "+str(combo_op)+") => "+str(trunc))

  register.set(trunc)

def bxl(op):
  global B

  result = B.get() ^ op

  if debug:
    print("bxl "+str(op) +" => "+str(result))
    
  B.set(result)

def bst(op):
  global B,pointer

  combo_op = get_combo_op(op)

  result = combo_op % 8

  if debug:
    print("bst "+str(op)+" (resolves to "+str(combo_op)+") => "+str(result))

  B.set(result)

def jnz(op):
  global A, pointer

  if A.get() == 0:

    if debug:
      print("jnz "+str(op)+" (not jumping)")
      
    return pointer + 2
  else:

    if debug:
      print("jnz "+str(op)+" (jumping)")

    return op

def bxc(op):
  global B, C

  b = B.get()
  c = C.get()
  result = b ^ c

  if debug:
    print("bxc "+str(b) +" "+str(c)+" => "+str(result))

  B.set(result)

def out(op):

  combo_op = get_combo_op(op)

  result = combo_op % 8

  if debug:
    print("out "+str(op)+" (resolves to "+str(combo_op)+") => "+str(result))

  return result

def run():
  global program, pointer

  output = []
  
  while pointer < len(program):

    if debug:
      print("Pointer: "+str(pointer)+" ("+str(program[pointer])+")")

    if program[pointer] == 0:
      div(A,program[pointer+1])
      pointer += 2
    elif program[pointer] == 1:
      bxl(program[pointer+1])
      pointer += 2
    elif program[pointer] == 2:
      bst(program[pointer+1])
      pointer += 2
    elif program[pointer] == 3:
      pointer = jnz(program[pointer+1])
    elif program[pointer] == 4:
      bxc(program[pointer+1])
      pointer += 2
    elif program[pointer] == 5:
      output.append(out(program[pointer+1]))
      pointer += 2
    elif program[pointer] == 6:
      div(B,program[pointer+1])
      pointer += 2
    elif program[pointer] == 7:
      div(C,program[pointer+1])
      pointer += 2
    else:
      print("huh?!")

  return output
      
debug = False
pointer = 0
 
def run_part1():
  global pointer, debug

  output = run()

  print(A)
  print(B)
  print(C)
  print(output)
  print(",".join([str(x) for x in output]))
  
      
  
def run_part2():
  global A,B,C,b_init,C_init,program,pointer

  outputstr = ""
  programstr = "5,5,3,0"#",".join([str(x) for x in program])
  i = -1

  while not outputstr == programstr:
    i += 1
    A.set(i)
    B.set(b_init)
    C.set(c_init)
    pointer = 0
    output = run()
    outputstr = ",".join([str(x) for x in output])
    
    if i % 100000 == 0:
        print(i)

    prefix = 11
    if outputstr[:prefix] == programstr[:prefix]:
      print("Found something for "+str(i)+": "+outputstr)

  print(i)

def run_part2_2():
  global A,B,C,b_init,C_init,program,pointer
  
  startwith = 56
  instructions = program.copy()
  lookfor = str(instructions.pop(-2))+","+str(instructions.pop(-1))

  outputstr = ""

  while True:
    
    while not outputstr == lookfor:
      A.set(startwith)
      B.set(b_init)
      C.set(c_init)
      pointer = 0
      output = run()
      outputstr = ",".join([str(x) for x in output])
      startwith += 1

    startwith += -1
    print(str(startwith)+" => "+outputstr)

    if len(output) == len(program):
      break
    else:
      lookfor = str(instructions.pop(-1))+","+lookfor
      startwith = startwith * 8

run_part1()
run_part2_2()
