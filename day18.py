from collections import Counter

with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

def step(point, grid, bbox):
    i,j = point
    imax, jmax = bbox
    c = Counter()
    directions = [(1,0), (-1,0), (0, 1), (0, -1),
                  (1,1), (1,-1), (-1,1), (-1,-1)]:

    for direction in directions:
        check = (point[0] + direction[0], point[1] + direction[1])
        if (check[0] in [-1, imax]) or (check[1] in [-1, jmax]):
            pass
        else:
            c[grid[check[0]][check[1]]] +=1

    if grid[i][j] == ".":
        if c["|"] >= 3:
            return "|"
        else:
            return "."
    elif grid[i][j] == "|":
        if c["#"] >= 3:
            return "#"
        else:
            return "|"
    elif grid[i][j] == "#":
        if c["#"] >= 1 and c["|"] >= 1:
            return "#"
        else:
            return "."
    else:
        raise RuntimeError()

def pprint(lines):
    print()
    for line in lines:
        print("".join(line))

def hash(grid):
    s = ""
    for line in grid:
        for char in line:
            s += char
    return s

def part1(lines, n):
    dims = len(lines), len(lines[0])
    state = lines[:]

    for _ in range(n):
        new_state = []
        for i in range(dims[0]):
            row = []
            for j in range(dims[1]):
                row.append(step((i, j), state, dims))
            new_state.append(row)
        state = new_state[:]

    c = Counter()
    for line in state:
        for cell in line:
            c[cell] += 1

    return c["#"], c["|"]

def part2(lines, n):
    dims = len(lines), len(lines[0])
    state = lines[:]
    results = {}

    for _ in range(n):
        h = hash(state)
        if results.get(h):
            state = results.get(h)

        else:
            new_state = []
            for i in range(dims[0]):
                row = []
                for j in range(dims[1]):
                    row.append(step((i, j), state, dims))
                new_state.append(row)
            results[h] = new_state
            state = new_state[:]

    c = Counter()
    for line in state:
        for cell in line:
            c[cell] += 1

    print(_, c["#"], c["|"], c["."])

def part2(lines, n):
    dims = len(lines), len(lines[0])
    state = lines[:]
    seen = Counter()
    results = {}
    start = None

    for x in range(n):
        h = hash(state)
        seen[h] += 1

        if seen.most_common()[0][1] == 3:
            end = x
            break

        elif seen.most_common()[0][1] == 2 and start is None:
            start = x

        new_state = []
        for i in range(dims[0]):
            row = []
            for j in range(dims[1]):
                row.append(step((i, j), state, dims))
            new_state.append(row)

        results[x+1] = h
        state = new_state[:]

    cycle = end - start
    y = start + ((n-start) % cycle)
    state = results[y+1]

    c = Counter()
    for line in state:
        for cell in line:
            c[cell] += 1

    return c["|"] * c["#"]
