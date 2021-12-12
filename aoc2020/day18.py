def calculate(expr, result=0, operator="+"):
#    print(result)
#    print(expr)
    char = expr.pop(0)
    if char.isdigit():
        if operator == "+":
            result += int(char)
        elif operator == "*":
            result = result * int(char)
    elif char == "+" or char == "*":
        operator = char
    elif char == "(":
        parcount = 1
        for i,x in enumerate(expr):
            if x == "(":
                parcount += 1
            elif x == ")":
                parcount = parcount - 1
                if parcount == 0:
                    parresult = calculate(expr[:i])
                    expr = [str(parresult)]+expr[i+1:]
                    break


    if len(expr) > 0:
#        print("iterate with result "+str(result)+" and op "+operator)
        return calculate(expr,result,operator)
    else:
#        print("Result: "+str(result))
        return result


def group(mylist):

    newlist = []
    char = mylist.pop(0)

    while char:

        if not char == "(":
            newlist.append(char)
        else:
            parcount = 1
            for i,x in enumerate(mylist):
                if x == "(":
                    parcount += 1
                elif x == ")":
                    parcount = parcount - 1
                    if parcount == 0:
                        pargroup = group(mylist[:i])
                        newlist.append(pargroup)
                        mylist = mylist[i+1:]
                        break

        if len(mylist) > 0:
            char = mylist.pop(0)
        else:
            char = False

    return newlist

def calculate_result(mylist):

    result = 0
    operator = "+"

    for char in mylist:
        if char.isdigit():
            if operator == "+":
                result += int(char)
            elif operator == "*":
                result = result * int(char)
        elif char == "+" or char == "*":
                operator = char

    print("List: " +str(mylist)+" Result: "+str(result))
    return str(result)

def calculate_result2(mylist):

    result = 1
    remember = 0
    thesum = 0

    for char in mylist:
        if char.isdigit():
#            print("Digit: "+char)
            remember = int(char)
        elif char == "+":
#            print("Found +")
            thesum += remember
        elif char == "*":
#            print("Found *")
            if thesum == 0:
#                print("Here: "+str(result)+" "+str(remember))
                result = result * remember
            else:
                thesum += remember
#                print("There: "+str(result)+" "+str(thesum))
                result = result * thesum
                thesum = 0

    if thesum == 0:
#        print("Here: "+str(result)+" "+str(remember))
        result = result * remember
    else:
        thesum += remember
#        print("There: "+str(result)+" "+str(thesum))
        result = result * thesum

    return str(result)


def getresult(mylist):

    all_flat = 1

    for el in mylist:
        if isinstance(el, list):
            all_flat=0
            break

    if all_flat:
        return calculate_result2(mylist)
    else:

        for i,el in enumerate(mylist):
            if isinstance(el, list):
                mylist[i] = getresult(el)
                break

        return getresult(mylist)



with open("input18.txt","r") as input:

    total = 0

    for line in input:
        line = line.rstrip("\n")
        line = line.replace(" ","")
        elements = group(list(line))
#        print(elements)

        result = getresult(elements)

#        result = calculate(list(line))
        print(result)
        total += int(result)

print("Total: "+str(total))
