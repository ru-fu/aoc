import re

rules = {}
yourticket = []
tickets = []

def readticket(line):
    ticket = line.split(",")
    for i,val in enumerate(ticket):
        ticket[i] = int(val)
    return ticket

with open("input16.txt","r") as input:

    regex = r"^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)\n$"

    line = input.readline()

    while not line == "\n":
        results = re.match(regex,line)
        (name,fr1,to1,fr2,to2) = results.groups()
        ok = []
        for i in range(int(fr1),int(to1)+1):
            ok.append(i)
        for i in range(int(fr2),int(to2)+1):
            ok.append(i)
        rules[name] = ok

        line = input.readline()

    line = input.readline()

    if line == "your ticket:\n":
        line = input.readline().rstrip("\n")
        yourticket = readticket(line)

    line = input.readline()
    line = input.readline()

    if line == "nearby tickets:\n":

        line = input.readline().rstrip("\n")

        while line:
            ticket = readticket(line)
            tickets.append(ticket)
            line = input.readline().rstrip("\n")

#print(rules)
#print(yourticket)
#print(tickets)

allowed = []

for ok in rules.values():
    allowed += ok


validtickets = []

for ticket in tickets:
    ok = 1
    for val in ticket:
        if not val in allowed:
            ok = 0
    if ok:
        validtickets.append(ticket)

#print(validtickets)

validtickets.append(yourticket)

values = {}

for ticket in validtickets:
    for i,val in enumerate(ticket):
        if not i in values:
            values[i] = []
        values[i].append(val)

print(values)

fields = {}
possiblefields = {}

for field in rules:
    fields[field] = "unknown"

for pos,vals in enumerate(values.values()):
    possible = []
    for field in fields:
        if fields[field] == "unknown":
            ok = 1
            for val in vals:
                if not val in rules[field]:
                    ok = 0
            if ok:
                possible.append(field)
    possiblefields[pos] = possible

print(possiblefields)


for i in range(100):

    for col,item in possiblefields.items():
        if len(possiblefields[col]) == 1:
            field = possiblefields[col][0]
            fields[field] = col
            for x in possiblefields:
                if field in possiblefields[x]:
                    possiblefields[x].remove(field)




#print(possiblefields)
print(fields)

mult = 1

for find in ['departure location','departure station','departure platform','departure track','departure date','departure time']:
    col = fields[find]
    yours = yourticket[col]
    print(find+": "+str(col)+" is "+str(yours))
    mult = mult * yours

print(mult)
