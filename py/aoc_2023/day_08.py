import math
from dataclasses import dataclass

from aocd import get_data

YEAR = 2023
DAY = 8


def parse_line(l):
    a, b = l.split("=")
    start = a.strip()
    l = b.split(",")[0][-3:]
    r = b.split(",")[1][1:4]
    return (start, l, r)


def preprocess_1(data):
    rl, paths = data.split("\n\n")
    paths = [parse_line(p) for p in paths.split("\n") if p]
    paths = {start: (l, r) for (start, l, r) in paths}
    return rl, paths


def preprocess_2(data):
    return preprocess_1(data)


def part_1(data):
    return f(*data)


def f(rl, paths, start="AAA", end: str | None = "ZZZ"):
    result = 0
    current = start
    while True:
        r_or_l = rl[result % len(rl)]
        current = paths[current][0] if r_or_l == "L" else paths[current][1]
        result += 1
        if (end and current == "ZZZ") or (not end and current.endswith("Z")):
            break
    return result


def part_2(data):
    rl, paths = data
    starts = [p for p in paths.keys() if p.endswith("A")]
    return math.lcm(*[f(rl, paths, start=s, end=None) for s in starts])


test = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test_2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

test_3 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


t = part_1(preprocess_1(test))
assert t == 2, t
t = part_1(preprocess_1(test_2))
assert t == 6, t
t = part_2(preprocess_1(test_2))
assert t == 6, t
t = part_2(preprocess_1(test_3))
assert t == 6, t


def main():
    data = get_data(day=DAY, year=YEAR)
    print("----------------------------------------")
    print()
    print("test 1: ", part_1(preprocess_1(test)))
    print("ANSWER 1: ", part_1(preprocess_1(data)))
    print()
    print("----------------------------------------")
    print()
    print("test 2: ", part_2(preprocess_2(test)))
    print("ANSWER 2: ", part_2(preprocess_2(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
