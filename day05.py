from collections import deque
from string import ascii_lowercase

with open('input.txt') as myfile:
    string = myfile.read().strip()

def loop(q, letter=None):
    out = deque()

    while(q):
        if q[0].lower() == letter:
            q.popleft()
        elif len(q) == 1:
            out.append(q.popleft())
        elif q[0].swapcase() == q[1]:
            q.popleft()
            q.popleft()
        else:
            out.append(q.popleft())

    return out

def part1(string, letter=None):
    q = deque(string)
    l = len(q)

    while(1):
        q = loop(q, letter)
        if len(q) == l:
            return q
        else:
            l = len(q)

def part2(string):
    letter_counts = {letter: len(part1(string, letter)) for letter in ascii_lowercase}
    min_letter = min(letter_counts, key=letter_counts.get)

    return letter_counts[min_letter]
