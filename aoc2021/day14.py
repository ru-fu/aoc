first = ""
last = ""
pairs = {}
rules = {}

with open("input14.txt","r") as input:

    for line in input:
        line = line.strip()

        if line:
            if line.find("->") > -1:
                rule = line.replace(" -> ","-").split("-")
                rules[rule[0]] = [rule[0][0]+rule[1], rule[1]+rule[0][1]]
            else:
                first = line[0]
                last = line[-1]
                for i in range(len(line)-1):
                    pair = line[i]+line[i+1]
                    pairs[pair] = pairs.setdefault(pair,0) + 1


for i in range(40):
    old_pairs = pairs.copy()
    for pair in old_pairs:
        if pair in rules:
            for newpair in rules[pair]:
#                print("add "+newpair)
                if newpair in pairs:
                    pairs[newpair] = pairs[newpair] + old_pairs[pair]
                else:
                    pairs[newpair] = old_pairs[pair]
            pairs[pair] = pairs[pair] - old_pairs[pair]
 #           print("remove "+pair)

count = {}
for pair in pairs:
    count[pair[0]] = count.setdefault(pair[0],0) + pairs[pair]
    count[pair[1]] = count.setdefault(pair[1],0) + pairs[pair]

count[first] = count[first] + 1
count[last] = count[last] + 1

for c in count:
    count[c] = int(count[c] / 2)

max_value = max(count.values())
min_value = min(count.values())

print(first)
print(last)
print(rules)
print(pairs)
print(count)
print(str(max_value - min_value))
