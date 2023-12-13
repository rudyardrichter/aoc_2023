import numpy as np
from aocd import get_data

YEAR = 2023
DAY = 13


def preprocess(data):
    grids = data.strip().split("\n\n")
    result = []
    for g in grids:
        lines = g.strip().splitlines()
        grid = [[c for c in line] for line in lines]
        result.append(np.array(grid))
    return result


def reflects_over(grid: np.ndarray, smudges: int = 0):
    for i in range(1, grid.shape[1]):
        left = grid[:, :i]
        right = grid[:, i:]
        right = right[:, : left.shape[1]]
        left = left[:, -right.shape[1] :]
        assert left.shape == right.shape
        right = np.flip(right, axis=1)
        n_diff = np.sum(left != right)
        if n_diff == smudges:
            return i
    return None


def f(data, n):
    vs = []
    hs = []
    for grid in data:
        x = reflects_over(grid, smudges=n)
        if x:
            vs.append(x)
            continue
        else:
            x = reflects_over(np.rot90(grid), smudges=n)
            assert x
            hs.append(x)
    return sum(vs) + 100 * sum(hs)


def part_1(data):
    return f(data, 0)


def part_2(data):
    return f(data, 1)


test = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

"""


def main():
    data = get_data(day=DAY, year=YEAR)
    print("----------------------------------------")
    print()
    assert part_1(preprocess(test)) == 405
    print("ANSWER 1: ", part_1(preprocess(data)))
    print()
    print("----------------------------------------")
    print()
    assert part_2(preprocess(test)) == 400
    print("ANSWER 2: ", part_2(preprocess(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
