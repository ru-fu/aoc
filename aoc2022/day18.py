sides = []

with open("input18.txt","r") as input:

  for line in input:
    coord = line.strip().split(",")
    coord = [int(x) for x in coord]
    x = coord[0]
    y = coord[1]
    z = coord[2]
    these_sides = [((x-1,x),y,z),((x,x+1),y,z),
                  (x,(y-1,y),z),(x,(y,y+1),z),
                  (x,y,(z-1,z)),(x,y,(z,z+1))]
    for side in these_sides:
      if side in sides:
        sides.remove(side)
      else:
        sides.append(side)

def run_part1():

  print(len(sides))

def run_part2():

  print("result")

run_part1()
run_part2()
