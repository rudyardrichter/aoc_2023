from collections import defaultdict

from aocd import get_data

from aoc_2023.lib import *

YEAR = 2023
DAY = 3


def preprocess(data):
    return data


def is_symbol(c):
    return not c.isdigit() and c != "."


def part_1(data):
    data = data.splitlines()
    inbounds = lambda i, j: 0 <= i < len(data) and 0 <= j < len(data[0])
    nums = []
    for y, row in enumerate(data):
        to_skip = 0
        for x, ch in enumerate(row):
            if to_skip > 0:
                to_skip -= 1
            else:
                if ch.isdigit():
                    next_to_part = False
                    x_i = x
                    n = 0
                    while inbounds(y, x_i) and data[y][x_i].isdigit():
                        to_skip += 1
                        n = n * 10 + int(data[y][x_i])
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if inbounds(y + dy, x_i + dx) and is_symbol(
                                    data[y + dy][x_i + dx]
                                ):
                                    next_to_part = True
                        x_i += 1
                    if next_to_part:
                        nums.append(n)
    return sum(nums)


def part_2(data):
    data = data.splitlines()
    inbounds = lambda i, j: 0 <= i < len(data) and 0 <= j < len(data[0])
    gearnums = defaultdict(list)
    for y, row in enumerate(data):
        to_skip = 0
        for x, ch in enumerate(row):
            if to_skip > 0:
                to_skip -= 1
            else:
                if ch.isdigit():
                    x_i = x
                    n = 0
                    next_to_gears = set()
                    while inbounds(y, x_i) and data[y][x_i].isdigit():
                        to_skip += 1
                        n = n * 10 + int(data[y][x_i])
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                if (
                                    inbounds(y + dy, x_i + dx)
                                    and data[y + dy][x_i + dx] == "*"
                                ):
                                    next_to_gears.add((y + dy, x_i + dx))
                        x_i += 1
                    for gear in next_to_gears:
                        gearnums[gear].append(n)
    return sum(v[0] * v[1] for v in gearnums.values() if len(v) == 2)


test = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def main():
    data = preprocess(get_data(day=3, year=2023))
    print("----------------------------------------")
    print()
    print("test 1: ", part_1(preprocess(test)))
    print("ANSWER 1: ", part_1(data))
    print()
    print("----------------------------------------")
    print()
    print("test 2: ", part_2(preprocess(test)))
    print("ANSWER 2: ", part_2(data))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    # if len(sys.argv) > 1 and sys.argv[1] == "1":
    #     answer = part_1(preprocess(get_data(day=DAY, year=YEAR)))
    #     print(f"SUBMITTING ANSWER 1: {answer}")
    #     submit(answer, part="a", day=2, year=2023)  # type: ignore
    # elif len(sys.argv) > 1 and sys.argv[1] == "2":
    #     answer = part_2(preprocess(get_data(day=DAY, year=YEAR)))
    #     print(f"SUBMITTING ANSWER 2: {answer}")
    #     submit(answer, part="b", day=2, year=2023)  # type: ignore
    # else:
    #     main()
    main()
