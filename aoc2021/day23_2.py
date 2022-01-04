class Board:

    def __init__(self):
        self.hall = ['.','.','.','.','.','.','.','.','.','.','.']
       # self.rooms = { 'A': ['B','A','A','A'],
       #                'B': ['C','C','B','B'],
       #                'C': ['A','B','C','C'],
       #                'D': ['D','D','D','D'] }
        self.rooms = { 'A': ['B','D','D','A'],
                       'B': ['C','C','B','D'],
                       'C': ['B','B','A','C'],
                       'D': ['D','A','C','A'] }

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
            if self.rooms[x][0] == x and self.rooms[x][1] == x and self.rooms[x][2] == x and self.rooms[x][3] == x:
                    continue
            if self.rooms[x][0] == '.' and self.rooms[x][1] == x and self.rooms[x][2] == x and self.rooms[x][3] == x:
                    continue
            if self.rooms[x][0] == '.' and self.rooms[x][1] == '.' and self.rooms[x][2] == x and self.rooms[x][3] == x:
                    continue
            if self.rooms[x][0] == '.' and self.rooms[x][1] == '.' and self.rooms[x][2] == '.' and self.rooms[x][3] == x:
                    continue
            if not self.rooms[x][0] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" top",pos))
            elif not self.rooms[x][1] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" two",pos))
            elif not self.rooms[x][2] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" three",pos))
            elif not self.rooms[x][3] == ".":
                new_pos = self.find_possible_pos(2*(i+1))
                for pos in new_pos:
                    moves.append((x+" bottom",pos))
        return moves

    def move(self,move):
        (fr,to) = move
        if fr.endswith("top"):
            which = 0
        elif fr.endswith("two"):
            which = 1
        elif fr.endswith("three"):
            which = 2
        else:
            which = 3
        room = fr[0]
        char = self.rooms[room][which]
        self.hall[to] = self.rooms[room][which]
        self.rooms[room][which] = '.'
        if which == 0:
            score = 1
        elif which == 1:
            score = 2
        elif which == 2:
            score = 3
        else:
            score = 4
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
            if self.rooms[x[0]][3] == '.':
                self.rooms[x[0]][3] = x
                score += 4 * mult
            elif self.rooms[x[0]][2] == '.':
                self.rooms[x[0]][2] = x
                score += 3 * mult
            elif self.rooms[x[0]][1] == '.':
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
                if self.rooms[x][3] == '.' or (self.rooms[x][2] == '.' and self.rooms[x][3] == x) or (self.rooms[x][1] == '.' and self.rooms[x][2] == x) or (self.rooms[x][0] == '.' and self.rooms[x][1] == x):
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

        for whichroom in ['A','B','C','D']:
            if whichroom == 'A':
                fromwhere = 2
            elif whichroom == 'B':
                fromwhere = 4
            elif whichroom == 'C':
                fromwhere = 6
            elif whichroom == 'D':
                fromwhere = 8
            firsts = [x for x in self.rooms[whichroom] if not x == "."]
            if len(firsts) > 0:
                if not firsts[0] == whichroom:
                    if self.rooms[firsts[0]][3] == '.' or (self.rooms[firsts[0]][2] == '.' and self.rooms[firsts[0]][3] == firsts[0]) or (self.rooms[firsts[0]][1] == '.' and self.rooms[firsts[0]][2] == firsts[0]) or (self.rooms[firsts[0]][0] == '.' and self.rooms[firsts[0]][1] == firsts[0]):
                        if firsts[0] == 'A':
                            try_moving = self.move_home(2,1,fromwhere,firsts[0])
                        elif firsts[0] == 'B':
                            try_moving = self.move_home(4,10,fromwhere,firsts[0])
                        elif firsts[0] == 'C':
                            try_moving = self.move_home(6,100,fromwhere,firsts[0])
                        elif firsts[0] == 'D':
                            try_moving = self.move_home(8,1000,fromwhere,firsts[0])
                        if try_moving > 0:
#                            print("Try moving: "+str(try_moving))

                            if firsts[0] == 'A':
                                total += 5-len(firsts)
                            if firsts[0] == 'B':
                                total += (5-len(firsts))*10
                            if firsts[0] == 'C':
                                total += (5-len(firsts))*100
                            if firsts[0] == 'D':
                                total += (5-len(firsts))*1000

                            total += try_moving
                            self.rooms[whichroom][4-len(firsts)] = "."

        return total

    def ready(self):
        return (self.rooms['A'][0] == 'A' and
                self.rooms['A'][1] == 'A' and
                self.rooms['A'][2] == 'A' and
                self.rooms['A'][3] == 'A' and
                self.rooms['B'][0] == 'B' and
                self.rooms['B'][1] == 'B' and
                self.rooms['B'][2] == 'B' and
                self.rooms['B'][3] == 'B' and
                self.rooms['C'][0] == 'C' and
                self.rooms['C'][1] == 'C' and
                self.rooms['C'][2] == 'C' and
                self.rooms['C'][3] == 'C' and
                self.rooms['D'][0] == 'D' and
                self.rooms['D'][1] == 'D' and
                self.rooms['D'][2] == 'D' and
                self.rooms['D'][3] == 'D')

    def ready2(self):
        count = 0
        for x in ['A','B','C','D']:
            for i in range(4):
                if self.rooms[x][i] == x:
                    count +=1
        return count

def sort_by_count(tup):
    (x,y,z,c) = tup
    return c

open_games = [(Board(),0,[],0)]
done = {}

lowest_score = 50000
saved = None

count = 50000

while open_games and count:
#    count += -1
    print("open games: "+str(len(open_games)))

    (b,s,m,c) = open_games.pop(0)

    if str(b) in done:
        if done[str(b)] < s:
            continue

    if s > lowest_score: # too expensive
        continue

    if b.ready2() == 16:
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
        ready = copy.ready2()
        if ready == 16:
            saved = log
            lowest_score = score
            continue
        if not copy.possible_moves(): # no more moves possible
            continue
        open_games.append((copy,score,log,ready))

#        open_games.sort(reverse=True,key=sort_by_count)
        done[str(copy)] = score
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
