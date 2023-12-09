from aocd import get_data

YEAR = 2023
DAY = 9


def preprocess(data):
    return [[int(x) for x in l.split()] for l in data.splitlines()]


def f(data):
    results = [data]
    diffs = data
    while True:
        diffs = [b - a for a, b in zip(diffs[:-1], diffs[1:])]
        results.append(diffs)
        if all(d == 0 for d in diffs):
            break
    extrapolate = 0
    for i in range(len(results) - 1, -1, -1):
        extrapolate += results[i][-1]
    return extrapolate


def part_1(data):
    return sum(f(l) for l in data)  # type: ignore


def g(data):
    results = [data]
    diffs = data
    while True:
        diffs = [b - a for a, b in zip(diffs[:-1], diffs[1:])]
        results.append(diffs)
        if all(d == 0 for d in diffs):
            break
    extrapolate = 0
    for i in range(len(results) - 1, -1, -1):
        extrapolate = results[i][0] - extrapolate
    return extrapolate


def part_2(data):
    return sum(g(l) for l in data)


test = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

test_2 = """\
10 13 16 21 30 45
"""

test_3 = """\
"""


def main():
    data = get_data(day=DAY, year=YEAR)
    print("----------------------------------------")
    print()
    print("test 1: ", part_1(preprocess(test)))
    print("ANSWER 1: ", part_1(preprocess(data)))
    print()
    print("----------------------------------------")
    print()
    print(part_2(preprocess(test_2)))
    print()
    print("test 2: ", part_2(preprocess(test)))
    print("ANSWER 2: ", part_2(preprocess(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
