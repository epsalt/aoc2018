from collections import Counter, namedtuple

with open("input.txt") as f:
    lines = [list(line.replace("\n", "")) for line in f.readlines()]

cart = namedtuple("Cart", "position, direction, turn")

def initialize_carts(lines):
    cart_starts = {">": ("-", [0, 1]),
                   "<": ("-", [0, -1]),
                   "^": ("|", [-1, 0]),
                   "v": ("|", [1, 0])}
    carts = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            curr = lines[y][x]
            start = cart_starts.get(curr)
            if start is not None:
                replacement, direction = start
                carts.append(cart([y, x], direction, 0))
                lines[y][x] = replacement

    return lines, carts

def turn(symbol, cart):
    y, x = cart.direction
    n = cart.turn

    if symbol == "+":
        if n % 3 == 0:   # left
            return -x, y
        elif n % 3 == 1: # straight
            return y, x
        elif n % 3 == 2: # right
            return x, -y

    elif symbol == "\\":
        return x, y

    elif symbol == "/":
        return -x, -y

def step(board, carts):
    turns = ["\\", "/", "+"]

    crashes = set()
    new_carts = []
    carts = carts[:]

    while(carts):
        current_cart = carts.pop()
        y, x = current_cart.position

        if (y, x) not in crashes:
            n = current_cart.turn
            tile = board[y][x]

            if tile in turns:
                new_direction = turn(tile, current_cart)
                if tile == "+":
                    n += 1
            elif tile == " ":
                raise RuntimeError("Derailment!!!!")
            else:
                new_direction = current_cart.direction

            new_position = [y + new_direction[0], x + new_direction[1]]

            if new_position in [cart.position for cart in carts]:
                crashes.add(tuple(new_position))
            elif new_position in [cart.position for cart in new_carts]:
                crashes.add(tuple(new_position))
            else:
                new_carts.append(cart(new_position, new_direction, n))

    alive_carts = [cart for cart in new_carts if tuple(cart.position) not in crashes]

    return alive_carts, crashes

## Returns [y, x]
def part1(lines):
    board, carts = initialize_carts(lines)
    while(True):
        carts, crashes = step(board, carts)
        if len(crashes) >= 1:
            return crashes

## Returns [y, x]
def part2(lines):
    board, carts = initialize_carts(lines)
    while(len(carts) > 1):
        carts, crashes = step(board, carts)

    return [cart.position for cart in carts]
