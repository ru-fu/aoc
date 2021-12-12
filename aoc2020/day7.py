import re

bags = {}

with open("input7.txt","r") as input:
    for line in input:

        contains = line.split("bags contain")
        bag = contains[0]
        bags[bag.strip()] = {}
        which = contains[1].split(", ")

        for one in which:

#            print(one)
            regex = r"^ *(\d+) ([\w ]+) bags?.?"

            results = re.findall(regex,one)

            for (num, name) in results:
                bags[bag.strip()][name.strip()] = int(num)

#print(bags)

found = []

def myfind(lookfor):

#    print("Finding "+lookfor)
    global found

    for outer in bags:
#        print("Checking for "+lookfor+" in "+outer)
        if lookfor in bags[outer].keys():
            if not outer in found:
                found.append(outer)
#                print("Found "+outer)
                myfind(outer)
#            else:
#                print("Not found: "+lookfor)

myfind("shiny gold")

print(found)
print(len(found))

total = 0

def findcontents(bag, times):

    global total

    for contains in bags[bag]:
        print(contains)
        print("Found "+str(bags[bag][contains])+" "+contains+" in "+bag)
        total += times * bags[bag][contains]
        findcontents(contains, times * bags[bag][contains])

findcontents("shiny gold",1)
print(total)
