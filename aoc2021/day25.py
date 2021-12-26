seafloor = []

with open("input25.txt","r") as input:

    for line in input:
        line = line.strip()
        seafloor.append(line)


def move_east():
    global seafloor
    changed = 0
    for r,row in enumerate(seafloor):
        string = ""
        p = 0
        while p < len(row):
            if row[p] == ">":
                if p < len(row)-1 and row[p+1] == ".":
                    string += ".>"
                    p += 1
                    changed = 1
                elif p == len(row)-1 and row[p] == ">" and row[0] == ".":
                    string = ">"+string[1:p]+"."
                    changed = 1
                else:
                    string += row[p]
            else:
                string += row[p]
            p += 1
        seafloor[r] = string
    return changed

def move_down():
    global seafloor
    new = []
    changed = 0
    for i in range(len(seafloor)):
        new.append("")
    for p in range(len(seafloor[0])):
        r = 0
        while r < len(seafloor):
            if seafloor[r][p] == "v":
                if r < len(seafloor)-1 and seafloor[r+1][p] == ".":
                    new[r] += "."
                    new[r+1] += "v"
                    r += 1
                    changed = 1
                elif r == len(seafloor)-1 and seafloor[r][p] == "v" and seafloor[0][p] == ".":
                    new[0] = new[0][:-1]+"v"
                    new[r] += "."
                    changed = 1
                else:
                    new[r] += seafloor[r][p]
            else:
                new[r] += seafloor[r][p]
            r += 1
    for i in range(len(seafloor)):
        seafloor[i] = new[i]

    return changed



for line in seafloor:
    print(line)

i = 0

res = 1

while res:
    res_east = move_east()
    res_down = move_down()
    res = res_east or res_down
    print("Step "+str(i))

    for line in seafloor:
        print(line)

    i += 1
