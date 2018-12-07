from collections import deque, defaultdict
from string import ascii_uppercase

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    pairs = [(line[36], line[5]) for line in lines]

deps = defaultdict(set)
tasks = set()

for pair in pairs:
    task, dep = pair

    deps[task].add(dep)

    for item in (task, dep):
        tasks.add(item)

def part1(deps, tasks):
    out = []
    while tasks:
        can_do = [task for task in tasks if not deps[task]]
        doing = min(can_do)
        out.append(doing)
        tasks.remove(doing)

        for dep in deps.keys():
            if doing in deps[dep]:
                deps[dep].remove(doing)

    return "".join(out)

def part2(deps, tasks, n_workers, penalty):
    scheduler = []
    time = 0
    times = {task: ascii_uppercase.index(task) + 1 + penalty for task in tasks}

    while tasks or scheduler:

        new_scheduler = []
        for task, time_left in scheduler:
            if time_left == 1:
                for dep in deps.keys():
                    if task in deps[dep]:
                        deps[dep].remove(task)
            else:
                new_scheduler.append([task, time_left-1])

        scheduler = new_scheduler

        can_do = sorted([task for task in tasks if not deps[task]])

        while len(scheduler) < n_workers:
            if can_do:
                doing = can_do.pop(0)
                tasks.remove(doing)
                weight = times[doing]
                scheduler.append([doing, weight])
            else:
                break

        time += 1

    return time-1
