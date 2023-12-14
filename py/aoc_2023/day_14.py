from functools import cache

from aocd import get_data

YEAR = 2023
DAY = 14


def preprocess(data) -> list[list[str]]:
    return [[c for c in line] for line in data.splitlines()]


def load(grid):
    result = 0
    n = len(grid)
    for i, row in enumerate(grid):
        for c in row:
            if c == "O":
                result += n - i
    return result


def slide_north(grid: list[list[str]]):
    for i in range(len(grid)):
        col = [row[i] for row in grid]
        new = slide_col("".join(col))
        for j, row in enumerate(grid):
            row[i] = new[j]
    return grid


@cache
def slide_col(col):
    if not col:
        return ""
    c = col[0]
    if c == "#" or c == "O":
        return c + slide_col(col[1:])
    assert c == ".", c
    has_rock = "".join(col).lstrip(".").startswith("O")
    if not has_rock:
        return "." + slide_col(col[1:])
    next_rock = "".join(col).index("O")
    result = list(col)
    result[next_rock] = "."
    return "O" + slide_col("".join(result[1:]))


def slide_south(grid):
    grid = invert_grid(grid)
    grid = slide_north(grid)
    return invert_grid(grid)


def slide_west(grid):
    grid = transpose_grid(grid)
    grid = slide_north(grid)
    return transpose_grid(grid)


def slide_east(grid):
    grid = transpose_grid(grid)
    grid = slide_south(grid)
    return transpose_grid(grid)


def invert_grid(grid):
    return [row[::-1] for row in grid[::-1]]


def transpose_grid(grid):
    return list(map(list, zip(*grid)))


def part_1(data):
    return load(slide_north(data))


def part_2(data):
    grid = data
    grid_to_i = {}
    n = 1000000000
    i_last = None
    last = None
    period = None
    for i in range(1, n):
        grid = slide_east(slide_south(slide_west(slide_north(grid))))
        grid_s = "\n".join(["".join(row) for row in grid])
        if grid_s in grid_to_i:
            i_last = i
            last = grid_s
            period = i - grid_to_i[grid_s]
            break
        grid_to_i[grid_s] = i
    assert i_last and last and period
    i_to_grid = {v: k.splitlines() for k, v in grid_to_i.items()}
    j = (i_last - period) + ((n - i_last) % period)
    grid = i_to_grid[j]
    return load(grid)


test = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def main():
    data = get_data(day=DAY, year=YEAR)
    print("----------------------------------------")
    print()
    t = part_1(preprocess(test))
    assert t == 136, t
    print("ANSWER 1: ", part_1(preprocess(data)))
    print()
    print("----------------------------------------")
    print()
    t = part_2(preprocess(test))
    assert t == 64, t
    print("ANSWER 2: ", part_2(preprocess(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
