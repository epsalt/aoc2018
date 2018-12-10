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

def simulate(points):
    for point in points:
        yield Vector(Point(point.position.x + point.velocity.x,
                           point.position.y + point.velocity.y),
                     Point(*point.velocity))

def corners(points):
    tl = Point(min([point.position.x for point in points]),
               min([point.position.y for point in points]))

    br = Point(max([point.position.x for point in points]),
               max([point.position.y for point in points]))

    return tl, br

def area(points):
    tl, br = corners(points)
    return (br.x - tl.x) * (br.y - tl.y)

def pretty_print(points):
    tl, br = corners(points)
    coords = [x.position for x in points]

    for y in range(tl.y, br.y+1):
        for x in range(tl.x, br.x+1):
            if Point(x, y) in coords:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

def solve(lines):
    points = list(parse(lines))
    a = area(points)
    t = 0

    while(True):

        new_points = list(simulate(points))
        new_a = area(new_points)

        if new_a > a:
            pretty_print(points)
            return t

        else:
            points = new_points
            a = new_a

        t += 1
