endings = []
new_endings = []
ends_at = {}

with open("input12.txt","r") as input:

    for line in input:
        path = line.strip().split("-")

        if path[1] == "end":
            new_endings.append(path)
        elif path[0] == "end":
            new_endings.append([path[1], path[0]])
        else:
            if path[1] in ends_at:
                ends_at[path[1]].append(path[0])
            else:
                ends_at[path[1]] = [path[0]]
            if path[0] in ends_at:
                ends_at[path[0]].append(path[1])
            else:
                ends_at[path[0]] = [path[1]]


while new_endings:

#    print(new_endings)

    endings = endings + new_endings
    process = new_endings
    new_endings = []

    for end in process:
        for start in ends_at[end[0]]:
            if start == "start":
                endings.append([start] + end)
            elif start.islower():
                if not start in end:
                    new_endings.append([start] + end)
                else:
                    lowers = [x for x in end if x.islower()]
                    if len(lowers) == len(set(lowers)):
                        new_endings.append([start] + end)
            else:
                new_endings.append([start] + end)


full_paths = [x for x in endings if x[0] == "start"]

print(ends_at)
print(full_paths)
print(len(full_paths))
