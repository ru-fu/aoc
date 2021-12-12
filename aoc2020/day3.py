class TreeRow:

    def __init__(self,start):
        self.content = start.rstrip("\n")

    def __str__(self):
        return self.content

    def char(self, i):

        if len(self.content) > i:
            return self.content[i]
        else:
            return self.char(i-len(self.content))

    def isTree(self,i):

        if (self.char(i) == "#"):
            return True
        else:
            return False


with open("input3.txt") as input:
    treerows = input.readlines()

for i, treerow in enumerate(treerows):
    treerows[i] = TreeRow(treerow)


def checkSlope(right,down):

    trees=0
    posr=right
    posd=down

    while posd < len(treerows):

        if treerows[posd].isTree(posr):
            trees += 1

        posr += right
        posd += down

    return trees

a=(checkSlope(1,1))
b=(checkSlope(3,1))
c=(checkSlope(5,1))
d=(checkSlope(7,1))
e=(checkSlope(1,2))

output = "{} * {} * {} * {} * {} = {}"
print(output.format(a,b,c,d,e,a*b*c*d*e))
