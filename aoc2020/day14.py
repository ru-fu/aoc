import re

memory = {}
mask = ""

def update(address,num):
    global memory, mask

    bin_num = bin(int(num))
    bin_num = bin_num[2:].zfill(36)
#    print(bin_num)

    for i,char in enumerate(mask):
        if char == "1":
            bin_num = bin_num[:i] + "1" + bin_num[i+1:]
        elif char == "0":
            bin_num = bin_num[:i] + "0" + bin_num[i+1:]

    memory[address] = bin_num

#    print(bin_num)

def write_all(todo,done,write):
    global memory

    if todo == "":
        memory[done] = write
#        print(done)

    else:
        check = todo[:1]
        todo = todo[1:]
        if check == "X":
            write_all(todo,done+"1",write)
            write_all(todo,done+"0",write)
        else:
            write_all(todo,done+check,write)

def updatev2(address,num):
    global memory, mask

    bin_num = bin(int(num))
    bin_num = bin_num[2:].zfill(36)
#    print(bin_num)

    bin_address = bin(int(address))
    bin_address = bin_address[2:].zfill(36)

    for i,char in enumerate(mask):
        if not char == "0":
            bin_address = bin_address[:i] + char + bin_address[i+1:]

#    print(bin_address)

    write_all(bin_address, "", bin_num)


with open("input14.txt","r") as input:

    for line in input:
        line = line.rstrip("\n")

        if line.startswith("mask = "):
            mask = line.lstrip("mask = ")
        else:
            regex = r"^mem\[(\d+)\] = (\d+)$"
            results = re.match(regex,line)
            (address,num) = results.groups()
            updatev2(address,num)

print(memory)

total = 0
for i in memory.values():
    total += int(i,2)

print(str(total))
