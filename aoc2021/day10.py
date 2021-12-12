illegals = {}
scores = []

def check(line):

#    print(line)

    line_new = line.replace("()","")
    line_new = line_new.replace("<>","")
    line_new = line_new.replace("{}","")
    line_new = line_new.replace("[]","")

    if len(line) == 0:
        return "ok"
    elif line_new == line:

        first_close = len(line)

        for x in [")","]","}",">"]:

            closing = line.find(x)
            if 0 <= closing < first_close:
                first_close = closing

        if first_close < len(line):
            return line[first_close]
        else:
            return "incomplete"+line
    else:
        return check(line_new)

def score(seq):
    seq = seq[::-1]
    score = 0
    for char in seq:
        score = score * 5
        if char == '(':
            score = score + 1
        elif char == "[":
            score = score + 2
        elif char == "{":
            score = score + 3
        elif char == "<":
            score = score + 4
    return score

with open("input10.txt","r") as input:

    for line in input:

        res = check(line.strip())

        if res == "ok":
            continue
        elif res.startswith("incomplete"):
            scores.append(score(res.replace("incomplete","")))
        else:
            illegals[res] = illegals.setdefault(res,0) + 1

calc = illegals[")"] * 3 + illegals["]"] * 57 + illegals["}"] * 1197 + illegals[">"] * 25137

scores.sort()

print(illegals)
print(calc)
print(scores)
print(scores[int(len(scores)/2)])
