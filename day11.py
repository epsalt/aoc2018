def calc(x, y, serial):
    rack_id = x + 10
    power_level = (((rack_id) * y) + serial) * rack_id
    hundreds = int(str(power_level)[-3])
    return hundreds - 5

def make_grid(serial):
    grid = []
    for x in range(1, 301):
        row = []
        for y in range(1, 301):
            row.append(calc(x, y, serial))
        grid.append(row)

    return grid

def selection(x, y, grid, size):
    s = 0
    for i in range(x, x+size):
        s += sum(grid[i][y:y+size])
    return s

def part1(grid):
    out = 0
    for x in range(len(grid)-3):
        for y in range(len(grid[0])-3):
            s = selection(x, y, grid, 3)
            if s > out:
                out = s
                winner = (x, y)

    return winner[0]+1, winner[1]+1

def part2(grid):
    out = 0
    for x in range(0, 300):
        for y in range(0, 300):
            size = min(300-x, 300-y)
            total = 0
            for s in range(size):
                for i in range(x, x+s):
                    total += grid[i][y+s]

                for j in range(y, y+s):
                    total += grid[x+s][j]

                total += grid[x+s][y+s]

                if total > out:
                    out = total
                    solution = (x+1, y+1, s+1)

    return solution
