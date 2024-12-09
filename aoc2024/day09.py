import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

diskmap2 = "" 
  
with open(inputfile,"r") as input:

  diskmap2 = input.read().rstrip()
  diskmap2 = [int(x) for x in diskmap2]

def run_part1():

  diskmap = diskmap2.copy()

  max_ID = int((len(diskmap)/2))
  curr_ID = 0
  checksum = 0
  check = ""
  pos = 0

  for i in range(len(diskmap)):

#    print("i: "+str(i)+" curr_ID: "+str(curr_ID)+" max_ID: "+str(max_ID))
#    print("Checksum: " + str(checksum))
#    print(check)
    if i % 2 == 0 and diskmap[i] > 0: # even
      for j in range(diskmap[i]):
#        print(diskmap[i])
        checksum += curr_ID * pos
        pos += 1
#        check += str(curr_ID)
        diskmap[i] = diskmap[i]-1
#        print(diskmap)
      curr_ID += 1
    else: # odd
      for j in range(diskmap[i]):
        while diskmap[max_ID * 2] == 0:
          max_ID = max_ID - 1
        if max_ID < 0:
#          print(check)
          break
        checksum += max_ID * pos
        pos += 1
#        check += str(max_ID)
        diskmap[max_ID * 2] = diskmap[max_ID * 2]-1
#        print(diskmap)
        
      
  print(checksum)

def calc_checksum(diskmap,positions):
  pos = 0
  checksum = 0

  for i in range(len(diskmap)):
    if i % 2 == 0: # even
      for j in range(diskmap[i]):
        checksum += pos * int(i/2)
 #       print(str(pos)+" "+str(int(i/2)))
        pos += 1
    else:
      pos += diskmap[i]

  for ID in positions:
    for p in positions[ID]:
      checksum += p * ID

  return checksum

def calc_checksum2(diskmap,empties):
  pos = 0
  checksum = 0
  check = ""

  for i in range(len(diskmap)):
    if i % 2 == 0: # even
      for j in range(diskmap[i]):
        checksum += pos * int(i/2)
      #  print(str(pos)+" "+str(int(i/2)))
        check += str(int(i/2))
        pos += 1
    else:
      add = 0
      if i in empties:
        for which in empties[i]:
          checksum += which * pos
       #   print(str(pos + add)+" "+str(which))
          check += str(which)
          add += 1
          pos += 1
    #  print("add: "+str(add)+" pos: "+str(pos)+" diskmap[i]: "+str(diskmap[i]))
      while (add < diskmap[i]):
        add += 1
        pos += 1
        check += "."

  print(check)
  return checksum

def run_part1_simpler():

  diskmap = diskmap2.copy()

  max_ID = int((len(diskmap)/2))
  pos = 0
  min_ID = 0

  positions = {}

  for i in range(len(diskmap)):

    if not i % 2 == 0: # odd
    #  print("i: "+str(i)+" pos: "+str(pos)+" min_ID: "+str(min_ID)+" max_ID: "+str(max_ID))
  #    print(diskmap)
      for j in range(diskmap[i]):
        while diskmap[max_ID * 2] == 0:
          max_ID = max_ID - 1
        if max_ID < min_ID:
          break

        if max_ID in positions:
          positions[max_ID].append(pos)
        else:
          positions[max_ID] = [pos]

   #     print("move "+str(max_ID)+" to "+str(pos))
          
        pos += 1
        
        diskmap[max_ID * 2] = diskmap[max_ID * 2]-1
    else: # even
      pos += diskmap[i]
      min_ID += 1

  print(diskmap)
  print(positions)
      


  print(calc_checksum(diskmap,positions))
      
  
def run_part2():

  diskmap = diskmap2.copy()

  max_ID = int((len(diskmap)/2))
  pos = 0

  empties = {}
  empty = [x for i,x in enumerate(diskmap) if not i%2 == 0 ]
 # print(empty)

  for i in range(max_ID,0,-1):
#    calc_checksum2(diskmap,empties)
    length = diskmap[i*2]
    bigenough = [x[0] for x in enumerate(empty) if x[1] >= length]
    if len(bigenough) > 0 and bigenough[0] < i:
      insert = bigenough[0]*2 + 1
#      print("move "+str(i)+"(x"+str(diskmap[i*2])+") to "+str(insert))
      for j in range(diskmap[i*2]):
        if insert in empties:
          empties[insert].append(i)
        else:
          empties[insert] = [i]
      empty[bigenough[0]] = empty[bigenough[0]] - length
      diskmap[i * 2] = 0
 #     print("add "+str(length)+" empty fields to "+str((i*2)-1))
      diskmap[(i * 2) - 1] += length

  #  print(diskmap)
  #  print(empty)
  #  print(empties)
      
  print(calc_checksum2(diskmap,empties))
      
#run_part1()
run_part1_simpler()
run_part2()



#  8554338581103 too high
