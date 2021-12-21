player_1_start = 10
player_2_start = 7

class Field:

    def __init__(self,score):
        self.next = None
        self.prev = None
        self.score = score

    def __str__(self):
        return str(self.score)

    def set_next(self,node):
        self.next = node

    def get_next(self):
        return self.next

    def get_score(self):
        return self.score

field0 = None
fieldprev = None
position = [None,None]

for i in range(10):
    f = Field(i+1)
    if i == 0:
        field0 = f
    else:
        fieldprev.set_next(f)
    if i == 9:
        f.set_next(field0)
    fieldprev = f
    if i+1 == player_1_start:
        position[0] = f
    if i+1 == player_2_start:
        position[1] = f

pos = [player_1_start,player_2_start]
score = [0,0]
turn = 0
i = 1
rolls = 0

while score[0] < 1000 and score[1] < 1000:
    rolls += 3
    if i <= 98:
        go = 3*i + 3
        i += 3
        if i == 101:
            i = 1
    elif i == 99:
        go = 99 + 100 + 1
        i = 2
    elif i == 100:
        go = 100 + 1 + 2
        i = 3
#    for j in range(go):
#        position[turn] = position[turn].get_next()
    pos[turn] += go
    if pos[turn] > 10:
        pos[turn] = pos[turn] % 10
    if pos[turn] == 0:
        pos[turn] = 10
#    score[turn] += position[turn].get_score()
    score[turn] += pos[turn]
#    print("Player "+str(turn+1)+" moves "+str(go)+" to "+str(position[turn])+str(pos[turn])+" with score "+str(score[turn]))
    if score[turn] >= 1000:
        break
    if turn:
        turn = 0
    else:
        turn = 1

def move(pos,go):
    pos += go
    if pos > 10:
        pos = pos % 10
    if pos == 0:
        pos = 10
    return pos

open_games = {(0,0,player_1_start,player_2_start): 1}
won = [0,0]

freq = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

while open_games:
#    print(open_games)
    (res,number) = open_games.popitem()
#    print("Player 1 "+str(res)+" "+str(number))

    turn = 0
    new_games = {}

    score = list(res)[turn]
    pos = list(res)[turn+2]
    for i in range(3,10):
        new_pos = move(pos,i)
        new_score = score + new_pos
        if new_score >= 21:
            won[turn] += number * freq[i]
        else:
            new_res = (new_score,res[1],new_pos,res[3])
            if new_res in new_games:
                print("Oh?")
            else:
                new_games[new_res] = number * freq[i]

    while new_games:
        (res,number) = new_games.popitem()

#        print("Player 2 "+str(res)+" "+str(number))

        turn = 1

        score = list(res)[turn]
        pos = list(res)[turn+2]
        for i in range(3,10):
            new_pos = move(pos,i)
            new_score = score + new_pos
            if new_score >= 21:
                won[turn] += number * freq[i]
            else:
                new_res = (res[0],new_score,res[2],new_pos)
                if new_res in open_games:
                    print("Oh?")
                else:
                    open_games[new_res] = number * freq[i]



print(won)
#print(score)
#print(rolls)
#print(min(score)*rolls)
