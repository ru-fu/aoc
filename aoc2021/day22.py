class Cube:

    def __init__(self,x,y,z):
        self.x = (int(x[0]),int(x[1]))
        self.y = (int(y[0]),int(y[1]))
        self.z = (int(z[0]),int(z[1]))

    def __str__(self):
        return "x: "+ str(self.x)+" y: "+str(self.y)+" z: "+str(self.z)

    def coords(self):
        coords = set()
        for x in range(self.x[0],self.x[1]+1):
            for y in range(self.y[0],self.y[1]+1):
                for z in range(self.z[0],self.z[1]+1):
                    coords.add((x,y,z))
        return coords

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def count(self):
        count = (self.x[1]-self.x[0]+1) * (self.y[1]-self.y[0]+1) * (self.z[1]-self.z[0]+1)
#        print(count)
        return count

# divide coords so they don't overlap with cube
def divide(divide_x,divide_y,divide_z,keep_x, keep_y, keep_z):
    #print("Divide "+str(divide_x)+str(divide_y)+str(divide_z)+" so they don't overlap with "+str(keep_x)+str(keep_y)+str(keep_z))
    x1 = int(divide_x[0])
    x2 = int(divide_x[1])
    y1 = int(divide_y[0])
    y2 = int(divide_y[1])
    z1 = int(divide_z[0])
    z2 = int(divide_z[1])
    kx1 = int(keep_x[0])
    kx2 = int(keep_x[1])
    ky1 = int(keep_y[0])
    ky2 = int(keep_y[1])
    kz1 = int(keep_z[0])
    kz2 = int(keep_z[1])

    xs = []
    if x1 < kx1:
        xs.append((x1,kx1-1))
    if x2 > kx2:
        xs.append((kx2+1,x2))
    if x1 >= kx1 and x2 >= kx2:
        xs.append((x1,kx2))
    if x1 <= kx1 and x2 <= kx2:
        xs.append((kx1,x2))
    if x1 < kx1 and x2 > kx2:
        xs.append((kx1,kx2))
    if x1 > kx1 and x2 < kx2:
        xs.append((x1,x2))
    ys = []
    if y1 < ky1:
        ys.append((y1,ky1-1))
    if y2 > ky2:
        ys.append((ky2+1,y2))
    if y1 >= ky1 and y2 >= ky2:
        ys.append((y1,ky2))
    if y1 <= ky1 and y2 <= ky2:
        ys.append((ky1,y2))
    if y1 < ky1 and y2 > ky2:
        ys.append((ky1,ky2))
    if y1 > ky1 and y2 < ky2:
        ys.append((y1,y2))
    zs = []
    if z1 < kz1:
        zs.append((z1,kz1-1))
    if z2 > kz2:
        zs.append((kz2+1,z2))
    if z1 >= kz1 and z2 >= kz2:
        zs.append((z1,kz2))
    if z1 <= kz1 and z2 <= kz2:
        zs.append((kz1,z2))
    if z1 < kz1 and z2 > kz2:
        zs.append((kz1,kz2))
    if z1 > kz1 and z2 < kz2:
        zs.append((z1,z2))

    coords2 = []

    for a in xs:
        for b in ys:
            for c in zs:
                #print(str(a)+" "+str(b)+" "+str(c))
                if not ((kx1 <= a[0] <= kx2 and
                         ky1 <= b[0] <= ky2 and
                         kz1 <= c[0] <= kz2)
                        or
                        (kx1 <= a[1] <= kx2 and
                         ky1 <= b[1] <= ky2 and
                         kz1 <= c[1] <= kz2)):
                    coords2.append((a,b,c))
#                else:
#                    print("no: "+str((a,b,c)))

   # print(coords2)
    return coords2


on1 = set()
on = []

def turn_on(x,y,z):
    global on, on1

    overlap = [c for c in on if (
        (c.get_x()[0] <= int(x[0]) <= c.get_x()[1] or
         c.get_x()[0] <= int(x[1]) <= c.get_x()[1] or
         (int(x[0]) <= c.get_x()[0] and int(x[1]) >= c.get_x()[1])
        ) and
        (c.get_y()[0] <= int(y[0]) <= c.get_y()[1] or
         c.get_y()[0] <= int(y[1]) <= c.get_y()[1] or
         (int(y[0]) <= c.get_y()[0] and int(y[1]) >= c.get_y()[1])
        ) and
        (c.get_z()[0] <= int(z[0]) <= c.get_z()[1] or
         c.get_z()[0] <= int(z[1]) <= c.get_z()[1] or
         (int(z[0]) <= c.get_z()[0] and int(z[1]) >= c.get_z()[1])
        )
    )]

    if len(overlap) == 0:
        cube = Cube(x,y,z)
        on.append(cube)
    else:
        coords = divide(x,y,z,overlap[0].get_x(),overlap[0].get_y(),overlap[0].get_z())
        for (new_x,new_y,new_z) in coords:
            turn_on(new_x,new_y,new_z)

    #cube = Cube(x,y,z)
    #on1.update(cube.coords())

def turn_off(x,y,z):
    cube = Cube(x,y,z)

    overlap = [c for c in on if (
        (c.get_x()[0] <= int(x[0]) <= c.get_x()[1] or
         c.get_x()[0] <= int(x[1]) <= c.get_x()[1] or
         (int(x[0]) <= c.get_x()[0] and int(x[1]) >= c.get_x()[1])
        ) and
        (c.get_y()[0] <= int(y[0]) <= c.get_y()[1] or
         c.get_y()[0] <= int(y[1]) <= c.get_y()[1] or
         (int(y[0]) <= c.get_y()[0] and int(y[1]) >= c.get_y()[1])
        ) and
        (c.get_z()[0] <= int(z[0]) <= c.get_z()[1] or
         c.get_z()[0] <= int(z[1]) <= c.get_z()[1] or
         (int(z[0]) <= c.get_z()[0] and int(z[1]) >= c.get_z()[1])
        )
    )]

    for one in overlap:
        coords = divide(one.get_x(),one.get_y(),one.get_z(),x,y,z)
        on.remove(one)
        for (new_x,new_y,new_z) in coords:
            turn_on(new_x,new_y,new_z)

    #on1.difference_update(cube.coords())


with open("input22.txt","r") as input:

    for line in input:
        #count = 0
        #for a in on:
            #print(a)
         #   count += a.count()
        #print(count)
        line = line.strip()

        split = line.split(",")
        xs = split[0].split("=")
        x = xs[1].split(".")
        ys = split[1].split("=")
        y = ys[1].split(".")
        zs = split[2].split("=")
        z = zs[1].split(".")

        process = 1
        for num in [x[0],x[2],y[0],y[2],z[0],z[2]]:
            if not -50 <= int(num) <= 50:
                process = 0
        process = 1
        if process:

            if line.startswith("on"):
                turn_on((x[0],x[2]),(y[0],y[2]),(z[0],z[2]))
            else:
                turn_off((x[0],x[2]),(y[0],y[2]),(z[0],z[2]))



total = 0
for cube in on:
    total += cube.count()

print(total)
#print(len(on1))
