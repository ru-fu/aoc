class Field:

    def __init__(self,id):
        self.beacons = set()
        self.scanner = (0,0)
        self.id = id

    def __str__(self):
        string = "Scanner "+self.id+"   "+str(self.scanner)+"\n"
        for b in self.beacons:
            string += str(b)+"\n"
        return string+"\n"
        
    def get_beacons(self):
        return self.beacons
        
    def size(self):
        return len(self.beacons)

    def addbeacon(self,b):
        self.beacons.add(b)
        
    def normalize(self,root):
        beacons = list(self.beacons)
        (x,y) = beacons[root]
        new_beacons=set()
        for b in beacons:
            new_b = (b[0]+(-1*x),b[1]+(-1*y))
            new_beacons.add(new_b)
        self.beacons = new_beacons
        self.scanner =  (self.scanner[0]+(-1*x),self.scanner[1]+(-1*y))

fields = []

with open("test.txt","r") as input:

    b = None

    for line in input:
        line = line.strip()
        if line.startswith("---"):
            if b:
                fields.append(b)
            line = line.replace("--- scanner ","")
            line = line.replace(" ---","")
            b = Field(line)
        elif line:
            coords = line.strip().split(",")
            coords = [int(x) for x in coords]
            b.addbeacon(tuple(coords))

    if b:
        fields.append(b)

#for f in fields:
 #   print(f)
#    f.normalize(0)
#    print(f)


def map(f1,f2):
    for i in range(f1.size()):
        f1.normalize(i)
        for j in range(f2.size()):
            f2.normalize(j)
            if len(f1.get_beacons().intersection(f2.get_beacons())) == 3:
                return (i,j)
    return None
            

#fields[0].normalize(0)
#print(fields[0])
#fields[1].normalize(1)
#print(fields[1])

b0 = fields[0].get_beacons()
b1 = fields[1].get_beacons()
print(b0.intersection(b1))

print(map(fields[0],fields[1]))