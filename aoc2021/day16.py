import math

with open("input16.txt","r") as input:

    for line in input:
        hexstring = line.strip()

binary = ""

while hexstring:
    bit = hexstring[0]
    hexstring = hexstring[1:]
    if bit == "0":
        binary += "0000"
    elif bit == "1":
        binary += "0001"
    elif bit == "2":
        binary += "0010"
    elif bit == "3":
        binary += "0011"
    elif bit == "4":
        binary += "0100"
    elif bit == "5":
        binary += "0101"
    elif bit == "6":
        binary += "0110"
    elif bit == "7":
        binary += "0111"
    elif bit == "8":
        binary += "1000"
    elif bit == "9":
        binary += "1001"
    elif bit == "A":
        binary += "1010"
    elif bit == "B":
        binary += "1011"
    elif bit == "C":
        binary += "1100"
    elif bit == "D":
        binary += "1101"
    elif bit == "E":
        binary += "1110"
    elif bit == "F":
        binary += "1111"

translation = ""

def parse_one(string):
    global translation, versions
    print(translation)
    print(string)

    versions.append(string[:3])
    print("Version: "+string[:3])
    string = string[3:]

    if string[:3] == "100":
        (number, reststring) = parse_literal(string[3:])
        string = reststring
        translation += str(int(number,2))+"|"
    else:
        print(string)
        (number, reststring) = parse_operator(string[3:],string[:3])
        string = reststring

    return (number, string)

def parse_literal(string):
    last = 0
    out = ""
    while not last:
        if string[0] == "0":
            last = 1
        out += string[1:5]
        string = string[5:]
    return (out, string)

def parse_operator(string, which):
    global translation
    numbers = []
    if string[0] == "1":
        how_many = int(string[1:12],2)
        string = string[12:]
        translation += "operator "+str(int(which,2))+" "
        translation += str(how_many)+"x|"
        for i in range(how_many):
            (number, string) = parse_one(string)
            numbers.append(int(number,2))
    else:
        how_many = int(string[1:16],2)
        print("how many bits: "+string[1:16]+" "+str(how_many))
        string = string[16:]
        translation += "operator "+str(int(which,2))+" "
        translation += str(how_many)+" bits|"
        save_string = string
        reststring = string[:how_many]
        while reststring and int(reststring,2):
            (number, reststring) = parse_one(reststring)
            numbers.append(int(number,2))
        string = save_string[how_many:]

    if int(which,2) == 0:
        number = sum(numbers)
    elif int(which,2) == 1:
        number = math.prod(numbers)
    elif int(which,2) == 2:
        number = min(numbers)
    elif int(which,2) == 3:
        number = max(numbers)
    elif int(which,2) == 5:
        if numbers[0] > numbers[1]:
            number = 1
        else:
            number = 0
    elif int(which,2) == 6:
        if numbers[0] < numbers[1]:
            number = 1
        else:
            number = 0
    elif int(which,2) == 7:
        if numbers[0] == numbers[1]:
            number = 1
        else:
            number = 0
    else:
        number = 0

    return (str(bin(number)), string)


versions = []

while binary and int(binary,2):
    (number,binary) = parse_one(binary)

version_sum = 0
for x in versions:
    version_sum += int(x,2)

print(versions)
print(binary)
print(translation)
print(version_sum)
print(str(int(number,2)))
