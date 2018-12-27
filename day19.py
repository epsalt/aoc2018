with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    ip = int(lines[0].split(" ")[1])
    parse = lambda x: [int(y) if y.isdigit() else y for y in x.split(" ")]
    instructions = [parse(line) for line in lines[1:]]

def execute(name, a, b, r):
    d = {'addr':  lambda r, a, b: r[a] + r[b],
         'addi':  lambda r, a, b: r[a] + b,
         'mulr':  lambda r, a, b: r[a] * r[b],
         'muli':  lambda r, a, b: r[a] * b,
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

def factors(n):
    i = n
    while i > 0:
        if n % i == 0:
            yield i
        i -= 1

def part1(ip, instructions):
    state = [0, 0, 0, 0, 0, 0]
    l = range(len(instructions))
    n = state[ip]

    while n in l:
        instruction, a, b, c = instructions[n]
        state[c] = execute(instruction, a, b, state)
        state[ip] += 1
        n = state[ip]

    return state

def part2(ip, instructions):
    state = [1, 0, 0, 0, 0, 0]
    n = state[ip]

    while n != 34:
        instruction, a, b, c = instructions[n]
        state[c] = execute(instruction, a, b, state)
        state[ip] += 1
        n = state[ip]

    return sum(factors(state[1]))
