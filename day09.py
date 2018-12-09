from collections import Counter, deque

with open('input.txt') as f:
    string = f.read().strip()
    players, last_marble = [int(s) for s in string.split() if s.isdigit()]
    last_marble_part2 = last_marble * 100

def solve(players, last_marble):
    players = deque(range(players))
    scores = Counter()
    board = deque([0])

    for marble in range(1, last_marble+1):
        player = players[0]
        players.rotate(-1)

        if marble % 23 != 0:
            board.rotate(-2)
            board.appendleft(marble)

        else:
            scores[player] += marble
            board.rotate(7)
            scores[player] += board.popleft()


    winner = max(scores, key=scores.get)
    return scores[winner]
