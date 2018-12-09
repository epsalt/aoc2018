## This is inefficient

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def parse_line(line):
    _, _, coords, dims = line.split(" ")
    x, y = map(int, coords[:-1].split(","))
    width, height = map(int, dims.split("x"))

    return (x, y, width, height)

def matrix(xoffset, yoffset, width, height, n):
    for y in range(n):
        if (y < yoffset or y >= yoffset + height):
            yield [0] * n
        else:
            yield [1 if(x >= xoffset and x < xoffset + width)
                   else 0 for x in range(n)]

def add_matrices(a, b):
    for x in range(len(a)):
        row = []
        for y in range(len(a[x])):
            row.append(a[x][y] + b[x][y])
        yield row

def overlap(a, b):
    for x in range(len(a)):
        for y in range(len(a[x])):
            if(a[x][y] != 0 and a[x][y] != b[x][y]):
                return True
    return False

def sum_matrices(lines, n):
    total = [[0] * n for _ in range(n)]

    for line in lines:
        xoffset, yoffset, width, height = parse_line(line)
        m = list(matrix(xoffset, yoffset, width, height, n))
        total = list(add_matrices(total, m))

    return total

total = sum_matrices(lines, 1000)

def part1(total, n):
    return sum([item > 1 for row in total for item in row])

def part2(lines, total, n):
    for i, line in enumerate(lines):
        xoffset, yoffset, width, height = parse_line(line)
        m = list(matrix(xoffset, yoffset, width, height, n))

        if not overlap(m, total):
            return i + 1
