with open("input13.txt","r") as input:
    time = int(input.readline().rstrip("\n"))
    lines = input.readline().rstrip("\n").split(",")
    offset = []
    for i,num in enumerate(lines):
        if not num == "x":
            offset.append((int(num),i))
    while "x" in lines:
        lines.remove("x")
    for i,num in enumerate(lines):
        lines[i] = int(num)
        

print(time)
print(lines)
soonest = (lines[0],lines[0]) 

for num in lines:
    arrivaltime = num - time % num
    print("Line "+str(num)+" arrives in "+str(arrivaltime)+" minutes.")

    if arrivaltime < soonest[1]:
        soonest = (num,arrivaltime)


print("Next bus is line "+str(soonest[0])+" in "+str(soonest[1])+" minutes.")
print("Product: "+str(soonest[0] * soonest[1]))

offset.sort(reverse = True)
print(offset)

i = 0
found = 0
interval= 1
hit = 0
highestbusindex = -1

while not found:
    i += 1
    time = hit + i * interval

#    print("Checking ..."+str(time)+" "+str(i)+" interval "+str(interval))

    for busindex,bus in enumerate(offset):
        if (time + bus[1]) % bus[0] == 0:
            if busindex > highestbusindex:
                hit = hit + i * interval
                interval = bus[0] * interval
                highestbusindex = busindex 
                i = 0
                print("New hit "+str(hit)+" interval "+str(interval))
                
            found = 1
            #if (bus[0] == 7):
             #   break
            continue
        else:            
#            print("Checking "+str(time)+" - not found for bus "+str(bus[0]))
            found = 0
            break

    if found:
        print(time)
        
