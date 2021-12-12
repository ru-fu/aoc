report = []

def todec(arr):
    string = "".join([str(x) for x in arr])
    return int(string,2)

with open("input03.txt","r") as input:

    for line in input:
        report.append([int(x) for x in list(line.strip())])

total = len(report)
one = len(report[0])
gamma = []
epsilon = []

oxygen = report
co2 = report

for bit in range(one):
    sum = 0
    for val in report:
        sum += val[bit]
    if sum > total/2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

for bit in range(one):
    if len(oxygen) > 1:
        sum = 0
        res = -1
        for val in oxygen:
            sum += val[bit]
        if sum >= len(oxygen)/2:
            res = 1
        else:
            res = 0
        oxygen = [x for x in oxygen if x[bit] == res]
#        print(oxygen)
    if len(co2) > 1:
        sum = 0
        res = -1
        for val in co2:
            sum += val[bit]
        if sum < len(co2)/2:
            res = 1
        else:
            res = 0
        co2 = [x for x in co2 if x[bit] == res]
#        print(co2)

print("Gamma: "+str(gamma)+" "+str(todec(gamma)))
print("Epsilon: "+str(epsilon)+" "+str(todec(epsilon)))
print("Product: "+str(todec(gamma) * todec(epsilon)))
print("Oxygen: "+str(oxygen[0])+" "+str(todec(oxygen[0])))
print("CO2: "+str(co2[0])+" "+str(todec(co2[0])))
print("Product: "+str(todec(oxygen[0]) * todec(co2[0])))
