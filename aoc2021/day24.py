instructions = []

def get_value(variables,what):
    if what.isalpha():
        if what in variables:
            return variables[what]
        else:
            return 0
    else:
        return int(what)

def get_var(variables,what):
    if isInt(what):
        return what
    elif what.isalnum():
        if what in variables:
            return variables[what]
        else:
            return "0"
    else:
        return what

def isInt(what):
    if what.isdigit():
        return True
    elif what.startswith("-") and what[1:].isdigit():
        return True
    return False

with open("input24.txt","r") as input:

    for line in input:

        line = line.strip()
        parts = line.split(" ")
        instructions.append(parts)

def process(number):
    global instructions
    variables = {}
    pointer = 0
    for ins in instructions:
        if ins[0] == "inp":
            variables[ins[1]] = int(number[pointer])
            pointer += 1
        elif ins[0] == "add":
            variables[ins[1]] = get_value(variables,ins[1]) + get_value(variables,ins[2])
        elif ins[0] == "mul":
            variables[ins[1]] = get_value(variables,ins[1]) * get_value(variables,ins[2])
        elif ins[0] == "div":
            variables[ins[1]] = int(get_value(variables,ins[1]) / get_value(variables,ins[2]))
        elif ins[0] == "mod":
            variables[ins[1]] = get_value(variables,ins[1]) % get_value(variables,ins[2])
        elif ins[0] == "eql":
            if get_value(variables,ins[1]) == get_value(variables,ins[2]):
                variables[ins[1]] = 1
            else:
                variables[ins[1]] = 0
    return variables['z']

def make_formula():
    global instructions
    variables = {}
    pointer = 0
    for ins in instructions:
        if ins[0] == "inp":
            variables[ins[1]+str(pointer)] = ins[1]+str(pointer)
            pointer += 1
        elif ins[0] == "add":
            if ins[2] == "w":
                add = "w"+str(pointer)
            else:
                add = ins[2]
            cur_value = get_var(variables,ins[1])
            add_value = get_var(variables,add)
            if add_value == "0":
                continue
            elif isInt(cur_value) and isInt(add_value):
                variables[ins[1]] = str(int(cur_value) + int(add_value))
            elif isInt(cur_value):
                variables[ins[1]] = "("+add_value+") + "+cur_value
            elif isInt(add_value):
                variables[ins[1]] = "("+cur_value+") + "+add_value
            else:
                variables[ins[1]] = "("+cur_value+") + ("+add_value+")"
        elif ins[0] == "mul":
            cur_value = get_var(variables,ins[1])
            mul_value = get_var(variables,ins[2])
            if mul_value == "0":
                variables[ins[1]] = "0"
            elif isInt(cur_value) and isInt(mul_value):
                variables[ins[1]] = str(int(cur_value) * int(mul_value))
            elif isInt(cur_value):
                variables[ins[1]] = "("+mul_value+") * "+cur_value
            elif isInt(mul_value):
                variables[ins[1]] = "("+cur_value+") * "+mul_value
            else:
                variables[ins[1]] = "("+cur_value+") * ("+mul_value+")"
        elif ins[0] == "div":
            cur_value = get_var(variables,ins[1])
            if ins[2] == 1:
                continue
            elif isInt(cur_value):
                variables[ins[1]] = str(int(int(cur_value) / int(get_var(variables,ins[2]))))
            else:
                variables[ins[1]] = "("+cur_value+") / "+get_var(variables,ins[2])
        elif ins[0] == "mod":
            cur_value = get_var(variables,ins[1])
            if int(cur_value) < int(get_var(variables,ins[2])):
                continue
            elif isInt(cur_value):
                variables[ins[1]] = str(int(cur_value) % int(get_var(variables,ins[2])))
            else:
                variables[ins[1]] = "("+cur_value+") mod "+get_var(variables,ins[2])
        elif ins[0] == "eql":
            cur_value = get_var(variables,ins[1])
            eql_value = get_var(variables,ins[2])
            if eql_value == "w":
                eql_value = "w"+str(pointer)
            if isInt(cur_value) and isInt(eql_value):
                if cur_value == eql_value:
                    variables[ins[1]] = "1"
                else:
                    variables[ins[1]] = "0"
            else:
                variables[ins[1]] = "("+cur_value+") eq ("+eql_value+")"
        print(variables)
    return variables


result = 1
number = str("100000000000000")

#while result and len(number) >= 14:
#    number = str(int(number) - 1)
#    while "0" in number:
 #       number = str(int(number) - 1)
    #print(number)
#    result = process(number)

print(number)

print(make_formula())
