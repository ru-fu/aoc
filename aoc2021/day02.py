import re

class Position:

    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def __str__(self):
        return "Horizontal "+str(self.horizontal)+" depth "+str(self.depth)+" (Product: "+str(self.horizontal * self.depth)+")"

    def moveforward(self,i):
        self.horizontal += i
        self.depth += self.aim * i

    def movedown(self,i):
        self.aim += i

    def moveup(self,i):
        self.aim -= i

pos = Position()

regex = r"^(\w+) (\d+)\n$"

with open("input02.txt","r") as input:

    for line in input:

        results = re.match(regex,line)
        (instruction,num) = results.groups()
        i = int(num)

        if instruction == "forward":
            pos.moveforward(i)
        elif instruction == "up":
            pos.moveup(i)
        elif instruction == "down":
            pos.movedown(i)


print(pos)
