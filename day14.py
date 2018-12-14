def part1(n, after=10):
    scoreboard = '37'
    positions = (0, 1)

    while(len(scoreboard) < (n + after)):
        scoreboard += str(int(scoreboard[positions[0]]) + int(scoreboard[positions[1]]))
        positions = [(position + 1 + int(scoreboard[position])) % len(scoreboard) for position in positions]

    return scoreboard[n:n+10]

def part2(token):
    scoreboard = '37'
    positions = (0, 1)
    length = len(token)

    while(token not in scoreboard[-length-1:]):
        scoreboard += str(int(scoreboard[positions[0]]) + int(scoreboard[positions[1]]))
        positions = [(position + 1 + int(scoreboard[position])) % len(scoreboard) for position in positions]

    return scoreboard.index(token)
