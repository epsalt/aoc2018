from datetime import datetime, timedelta
from collections import Counter, defaultdict
import re

with open("input.txt") as f:
    lines = sorted([line.strip() for line in f.readlines()])

def parse_lines(lines):
    dt_format = "%Y-%m-%d %H:%M"

    for line in lines:
        date = datetime.strptime(re.search('\[(.*?)\]', line).group(1), dt_format)

        if re.search("falls", line):
            status = "sleep"
        elif re.search("wakes", line):
            status = "wake"
        else:
            status = int(re.search("#(\d+)", line).group(1))

        yield(date, status)

def sleep_deltas(parsed_lines):
    deltas = defaultdict(list)
    state = "awake"

    for line in parsed_lines:
        dt, status = line

        if status == "sleep":
            start = dt
            state = "sleeping"
        elif status == "wake":
            deltas[guard].append((start, dt))
        else:
            if status == "sleeping":
                deltas[guard].append(start, dt)
            guard = status
            state = "awake"

    return deltas

def best_minute(deltas):
    minutes = Counter()
    for delta in deltas:
        start, end = delta

        for i in range(int((end - start).seconds / 60)):
            hhmm = (start + timedelta(seconds=(i*60))).strftime("%H%M")
            minutes[hhmm] += 1

    return minutes.most_common(1)

def part1(lines):
    parsed_lines = parse_lines(lines)
    deltas = sleep_deltas(parsed_lines)

    sleep_time = {}
    for guard, delta_list in deltas.items():
        sleep_time[guard] = sum([(end - start).seconds for start, end in delta_list])

    sleepiest_guard = max(sleep_time, key=sleep_time.get)

    return sleepiest_guard * int(best_minute(deltas[sleepiest_guard])[0][0])

def part2(lines):
    parsed_lines = parse_lines(lines)
    deltas = sleep_deltas(parsed_lines)

    best_minutes = {}
    for guard in deltas.keys():
        best_minutes[guard] = best_minute(deltas[guard])

    sleepiest_guard = max(x, key=lambda d: x.get(d)[0][1])

    return sleepiest_guard * int(best_minutes[sleepiest_guard][0][0])
