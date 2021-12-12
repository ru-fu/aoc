ages = {}

for i in range(9):
    ages[i] = 0

with open("input06.txt","r") as input:

    line = input.readline()
    start = line.strip().split(",")

    for i in start:
        ages[int(i)] += 1

def newday():
    new_fish = ages[0]
    ages[7] += ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7]
    ages[7] = ages[8]
    ages[8] = new_fish


for i in range(256):
    newday()
    print(str(i+1)+": "+str(ages))

print(sum(ages.values()))
