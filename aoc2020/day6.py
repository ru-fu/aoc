groups = []
group = {}
members = 0
groupmembers = []

with open("input6.txt","r") as input:
    for line in input:
        line = line.rstrip("\n")
        if line:
            members += 1
            for char in line:
                if char in group:
                    group[char] = group[char] + 1
                else:
                    group[char] = 1

        else:
            groups.append(group)
            groupmembers.append(members)
            group = {}
            members = 0

if len(group) > 0:
    groups.append(group)
    groupmembers.append(members)

print(groups)

thesum = []

for i,answers in enumerate(groups):
    allanswered = {k:v for (k,v) in answers.items() if v == groupmembers[i]}
    print(len(allanswered))
    thesum.append(len(allanswered))

print(sum(thesum))
    
