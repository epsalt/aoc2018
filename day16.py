import re

with open("samples.txt") as f:
    before = []
    instruction = []
    after = []

    for line in f:
        if re.match("Before:", line):
            before.append(list(map(int, line[9:19].split(", "))))
        elif re.match("After:", line):
            after.append(list(map(int, line[9:19].split(", "))))
        else:
            if line.strip() != "":
                instruction.append(list(map(int, line.split(" "))))

    tests = list(zip(before, instruction, after))

with open("program.txt") as f:
    program = []
    for line in f:
        program.append(list(map(int, line.split(" "))))


codes = set(['addr', 'addi', 'multr', 'multi', 'banr', 'bani', 'borr',
             'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir',
             'eqri', 'eqrr'])

def execute(name, a, b, r):
    d = {'addr':  lambda r, a, b: r[a] + r[b],
         'addi':  lambda r, a, b: r[a] + b,
         'multr': lambda r, a, b: r[a] * r[b],
         'multi': lambda r, a, b: r[a] * b,
         'banr':  lambda r, a, b: r[a] & r[b],
         'bani':  lambda r, a, b: r[a] & b,
         'borr':  lambda r, a, b: r[a] | r[b],
         'bori':  lambda r, a, b: r[a] | b,
         'setr':  lambda r, a, b: r[a],
         'seti':  lambda r, a, b: a,
         'gtir':  lambda r, a, b: int(a > r[b]),
         'gtri':  lambda r, a, b: int(r[a] > b),
         'gtrr':  lambda r, a, b: int(r[a] > r[b]),
         'eqir':  lambda r, a, b: int(a == r[b]),
         'eqri':  lambda r, a, b: int(r[a] == b),
         'eqrr':  lambda r, a, b: int(r[a] == r[b])}

    f = d[name]

    return f(r, a, b)

def part1(tests, codes):
    total = 0

    for before, instruction, after in tests:
        hits = 0
        _, a, b, c = instruction
        for code in codes:
            result = before[:]
            result[c] = execute(code, a, b, before)
            if result == after:
                hits += 1

        if hits >= 3:
            total +=1

    return total

def part2(tests, codes, program):
    code_dict = {}

    while(codes):
        for before, instruction, after in tests:
            hits = []
            n, a, b, c = instruction
            for code in codes:
                result = before[:]
                result[c] = execute(code, a, b, before)
                if result == after:
                    hits.append((n, code))

            if len(hits) == 1:
                i, j = hits[0]
                code_dict[i] = j
                codes.remove(j)

    state = [0, 0, 0, 0]

    for instruction in program:
        n, a, b, c, = instruction
        code = code_dict[n]
        state[c] = execute(code, a, b, state)

    return state
