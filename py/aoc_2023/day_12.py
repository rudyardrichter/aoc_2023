from functools import cache

from aocd import get_data

YEAR = 2023
DAY = 12


@cache
def solve(cells: str, groups: tuple[int], n_broken: int) -> int:
    if not cells:
        if not groups and n_broken == 0:
            return 1
        if len(groups) == 1 and groups[0] == n_broken:
            return 1
        return 0
    result = 0
    if cells[0] == "?" or cells[0] == ".":
        if n_broken == 0:
            result += solve(cells[1:], groups, 0)
        elif groups and groups[0] == n_broken:
            result += solve(cells[1:], groups[1:], 0)
    if cells[0] == "?" or cells[0] == "#":
        result += solve(cells[1:], groups, n_broken + 1)
    return result


def preprocess(data):
    result = []
    for line in data.splitlines():
        cells, ns = line.split()
        ns = tuple(int(n) for n in ns.split(","))
        result.append((cells, ns))
    return result


def part_1(data):
    result = 0
    for cells, ns in data:
        result += solve(cells, ns, 0)
    return result


def part_2(data):
    result = 0
    for cells, ns in data:
        cells = "?".join(5 * [cells])
        ns = tuple(5 * list(ns))
        result += solve(cells, ns, 0)
    return result


test = """\
?###???????? 3,2,1
"""

test_2 = """\
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
    print()
    print("test 2: ", part_2(preprocess(test)))
    print("ANSWER 2: ", part_2(preprocess(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
