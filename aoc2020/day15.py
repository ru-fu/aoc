numbers = [0,12,6,13,20,1,17]
index = {}

for i in range(30000000):

    if i % 100000 == 0:
        print(i)

    if i >= len(numbers):
#        print(numbers)
#        print(index)
        lastnumber = numbers[-1]
        if lastnumber in index:
            diff = i - index[lastnumber] -1
            numbers.append(diff)
#            print("i: "+str(i)+" lastnumber: "+str(lastnumber)+" diff: "+str(diff))
        else:
            numbers.append(0)
#            print("i: "+str(i))

    if i > 0:
        index[numbers[i-1]] = i-1

print(numbers[-1])
