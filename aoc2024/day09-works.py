#import utils

#inp = utils.get_input(9)
inp = "2333133121414131402"
# inp = sample_inp
import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

with open(inputfile,"r") as input:

  inp = input.read().rstrip()


pid = 0
free = []
free_blocks = {}
filled = {}
blocks = {}
pos = 0
for i, l in enumerate(inp.strip()):
    l = int(l)
    if i % 2:
        if l:
            free.extend(list(range(pos, pos + l)))
            free_blocks[pos] = l
    else:
        filled[pid] = list(range(pos, pos + l))[::-1]
        blocks[pid] = pos, l
        pid += 1
    pos += l

data = {}
for pid in sorted(filled.keys(), key=lambda x: -x):
    for k in filled[pid]:
        k_ = k
        if free and free[0] < k:
            k_ = free[0]
            free.pop(0)
        assert k_ not in data
        data[k_] = pid

ans = sum(k * v for k, v in data.items())
#utils.write_output(ans, day=9, w=1)

data = {}
for pid in sorted(blocks.keys(), key=lambda x: -x):
    s, l = blocks[pid]
    for k2 in sorted(free_blocks.keys()):
        if k2 > s:
            continue
        if free_blocks[k2] < l:
            continue
        l2 = free_blocks[k2]
        del free_blocks[k2]
        if l2 > l:
            free_blocks[k2 + l] = l2 - l
        for i in range(k2, k2 + l):
            assert i not in data
            data[i] = pid
        break
    else:
        for i in range(s, s + l):
            assert i not in data
            data[i] = pid
ans2 = sum(k * v for k, v in data.items())
print(ans2)
#utils.write_output(ans2, day=9, a=1)
