with open("input9.txt","r") as input:
    numbers = input.readlines()

for i,num in enumerate(numbers):
    numbers[i] = int(num.rstrip("\n"))

preamble = 25

def checkNumber(i):
    global numbers, preamble

    tocheck = numbers[i-preamble:i]

    for check in tocheck:
        if numbers[i]-check in tocheck:
            return str(check)+"+"+str(numbers[i]-check)

    return "not found"

#for i in range(preamble,len(numbers)):

#    print(str(i) + ":" + str(numbers[i]) + "=" +checkNumber(i))


lookfor = 257342611

for i in range(len(numbers)):

    thesum = 0
    x = 0

    while thesum < lookfor:
        thesum += numbers[i+x]
        x += 1

    if thesum == lookfor:
        result = numbers[i:i+x]
        result.sort()
        if len(result) > 1:
            print(result[0]+result[-1])
