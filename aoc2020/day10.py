with open("input10.txt","r") as input:
    numbers = input.readlines()

for i,num in enumerate(numbers):
    numbers[i] = int(num.rstrip("\n"))

startfrom = 0
top = max(numbers)+3

numbers.sort()


diff1 = 0
diff3 = 0


def compare(n1,n2):

    global diff1, diff3

    if n1 + 1 == n2:
        diff1 += 1
    elif n1 + 3 == n2:
        diff3 += 1
    elif n1 + 3 < n2:
        print("Gap between "+str(n1)+" and "+str(n2))
        return False

    return True


compare(startfrom, numbers[0])

for i,num in enumerate(numbers):

    if i + 1 < len(numbers):

        if not compare(num, numbers[i+1]):
            break

    else:

        compare(num,top)

print("Diff 1: "+str(diff1))
print("Diff 3: "+str(diff3))
print("Product: "+str(diff1*diff3))

numbers.append(0)
numbers.append(top)

numbers.sort(reverse = True)
print(numbers)

options = {}
counts = {}

def saveoption(i1,i2):
    if not numbers[i1] in options:
            options[numbers[i1]] = []
    options[numbers[i1]].append(numbers[i2])

for i in range(len(numbers)):
#    print(numbers[i])
    count = 0
    if i-1 >= 0 and numbers[i-1] - 3 <= numbers[i]:
        saveoption(i,i-1)
        print(str(numbers[i-1])+" - 3 <= "+str(numbers[i]))
    if i-2 >= 0 and numbers[i-2] - 3 <= numbers[i]:
        saveoption(i,i-2)
        print(str(numbers[i-2])+" - 3 <= "+str(numbers[i]))
    if i-3 >= 0 and numbers[i-3] - 3 <= numbers[i]:
        saveoption(i,i-3)
        print(str(numbers[i-3])+" - 3 <= "+str(numbers[i]))
    if i-4 >= 0 and numbers[i-4] - 3 <= numbers[i]:
        saveoption(i,i-4)
        print(str(numbers[i-4])+" - 3 <= "+str(numbers[i]))

print(options)

for num, arr in options.items():
    counts[num] = 0
    for opt in arr:
        if opt in counts:
            counts[num] += counts[opt]
        else:
            counts[num] += 1


print(counts)
