from collections import deque

with open('input.txt') as myfile:
    string = myfile.read().strip()
    q = deque(map(int, string.split(" ")))

def parse(q):
    if q:
        n_children = q.popleft()
        n_metadata = q.popleft()

        children = []
        for _ in range(n_children):
            children.append(parse(q))

        metadata = []
        for _ in range(n_metadata):
            metadata.append(q.popleft())

        return {'children': children, 'metadata': metadata}

def total_metadata_sum(tree):
    s = 0

    if tree['metadata']:
        s += sum(tree['metadata'])

    for child in tree['children']:
        s += total_metadata_sum(child)

    return s

def child_node_metadata_sum(tree):
    s = 0

    if not tree['children']:
        s += sum(tree['metadata'])
    else:
        for i in tree['metadata']:
            children = tree['children']

            if i <= len(children):
                child = children[i-1]
                s += child_node_metadata_sum(child)

    return s

def part1(q):
    return total_metadata_sum(parse(q))

def part2(q):
    return child_node_metadata_sum(parse(q))
