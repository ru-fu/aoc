import re

class Board:

    def __init__(self):
        self.rows = []
        self.win = 0

    def __str__(self):
        board = ""
        for r in self.rows:
            board += self.printrow(r)
            board += "\n"
        return board

    def addrow(self,arr):
        self.rows.append([(int(x),0) for x in arr])

    def printrow(self,row):
        out = ""
        for (num,marked) in row:

            if num < 10:
                numstr = " "+str(num)
            else:
                numstr = str(num)
            if marked:
                out += "*"+numstr+"*"
            else:
                out += " "+numstr+" "
            out += " "
        return out

    def isBoard(self):
        return len(self.rows) == 5

    def mark(self,num):
        if not self.win:
            for i,row in enumerate(self.rows):
                for j,val in enumerate(row):
                    if (val[0] == num):
                        self.rows[i][j] = (num,1)

    def check(self):
        if not self.win:
            for row in self.rows:
                checkrow = [x for x in row if x[1] == 1]
                if len(checkrow) == 5:
                    return 1
            for i in range(len(self.rows[0])):
                checkcol = [1 for x in self.rows if x[i][1] == 1]
                if len(checkcol) == 5:
                    return 1
        return 0

    def score(self,num):
        sum = 0
        for row in self.rows:
            for val in row:
                if not val[1]:
                    sum += val[0]
        return str(sum * int(num))

    def won(self):
        self.win = 1

boards = []

regex = r"^ *(\d+) +(\d+) +(\d+) +(\d+) +(\d+)$"

with open("input04.txt","r") as input:

    lines = input.readlines()
    numbers = lines.pop(0).strip().split(",")

    board = Board()

    for line in lines:

        results = re.match(regex,line.strip())
        if results:
            board.addrow(list(results.groups()))
        else:
            if board.isBoard():
                boards.append(board)
            board = Board()

    if board.isBoard():
        boards.append(board)

winner = 0
winnum = 0

for num in numbers:
    for b in boards:
        b.mark(int(num))
    for b in boards:
        check = b.check()
        if check:
            b.won()
            winner = b
            winnum = num



print(winner)
print(winner.score(winnum))
