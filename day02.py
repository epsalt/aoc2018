from collections import Counter

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def reps(lines, n):
    out = 0

    for line in lines:
        cnt = Counter()

        for letter in line:
            cnt[letter] += 1

        if n in set(cnt.values()):
            out += 1

    return out

def part1(lines):
    return reps(lines, 2) * reps(lines, 3)

def part2(lines):
    lines = lines[:]

    while(True):
        popped = lines.pop()

        for line in lines:
            if sum([a != b for a, b in zip(popped, line)]) == 1:
                return ''.join([a for a, b in zip(popped, line) if a == b])
