from math import ceil

with open("input5.txt") as input:
    boardingpasses = input.readlines()

#print(boardingpasses)


def findnumber(thepass,themax,therange,start,lower,upper):

    min = 0
    max = themax
    
    for i in range(therange):

        if thepass[start+i] == lower:
            max = max - ((max-min) // 2 + ((max-min) % 2 > 0))

        elif thepass[start+i] == upper:
            min = min + (max-min) // 2 + ((max-min) % 2 > 0)

        else:
           break

#        print(str(min)+" "+str(max))
       
    if (min == max):

        return min

    else:

        return "Error"


seats = []

for onepass in boardingpasses:

    row = findnumber(onepass,127,7,0,"F","B")
    column = findnumber(onepass,7,3,7,"L","R")
    
    seats.append((row, column, row*8+column))


print(seats)    

max = 0

for seat in seats:
  if seat[2] > max:
      max = seat[2]

print max

seats.sort(key=lambda tup: tup[2])

print seats

myseat=seats[0][2]

#print(myseat)

for seat in seats:
    if seat[2] - 1 > myseat:
        print(myseat)
        print(seat[2] - 1)
        print "My seat: "+str(seat[2] - 1)
        break
    else:
        myseat = seat[2]
