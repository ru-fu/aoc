grid = []

with open("input11.txt","r") as input:
    for line in input:
        line = line.rstrip("\n")
        grid.append(list(line))

#for line in grid:
#    print(line)

def check(rn,sn):
    global grid

    if grid[rn][sn] == "#":
        return 1
    else:
        return 0

def countocc(rn,sn):
    global grid

    count = 0

    if rn > 0:
        if sn > 0:
            count += check(rn-1,sn-1)
        count += check(rn-1,sn)
        if sn + 1 < len(grid[rn]):
            count += check(rn-1,sn+1)

    if sn > 0:
        count += check(rn,sn-1)
    if sn + 1 < len(grid[rn]):
        count += check(rn,sn+1)

    if rn + 1 < len(grid):
        if sn > 0:
            count += check(rn+1,sn-1)
        count += check(rn+1,sn)
        if sn + 1 < len(grid[rn]):
            count += check(rn+1,sn+1)

    return count

def check2(di,rn,sn):
    global grid

    checkr = rn
    checks = sn

    if 1 <= di <= 3 :
        checkr = rn - 1
    elif 7 <= di <= 9:
        checkr = rn + 1

    if di == 1 or di == 4 or di == 7:
        checks = sn - 1
    elif di == 3 or di == 6 or di == 9:
        checks = sn + 1

    if not 0 <= checkr < len(grid):
        return 0

    if not 0 <= checks < len(grid[checkr]):
        return 0

    if grid[checkr][checks] == "#":
        return 1
    elif grid[checkr][checks] == "L":
        return 0
    else:
        return check2(di,checkr,checks)

def countocc2(rn,sn):
    global grid

    count = 0

    for i in [1,2,3,4,6,7,8,9]:
        count += check2(i,rn,sn)

    return count


def updateseat(rn,sn):
    global grid, updates

    if grid[rn][sn] == "L":

        if countocc2(rn,sn) == 0:
            updates.append((rn,sn,"#"))

    elif grid[rn][sn] == "#":

        if countocc2(rn,sn) >= 5:
            updates.append((rn,sn,"L"))

def updategrid(updates):
    global grid

    for rn,sn,ch in updates:
        grid[rn][sn] = ch

updates = ["start"]


while len(updates) > 0:

    updates = []

    for rown,row in enumerate(grid):
        for seatn,seat in enumerate(row):
            updateseat(rown,seatn)

#        print(updates)

#    for line in grid:
#        print(line)

#    print("---")

    updategrid(updates)



for line in grid:
    print(line)

count = 0

for rown,row in enumerate(grid):
    for seatn,seat in enumerate(row):
        count += check(rown,seatn)

print(count)
