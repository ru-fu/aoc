numbers = {}

numbers[str([1, 1, 1, 0, 1, 1, 1])] = 0
numbers[str([0, 0, 1, 0, 0, 1, 0])] = 1
numbers[str([1, 0, 1, 1, 1, 0, 1])] = 2
numbers[str([1, 0, 1, 1, 0, 1, 1])] = 3
numbers[str([0, 1, 1, 1, 0, 1, 0])] = 4
numbers[str([1, 1, 0, 1, 0, 1, 1])] = 5
numbers[str([1, 1, 0, 1, 1, 1, 1])] = 6
numbers[str([1, 0, 1, 0, 0, 1, 0])] = 7
numbers[str([1, 1, 1, 1, 1, 1, 1])] = 8
numbers[str([1, 1, 1, 1, 0, 1, 1])] = 9





with open("input08.txt","r") as input:

    count = 0
    sum = 0

    for line in input:

        entry = line.strip().split(" | ")
        patterns = entry[0].split()
        output = entry[1].split()
        allpatt = patterns + output

        count += len([x for x in output if (len(x) == 7 or 1 < len(x) < 5)])

        mapping = {}
        decode = {}

        one = [x for x in allpatt if len(x) == 2][0]
        seven = [x for x in allpatt if len(x) == 3][0]
        four = [x for x in allpatt if len(x) == 4][0]
        len_six = [x for x in allpatt if len(x) == 6]
        len_five = [x for x in allpatt if len(x) == 5]

        mapping[2] = list(one)
        mapping[5] = list(one)

        pos_0 = list(seven)
        for x in list(one):
            pos_0.remove(x)
        mapping[0] = pos_0[0]
        decode[pos_0[0]] = 0

        pos_13 = list(four)
        for x in list(one):
            pos_13.remove(x)
        mapping[1] = pos_13
        mapping[3] = pos_13

        for patt in len_six:
            if len(mapping[3]) > 1:
                if mapping[3][0] in list(patt) and mapping[3][1] in list(patt):
                    continue
                else:
                    if mapping[3][0] in list(patt):
                        decode[mapping[3][1]] = 3
                        decode[mapping[3][0]] = 1
                        mapping[1] = mapping[3][0]
                        mapping[3] = mapping[3][1]
                    else:
                        decode[mapping[3][0]] = 3
                        decode[mapping[3][1]] = 1
                        mapping[1] = mapping[3][1]
                        mapping[3] = mapping[3][0]

        for patt in len_six:
            if len(mapping[2]) > 1:
                if mapping[2][0] in list(patt) and mapping[2][1] in list(patt):
                    continue
                else:
                    if mapping[2][0] in list(patt):
                        decode[mapping[2][1]] = 2
                        decode[mapping[2][0]] = 5
                        mapping[5] = mapping[2][0]
                        mapping[2] = mapping[2][1]
                    else:
                        decode[mapping[2][0]] = 2
                        decode[mapping[2][1]] = 5
                        mapping[5] = mapping[2][1]
                        mapping[2] = mapping[2][0]

        for patt in len_five:
            pattern = list(patt)
            if mapping[0] in pattern and mapping[2] in pattern and mapping[3] in pattern and mapping[5] in pattern:
                pattern.remove(mapping[0])
                pattern.remove(mapping[2])
                pattern.remove(mapping[3])
                pattern.remove(mapping[5])
                mapping[6] = pattern[0]
                decode[pattern[0]] = 6

        for x in ['a','b','c','d','e', 'f', 'g']:
            if not x in decode:
                decode[x] = 4
                mapping[4] = x

        output_val = ""
        for x in output:
            x_decoded = [0,0,0,0,0,0,0]
            for stroke in list(x):
                x_decoded[decode[stroke]] = 1
            output_val += str(numbers[str(x_decoded)])

        sum += int(output_val)

print(count)
print(sum)
