from collections import defaultdict, deque

with open("input.txt") as f:
    string = f.read().strip()

def generate_paths(string):
    paths = set()
    stack = deque()
    path = ""

    for char in string:
        if char == "(":
            stack.append(path)
        elif char == ")":
            path = stack.pop()
        elif char == "|":
            path = stack[-1]
        else:
            path += char
            paths.add(path)

    return paths

def walk_paths(paths):
    d = {'N': (0, 1),
         'S': (0, -1),
         'W': (1, 0),
         'E': (-1, 0)}

    results = defaultdict(set)

    for path in paths:
        loc = (0, 0)

        for i, step in enumerate(path, 1):
            direction = d[step]
            loc = (loc[0] + direction[0], loc[1] + direction[1])
            results[loc].add(i)

    return results

def part1(string):
    string = string[1:-1]
    paths = generate_paths(string)
    distances = walk_paths(paths)

    return max([min(value) for value in distances.values()])

def part2(string):
    string = string[1:-1]
    paths = generate_paths(string)
    distances = walk_paths(paths)

    return sum([(min(value) >= 1000) for value in distances.values()])
