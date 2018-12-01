with open("input.txt") as f:
  lines = f.readlines()

def part1(lines):
  return sum([int(n) for n in lines])

def part2(lines):
  counter = 0
  cache = set([counter])

  while(1):
    for line in lines:
      counter += int(line)

      if counter in cache:
        return counter

      cache.add(counter)
