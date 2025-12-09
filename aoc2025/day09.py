import sys
import shapely
import matplotlib.pyplot as plt

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

tiles = dict()
squares = dict()
corners = []

with open(inputfile,"r") as input:

  for line in input:
    one = [int(x) for x in line.rstrip().split(",")]
    corners.append((one[1],one[0]))
    if one[1] in tiles:
      if one[0] < tiles[one[1]][0]:
        tiles[one[1]] = (one[0],tiles[one[1]][1])
      if one[0] > tiles[one[1]][1]:
        tiles[one[1]] = (tiles[one[1]][0],one[0])
    else:
      tiles[one[1]] = (one[0],one[0])
      

def generate_squares(which = 1):
  global squares, tiles

   
  for row1 in tiles:
    for row2 in tiles:
      squares[((row1,tiles[row1][0]),(row2,tiles[row2][1]))] = 0
      if which == 2:
        if not ((row2,tiles[row2][0]),(row1,tiles[row1][0])) in squares:
          squares[((row1,tiles[row1][0]),(row2,tiles[row2][0]))] = 0
        if not ((row2,tiles[row2][0]),(row1,tiles[row1][1])) in squares:
          squares[((row1,tiles[row1][1]),(row2,tiles[row2][0]))] = 0
        if not ((row2,tiles[row2][1]),(row1,tiles[row1][1])) in squares:
          squares[((row1,tiles[row1][1]),(row2,tiles[row2][1]))] = 0

      
def calc_area(max_size = 0):
  global squares

  for square in squares:
    c1 = square[0]
    c2 = square[1]
    area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)
    if (not max_size) or area < max_size:
      squares[square] = area
      
      
def run_part1():

  generate_squares()
  calc_area()

  print(tiles)
  for square in squares:
    print(str(square)+" - "+str(squares[square]))

  print(max(squares.values()))

def run_part2():

  polygon = shapely.Polygon(corners)
  print(polygon)
  max_size = int(shapely.area(polygon))
#  plt.plot(*polygon.exterior.xy)
#  plt.show()

  generate_squares(2)
  calc_area(max_size)

  squares2 = dict(reversed(sorted(squares.items(), key=lambda item: item[1])))

  for square in squares2:
 #   print(str(square)+" - "+str(squares[square]))
    rectangle = shapely.box(square[0][0],square[0][1],square[1][0],square[1][1])
#    plt.plot(*rectangle.exterior.xy)
#    plt.show()
    if polygon.contains(rectangle):
      print(str(square)+" - "+str(squares[square]))
      break


run_part1()
squares = dict()
run_part2()
