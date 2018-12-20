import sys

from itertools import count

clay = set()
pool = set()
flowing = set()

def parse(line):
    i, j = [x.strip() for x in line.split(",")]

    j1, j2 = [int(d) for d in j[2:].split('..')]
    for j in range(j1, j2+1):
        if i[0] == "x":
            clay.add((int(i[2:]), j))
        else:
            clay.add((j, int(i[2:])))

with open("input.txt") as f:
    for line in f.readlines():
        parse(line)

def pprint(clay, flowing, pool):
    xbounds = min(c[0] for c in clay) - 1, max(c[0] for c in clay) + 2
    ybounds = min(c[1] for c in clay) - 1, max(c[1] for c in clay) + 2
    sys.stdout.write("\n")

    for j in range(*ybounds):
        for i in range(*xbounds):
            if (i, j) in pool:
                sys.stdout.write("~")
            elif (i, j) in flowing:
                sys.stdout.write("|")
            elif (i, j) in clay:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")

def scan(pos, direc):
    for i in count(1):
        loc = (pos[0] + direc[0] * i, pos[1] + direc[1])
        below = (loc[0], loc[1] + 1)

        if (loc not in clay) and (below not in pool) and (below not in clay):
            return loc, '|'
        elif loc in clay:
            return loc, '#'
        else:
            pass

def pour(pos, ylim):
    curr = pos

    while (curr not in clay):
        if curr[1] > ylim or curr in flowing:
            return
        flowing.add(curr)
        curr = (curr[0], curr[1] + 1)

    while(True):
        curr = (curr[0], curr[1] - 1)
        left = scan(curr, (-1, 0))
        right = scan(curr, (1, 0))

        if all([d[1] == "#" for d in (left, right)]):
            for x in range(left[0][0]+1, right[0][0]):
                pool.add((x, curr[1]))
                if (x, curr[1]) in flowing:
                    flowing.remove((x, curr[1]))

        else:
            for x in range(left[0][0]+1, right[0][0]):
                flowing.add((x, curr[1]))
            if left[1] == "|":
                pour(left[0], ylim)
            if right[1] == "|":
                pour(right[0], ylim)

            break

def part1(spring, clay):
    ymin = min(c[1] for c in clay)
    ymax = max(c[1] for c in clay)

    pour(spring, ymax)

    water = pool.union(flowing)

    return sum([1 for tile in water if (tile[1] <= ymax) and (tile[1] >= ymin)])

def part2(spring, clay):
    ymin = min(c[1] for c in clay)
    ymax = max(c[1] for c in clay)

    pour(spring, ymax)

    return sum([1 for tile in pool if (tile[1] <= ymax) and (tile[1] >= ymin)])
