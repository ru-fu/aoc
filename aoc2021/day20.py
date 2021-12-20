grid = {}
default = "."

def get_grid(r,c):
    global default

    if default == "#":
        if r in grid:
            if c in grid[r]:
                return 0
        return 1
    else:
        if r in grid:
            if c in grid[r]:
                return 1
        return 0

def find_neighbors(r,c):
    bits = ""
    bits += str(get_grid(r-1,c-1))
    bits += str(get_grid(r-1,c))
    bits += str(get_grid(r-1,c+1))
    bits += str(get_grid(r,c-1))
    bits += str(get_grid(r,c))
    bits += str(get_grid(r,c+1))
    bits += str(get_grid(r+1,c-1))
    bits += str(get_grid(r+1,c))
    bits += str(get_grid(r+1,c+1))
    return int(bits,2)


with open("input20.txt","r") as input:
    key = input.readline().strip()

    row = 0
    for line in input:
        line = line.strip()
        if line:
            for i,char in enumerate(line):
                if char == "#":
                    if not row in grid:
                        grid[row] = {}
                    grid[row][i] = 1
            row += 1

def get_all_lit():
    global grid
    cols = []
    for r in grid:
        cols.extend(list(grid[r].keys()))
    return cols

def enhance():
    global grid, default

    min_r = min(grid.keys())
    max_r = max(grid.keys())
    cols = get_all_lit()
    min_c = min(cols)
    max_c = max(cols)

    to_dot = []
    to_hash = []

    for r in range(min_r-1,max_r+2):
        for c in range(min_c-1,max_c+2):
            new_char = key[find_neighbors(r,c)]
            if new_char == "#":
                to_hash.append((r,c))
            else:
                to_dot.append((r,c))

    if default == "#":
        new_default = key[int("111111111",2)]
    else:
        new_default = key[int("000000000",2)]

    default = new_default

    if default == "#":
        to_default = to_hash
        to_non_default = to_dot
    else:
        to_default = to_dot
        to_non_default = to_hash

    for (r,c) in to_non_default:
        if not r in grid:
            grid[r] = {}
        grid[r][c] = 1

    for (r,c) in to_default:
        if r in grid:
            if c in grid[r]:
                grid[r].pop(c)
            if not grid[r]:
                grid.pop(r)




for i in range(50):
    enhance()

print(grid)
print(len(get_all_lit()))
