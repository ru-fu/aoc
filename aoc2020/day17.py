def neighbors(x,y,z,w):
    neighbors = []

    for newx in [x-1,x,x+1]:
        for newy in [y-1,y,y+1]:
            for newz in [z-1,z,z+1]:
                for neww in [w-1,w,w+1]:
                    neighbors.append((newx,newy,newz,neww))

    neighbors.remove((x,y,z,w))

    return neighbors

coords={}

def countNeighbors(x,y,z,w):

    all = neighbors(x,y,z,w)

    count = 0

    for node in all:
        (xx,yy,zz,ww) = node
        if isactive(xx,yy,zz,ww):
            count +=1

    return count

def makeactive(x,y,z,w):
    global coords

    if not str(x) in coords:
        coords[str(x)] = {}

    if not str(y) in coords[str(x)]:
        coords[str(x)][str(y)] = {}

    if not str(z) in coords[str(x)][str(y)]:
        coords[str(x)][str(y)][str(z)] = {}

    coords[str(x)][str(y)][str(z)][str(w)] = "active"

def isactive(x,y,z,w):
    global coords

    if str(x) in coords:
        if str(y) in coords[str(x)]:
            if str(z) in coords[str(x)][str(y)]:
                if str(w) in coords[str(x)][str(y)][str(z)]:
                    return True

    return False

def makeinactive(x,y,z,w):
    global coords

    del coords[str(x)][str(y)][str(z)][str(w)]

    if len(coords[str(x)][str(y)][str(z)]) == 0:
        del coords[str(x)][str(y)][str(z)]

    if len(coords[str(x)][str(y)]) == 0:
        del coords[str(x)][str(y)]

    if len(coords[str(x)]) == 0:
        del coords[str(x)]

def countactive():
    global coords,max_x,min_x,max_y,min_y,max_z,min_z,max_w,min_w

    count = 0
    for nrx in range(min_x-2,max_x+3):
        for nry in range(min_y-2,max_y+3):
            for nrz in range(min_z-2,max_z+3):
                for nrw in range(min_w-2,max_w+3):
                    if isactive(nrx,nry,nrz,nrw):
                        count += 1
    return count

def printgrid():
    global coords,max_x,min_x,max_y,min_y,max_z,min_z

#    print("max x:"+str(max_x))
#    print("max y:"+str(max_y))
#    print("max z:"+str(max_z))
#    print("min x:"+str(min_x))
#    print("min y:"+str(min_y))
#    print("min z:"+str(min_z))

    for nrx in range(min_x-1,max_x+2):
        print("x = "+str(nrx))

        for nry in range(min_y-1,max_y+2):
            line = ""
            for nrz in range(min_z-1,max_z+2):
                if isactive(nrx,nry,nrz):
                    line += "#"
                else:
                    line += "."
            print(line)


with open("input17.txt","r") as input:
    y = 0

    for line in input:
        arr = list(line.rstrip("\n"))
        x = 0

        for char in arr:
            if char == "#":
                makeactive(0,0,y,x)
            x += 1

        y += 1


max_x = 10
min_x = 0
max_y = 10
min_y = 0
max_z = 10
min_z = 0
max_w = 10
min_w = 0

for i in range(6):

    #print(coords)

#    all_x = list(coords.keys())
#    all_y = []
#    all_z = []
#    for x in coords:
#        for y in coords[x]:
#            all_y +=list(coords[x].keys())
#            for z in coords[x][y]:
#                all_z +=list(coords[x][y].keys())

#    all_x.sort()
#    max_x = int(all_x[-1])
#    min_x = int(all_x[0])
#    all_y.sort()
#    max_y = int(all_y[-1])
#    min_y = int(all_y[0])
#    all_z.sort()
#    max_z = int(all_z[-1])
#    min_z = int(all_z[0])

    updateactive = []
    updateinactive = []
    for nrx in range(min_x-2,max_x+3):
        for nry in range(min_y-2,max_y+3):
            for nrz in range(min_z-2,max_z+3):
                for nrw in range(min_w-2,max_w+3):
                    activeNeighbors = countNeighbors(nrx,nry,nrz,nrw)
                    if isactive(nrx,nry,nrz,nrw):
                        if not 1 < activeNeighbors < 4:
                            updateinactive.append((nrx,nry,nrz,nrw))
                    elif activeNeighbors == 3:
                        updateactive.append((nrx,nry,nrz,nrw))

    #print(updateactive)

    for (x,y,z,w) in updateactive:
        makeactive(x,y,z,w)

    #print(updateinactive)

    for (x,y,z,w) in updateinactive:
        makeinactive(x,y,z,w)

    max_x += 1
    max_y += 1
    max_z += 1
    max_w += 1
    min_x = min_x - 1
    min_y = min_y - 1
    min_z = min_z - 1
    min_w = min_w - 1

    #printgrid()
    print(countactive())
