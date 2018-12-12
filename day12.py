with open("input.txt") as f:
    lines = [l.strip() for l in f]
    initial = list(lines[0][15:])
    patterns = {l.split(" => ")[0]: l.split(" => ")[1] for l in lines[2:]}

def part1(initial, patterns, n):
    state = [".", ".", "."] + initial + [".", ".", "."]
    idx = -3
    s = 0
    for _ in range(n):
        state, idx = generation(state, patterns, idx)
        pots = zip(state, range(idx, len(state)+idx))

    return sum([pot for plant, pot in pots if plant == "#"])

def generation(state, patterns, idx):
    out = []
    buff = ["."] * 3

    if "#" in state[:3]:
        state = buff + state
        idx -= 3

    if "#" in state[-3:]:
        state = state + buff

    for i in range(len(state)):
        if i < 2 or i > len(state)-2:
            out.append(".")
        else:
            window = "".join(state[i-2:i+3])
            match = patterns.get(window)
            if match == "#":
                out.append("#")
            else:
                out.append(".")

    return out, idx


def inspect(initial, patterns, n):
    state = [".", ".", "."] + initial + [".", ".", "."]
    idx = -3
    s = 0
    for _ in range(n):
        state, idx = generation(state, patterns, idx)
        pots = zip(state, range(idx, len(state)+idx))
        new_s = sum([pot for plant, pot in pots if plant == "#"])
        print(_, new_s, new_s - s)
        s = new_s

# n   new_s  s
# 153 10818 -67
# 154 10951 133
# 155 11094 143
# 156 11237 143
# 157 11373 136
# 158 11454 81
# 159 11535 81
# 160 11616 81
# 161 11697 81
# 162 11778 81

def part2(n):
    return (n - 157) * 81 + 11373 - 81
