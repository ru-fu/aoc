import re

grid = {}

def add(x,y):
    if x in grid:
        if y in grid[x]:
            grid[x][y] += 1
        else:
            grid[x][y] = 1
    else:
        grid[x] = {}
        grid[x][y] = 1

regex = r"^(\d+),(\d+) -> (\d+),(\d+)$"

with open("input05.txt","r") as input:

    for line in input:

        results = re.match(regex,line.strip())

        (x1,y1,x2,y2) = results.groups()

        if (x1 == x2):
            if int(y2) > int(y1):
                for y in range(int(y1),int(y2)+1):
                    add(x1,str(y))
            else:
                for y in range(int(y2),int(y1)+1):
                    add(x1,str(y))
        elif (y1 == y2):
            if int(x2) > int(x1):
                for x in range(int(x1),int(x2)+1):
                    add(str(x),y1)
            else:
                for x in range(int(x2),int(x1)+1):
                    add(str(x),y1)
        else:
            mult = 1
            if (int(x1) >= int(x2)):
                tmp = x1
                x1 = x2
                x2 = tmp
                tmp = y1
                y1 = y2
                y2 = tmp
            if (int(y1) >= int(y2)):
                mult = -1
            i = 0
            for x in range(int(x1),int(x2)+1):
                y = int(y1) + ( i * mult)
                add(str(x),str(y))
                i += 1

#print(grid)

points = 0
for x in grid:
    for y in grid[x]:
        if grid[x][y]>=2:
            points += 1

print(points)
