from collections import deque

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    points = [tuple(map(int, line.split(","))) for line in lines]

def closest(location, points):
    x, y = location
    distances = [abs(i-x) + abs(y-j) for i, j in points]
    minimum = min(distances)

    return [index for index, distance in enumerate(distances) if distance == minimum]

def borders(points):
    topleft = (min([x for x, y in points]),
               min([y for x, y in points]))

    bottomright = (max([x for x, y in points]),
                   max([y for x, y in points]))

    return topleft, bottomright

def infinite(point, borders):
    x, y = point
    topleft, bottomright = borders

    if x <= topleft[0] or x >= bottomright[0]:
        return True
    elif y <= topleft[1] or y >= bottomright[1]:
        return True
    else:
        return False

def flood(location, points, index, grid_borders):
    zone = deque([location])
    q = deque([location])

    while(q):
        x, y = q.pop()

        directions = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

        for direction in directions:
            idx_closest = closest(direction, points)

            if direction in zone:
                pass
            elif len(idx_closest) > 1:
                pass
            elif idx_closest[0] != index:
                pass
            elif infinite(direction, grid_borders):
                return False
            else:
                zone.append(direction)
                q.append(direction)

    return zone

def part1(points):
    output = {}
    grid_borders = borders(points)

    for index, location in enumerate(points):
        zone = flood(location, points, index, grid_borders)

        if zone:
            output[index] = len(zone)

    return max(output.values())

def centroid(points):
    x = sum([x for x, y in points]) / len(points)
    y = sum([y for x, y in points]) / len(points)

    return (round(x), round(y))

def critereon(point, points, n):
    x, y = point
    return sum([abs(x-i) + abs(y-j) for i, j in points]) < n

def flood2(start, points, n):
    zone = deque([start])
    q = deque([start])

    while(q):
        x, y = q.pop()
        directions = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]

        for direction in directions:
            if direction in zone:
                pass
            elif critereon(direction, points, n):
                zone.append(direction)
                q.append(direction)
            else:
                pass

    return zone

def part2(points, n):
    start = centroid(points)
    zone = flood2(start, points, n)

    return len(zone)
