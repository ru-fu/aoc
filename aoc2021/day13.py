paper = {}
instructions = []

def mark_paper(x,y):
    if not y in paper:
        paper[y] = set()
    paper[y].add(x)


def print_paper(size):
    collect = ""

    for y in range(size):
        if str(y) in paper:
            for x in range(size):
                if str(x) in paper[str(y)]:
                    collect += "#"
                else:
                    collect += "."
            print(collect)
            collect = ""
        else:
            for i in range(size):
                collect += "."
            print(collect)
            collect = ""


def merge_y(down,up):
    if down in paper:
        if up in paper:
            paper[up] = paper[up].union(paper[down])
        else:
            paper[up] = paper[down]
    paper.pop(down)

def fold_up(where):
    paper_copy = paper.copy()
    for y in paper_copy:
        if int(y) > int(where):
            merge_y(y,str(int(where)-(int(y)-int(where))))

    print("Fold up "+where)

def fold_left(where):
    paper_copy = paper.copy()
    for y in paper_copy:
        for x in paper_copy[y].copy():
            if int(x) > int(where):
                paper[y].add(str(int(where)-(int(x)-int(where))))
                paper[y].remove(x)

    print("Fold left "+where)

with open("input13.txt","r") as input:

    for line in input:
        if not line.strip():
            continue
        elif line.startswith("fold along"):
            ins = line.replace("fold along ","").split("=")
            instructions.append(ins)
        else:
            dot = line.strip().split(",")
            mark_paper(dot[0],dot[1])

print_paper(15)

for ins in instructions:
    if (ins[0] == "x"):
        fold_left(ins[1])
    else:
        fold_up(ins[1])



print(paper)

print_paper(150)


count = 0
for y in paper:
    count += len(paper[y])

print(count)
