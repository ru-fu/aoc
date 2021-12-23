class Board:

    def __init__(self):
        self.hall = ['.','.','.','.','.','.','.','.','.','.','.']
        self.rooms = { 'A': ['D','B'],
                       'B': ['C','A'],
                       'C': ['D','A'],
                       'D': ['B','C'] }

    def copy(self):
        b = Board()
        b.hall = self.hall.copy()
        b.rooms = {}
        for x,y in self.rooms.items():
            b.rooms[x] = y.copy()
        return b

    def __str__(self):
        string = ""
        for x in self.hall:
                string += x[0]
        string += "\n #"
        for x in ['A','B','C','D']:
            string += self.rooms[x][0]
            string += "#"
        string += "\n #"
        for x in ['A','B','C','D']:
            string += self.rooms[x][1]
            string += "#"
        return string

    def find_possible_pos(self,start):
        pos = []
        for i in range(start-1,-1,-1):
            if self.hall[i] == '.' and i in [2,4,6,8]:
                continue
            elif self.hall[i] == '.':
                pos.append(i)
            else:
                break
        for i in range(start+1,11):
            if self.hall[i] == '.' and i in [2,4,6,8]:
                continue
            elif self.hall[i] == '.':
                pos.append(i)
            else:
                break
        return pos

    def possible_moves(self):
        moves = []
        for i,x in enumerate(['A','B','C','D']):
            if self.rooms[x][0] == x and self.rooms[x][1] == x:
                    continue
            if self.rooms[x][0] == '.' and self.rooms[x][1] == x:
                    continue
            if not self.rooms[x][0] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" top",pos))
            elif not self.rooms[x][1] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" bottom",pos))
        return moves

    def move(self,move):
        (fr,to) = move
        if fr.endswith("top"):
            which = 0
        else:
            which = 1
        room = fr[0]
        char = self.rooms[room][which]
        self.hall[to] = self.rooms[room][which]
        self.rooms[room][which] = '.'
        if which:
            score = 2
        else:
            score = 1
        if room == 'A':
            if to < 2:
                score += 2 - to
            else:
                score += to - 2
        elif room == 'B':
            if to < 4:
                score += 4 - to
            else:
                score += to - 4
        elif room == 'C':
            if to < 6:
                score += 6 - to
            else:
                score += to - 6
        elif room == 'D':
            if to < 8:
                score += 8 - to
            else:
                score += to - 8
        if char == 'B':
            score = score * 10
        elif char == 'C':
            score = score * 100
        elif char == 'D':
            score = score * 1000
        return score

    def move_home(self,border,mult,i,x):
        score = 0
        if i < border:
            for j in range(i+1,border+1):
                if self.hall[j] == '.':
                    score += 1 * mult
                else:
                    score = 0
                    break
        else:
            for j in range(i-1,border-1,-1):
                if self.hall[j] == '.':
                    score += 1 * mult
                else:
                    score = 0
                    break

        if score:
            self.hall[i] = '.'
            if self.rooms[x[0]][1] == '.':
                self.rooms[x[0]][1] = x
                score += 2 * mult
            else:
                self.rooms[x[0]][0] = x
                score += 1 * mult

        return score

    def move_in(self):
        total = 0
        for i,x in enumerate(self.hall):
            score = 0
            if not x == ".":
                if self.rooms[x][1] == '.' or (self.rooms[x][0] == '.' and self.rooms[x][1] == x):
                    # room is free
                    if x[0] == 'A':
                        add = self.move_home(2,1,i,x)
                        score += add
                    elif x[0] == 'B':
                        add = self.move_home(4,10,i,x)
                        score += add
                    elif x[0] == 'C':
                        add = self.move_home(6,100,i,x)
                        score += add
                    elif x[0] == 'D':
                        add = self.move_home(8,1000,i,x)
                        score += add
            total += score
        return total

    def ready(self):
        return (self.rooms['A'][0] == 'A' and
            self.rooms['A'][1] == 'A' and
            self.rooms['B'][0] == 'B' and
            self.rooms['B'][1] == 'B' and
            self.rooms['C'][0] == 'C' and
            self.rooms['C'][1] == 'C' and
            self.rooms['D'][0] == 'D' and
            self.rooms['D'][1] == 'D')


open_games = [(Board(),0,[])]

lowest_score = 15000
saved = None

count = 300000

while open_games and count:
#    count += -1
    print("open games: "+str(len(open_games)))

    (b,s,m) = open_games.pop(0)

    if s > lowest_score: # too expensive
        continue

    if b.ready():
        saved = b
        lowest_score = s
        continue

#    print(b)
    moves = b.possible_moves()
#    print("moves: "+str(len(moves)))
#    print(moves)

    if not moves: # no more moves possible
        continue

    for x in moves:
        log = m.copy()
        log.append(x)
        copy = b.copy()
        score = s
#        print("before")
#        print(score)
#        print(copy)
        score += copy.move(x)
        new_score = 1
        while new_score:
            new_score = copy.move_in()
            score += new_score
        log.append(score)
        if score > lowest_score: # too expensive
            continue
        if copy.ready():
            saved = log
            lowest_score = score
            continue
        if not copy.possible_moves(): # no more moves possible
            continue
        open_games.append((copy,score,log))
#        print("after")
#        print(copy)
#        print(score)
#        print(lowest_score)

#    print(x)
#    print(copy.move(x))
#    print(copy.hall)

#print(b.hall)
#print(b.move_in())
#print(b)

print(lowest_score)
print(saved)
