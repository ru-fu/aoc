crabs = {}

with open("input07.txt","r") as input:

    line = input.readline()
    start = line.strip().split(",")

    for i in start:
        if int(i) in crabs:
            crabs[int(i)] += 1
        else:
            crabs[int(i)] = 1

steps_cache = {}

def steps(x):
    if x in steps_cache:
        return steps_cache[x]
    else:
        sum = 0
        for i in range(x):
            sum += i + 1
        steps_cache[x] = sum
        return sum

distances = {}

for i in range(min(crabs.keys()),max(crabs.keys())+1):
    sum = 0
    for crab,num in crabs.items():
        if crab > i:
            sum += steps(crab - i) * num
        else:
            sum += steps(i - crab) * num
    distances[i] = sum


print(crabs)
print(distances)

print(min(distances.values()))
