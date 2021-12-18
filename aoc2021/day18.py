import math

chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def convert_to_num(char):
    if char.isdigit():
        return int(char)
    else:
        if char in chars:
            return 10 + int(chars.index(char))
        else:
            print("OUT OF RANGE!  "+char)

def convert_to_one(num):
    if num < 10:
        return str(num)
    else:
        if num - 10 < len(chars):
            return chars[num - 10]
        else:
            print("OUT OF RANGE!  "+str(num))

def explode(string):
    brackets = 0
    exp1 = 0
    lastnum = -1
    for i,char in enumerate(string):
        if brackets == 5:
            exp1 = i
            break
        if char == "[":
            brackets += 1
        elif char == "]":
            brackets += -1
        elif char == ",":
            continue
        else:
            lastnum = i

    if exp1:
        left = convert_to_num(string[exp1])
        right = convert_to_num(string[exp1+2])
        if lastnum > -1:
            newstring = string[:lastnum]
            newstring += convert_to_one(convert_to_num(string[lastnum]) + left)
            newstring += string[lastnum+1:exp1-1]
        else:
            newstring = string[:exp1-1]
        newstring += "0"
        nextnum = 0
        for i,char in enumerate(string[exp1+3:]):
            if not char =="[" and not char =="]" and not char == ",":
                nextnum = i
                break
        if nextnum > 0:
            newstring += string[exp1+4:exp1+3+nextnum]
            newstring += convert_to_one(right + convert_to_num(string[exp1+3+nextnum]))
            newstring += string[exp1+4+nextnum:]
        else:
            newstring += string[exp1+4:]
        return newstring
    else:
        return string

def split(string):
    for i,char in enumerate(string):
        if not char =="[" and not char =="]" and not char == "," and not char.isdigit():
            num = convert_to_num(char)
            left = math.floor(num/2)
            right = math.ceil(num/2)
            newstring = string[:i]
            newstring += "["+convert_to_one(left)+","+convert_to_one(right)+"]"
            newstring += string[i+1:]
            return newstring
    return string

def reduce(line):
    reduced = explode(line)

    while not line == reduced:
        line = reduced
        reduced = explode(line)

    reduced = split(line)

    return reduced

def run_reduce(line):
    reduced = reduce(line)

    while not line == reduced:
        line = reduced
        reduced = reduce(line)

    return line

def add(str1,str2):
    return "["+str1+","+str2+"]"

def magnitude(pair):

    brackets = 0
    middle = 0

    if pair.isdigit():
        return int(pair)

    for i, char in enumerate(pair):
        if char == "[":
            brackets += 1
        elif char == "]":
            brackets += -1
        elif char == ",":
            if brackets == 1:
                middle = i
                break
    if not middle:
        print("HUH?!")
    else:
        left = pair[1:middle]
        right = pair[middle+1:-1]
        return 3*magnitude(left) + 2*magnitude(right)

results = []

with open("input18.txt","r") as input:

#    result = ""

#    for line in input:
#        if result:
#            new_result = add(result, line.strip())
#            result = run_reduce(new_result)
#        else:
#            result = run_reduce(line.strip())

    lines = input.readlines()

    for i, line in enumerate(lines):
        for j in range(len(lines)):
            if not i == j:
                results.append(magnitude(run_reduce(add(lines[i].strip(),lines[j].strip()))))

print(max(results))

#print(magnitude(result))
