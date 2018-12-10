import re
import sys

from collections import namedtuple

Vector = namedtuple('Vector', 'position, velocity')
Point = namedtuple('Point', 'x, y')

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def parse(lines):
    for line in lines:
       position, velocity = re.findall(r'\<(.*?)\>', line)

       position = [int(s) for s in position.split(",")]
       velocity = [int(s) for s in velocity.split(",")]

       yield Vector(Point(*position), Point(*velocity))

def simulate(vectors):
    for vector in vectors:
        yield Vector(Point(vector.position.x + vector.velocity.x,
                           vector.position.y + vector.velocity.y),
                     Point(*vector.velocity))

def corners(vectors):
    tl = Point(min([vector.position.x for vector in vectors]),
               min([vector.position.y for vector in vectors]))

    br = Point(max([vector.position.x for vector in vectors]),
               max([vector.position.y for vector in vectors]))

    return tl, br

def area(vectors):
    tl, br = corners(vectors)
    return (br.x - tl.x) * (br.y - tl.y)

def pretty_print(vectors):
    tl, br = corners(vectors)
    coords = [x.position for x in vectors]

    for y in range(tl.y, br.y+1):
        for x in range(tl.x, br.x+1):
            if Point(x, y) in coords:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

def solve(lines):
    vectors = list(parse(lines))
    a = area(vectors)
    t = 0

    while(True):

        new_vectors = list(simulate(vectors))
        new_a = area(new_vectors)

        if new_a > a:
            pretty_print(vectors)
            return t

        else:
            vectors = new_vectors
            a = new_a

        t += 1
