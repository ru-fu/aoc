import re

class Ship:

    directions = ["N","E","S","W"]

    def __init__(self,direction):
        self.direction = direction
        self.east = 0
        self.north = 0

    def __str__(self):
        return "East "+str(self.east)+" north "+str(self.north)+", facing "+str(self.direction)+" (Manhattan distance: "+str(abs(self.north)+abs(self.east))+")"

    def movenorth(self,i):
        self.north += i

    def movesouth(self,i):
        self.north -= i

    def moveeast(self,i):
        self.east += i

    def movewest(self,i):
        self.east -= i

    def turnleft(self,i):
        change = i // 90
        new = (self.directions.index(self.direction) - change) % len(self.directions)
        self.direction = self.directions[new]
        
    def turnright(self,i):
        change = i // 90
        new = (self.directions.index(self.direction) + change) % len(self.directions)
        self.direction = self.directions[new]

    def moveforward(self,i):
        if self.direction == "E":
            self.moveeast(i)
        elif self.direction == "W":
            self.movewest(i)
        elif self.direction == "N":
            self.movenorth(i)
        elif self.direction == "S":
            self.movesouth(i)

            
ship = Ship("E")



regex = r"^(\w)(\d+)\n$"

with open("input12.txt","r") as input:

    for line in input:
        
        results = re.match(regex,line)
        (instruction,num) = results.groups()
        i = int(num)
        
        if instruction == "N":
            ship.movenorth(i)
        elif instruction == "S":
            ship.movesouth(i)
        elif instruction == "E":
            ship.moveeast(i)
        elif instruction == "W":
            ship.movewest(i)
        elif instruction == "L":
            ship.turnleft(i)
        elif instruction == "R":
            ship.turnright(i)
        elif instruction == "F":
            ship.moveforward(i)
    
        
print(ship)







class GuidedShip:

    directions = ["N","E","S","W"]

    def __init__(self,wpeast,wpnorth):
        self.wpeast = wpeast
        self.wpnorth = wpnorth
        self.east = 0
        self.north = 0

    def __str__(self):
        return "East "+str(self.east)+" north "+str(self.north)+", waypoint "+str(self.wpeast)+"E "+str(self.wpnorth)+"N (Manhattan distance: "+str(abs(self.north)+abs(self.east))+")"

    def movewpnorth(self,i):
        self.wpnorth += i

    def movewpsouth(self,i):
        self.wpnorth -= i

    def movewpeast(self,i):
        self.wpeast += i

    def movewpwest(self,i):
        self.wpeast -= i

    def turnwpleft(self,i):
        cureast = self.wpeast
        curnorth = self.wpnorth
        if i == 90:
            self.wpnorth = cureast
            self.wpeast = 0 - curnorth
        elif i == 180:
            self.wpnorth = 0 - curnorth
            self.wpeast = 0 - cureast
        elif i == 270:
            self.wpnorth = 0 - cureast
            self.wpeast = curnorth
        
    def turnwpright(self,i):
        cureast = self.wpeast
        curnorth = self.wpnorth
        if i == 90:
            self.wpnorth = 0 - cureast
            self.wpeast = curnorth
        elif i == 180:
            self.wpnorth = 0 - curnorth
            self.wpeast = 0 - cureast
        elif i == 270:
            self.wpnorth = cureast
            self.wpeast = 0 - curnorth

    def moveforward(self,i):
        self.north += i * self.wpnorth
        self.east += i * self.wpeast


ship = GuidedShip(10,1)

regex = r"^(\w)(\d+)\n$"

with open("input12.txt","r") as input:

    for line in input:
        
        results = re.match(regex,line)
        (instruction,num) = results.groups()
        i = int(num)
        
        if instruction == "N":
            ship.movewpnorth(i)
        elif instruction == "S":
            ship.movewpsouth(i)
        elif instruction == "E":
            ship.movewpeast(i)
        elif instruction == "W":
            ship.movewpwest(i)
        elif instruction == "L":
            ship.turnwpleft(i)
        elif instruction == "R":
            ship.turnwpright(i)
        elif instruction == "F":
            ship.moveforward(i)

        print(ship)



