from collections import deque
from functools import cache, reduce

from aocd import get_data

YEAR = 2023
DAY = 15


def preprocess(data):
    return data.strip()


def step(acc, c):
    return (17 * (acc + ord(c))) % 256


def solve(segment):
    result = 0
    for c in segment:
        result = step(result, c)
    return result


def part_1(data):
    return sum(solve(segment.strip()) for segment in data.strip().split(","))


def power(boxes):
    result = 0
    for i, box in enumerate(boxes):
        for j, (_, focal) in enumerate(box):
            result += (i + 1) * (j + 1) * int(focal)
    return result


def part_2(data):
    boxes = [deque() for _ in range(256)]

    def remove(i_box, label):
        labels = [l for l, _ in boxes[i_box]]
        try:
            i_label = labels.index(label)
            boxes[i_box].remove(boxes[i_box][i_label])
            return i_label
        except ValueError:
            return None

    for instr in data.strip().split(","):
        if "=" in instr:
            label, focal = instr.split("=")
            i_box = solve(label)
            if (i_label := remove(i_box, label)) is not None:
                boxes[i_box].insert(i_label, (label, focal))
            else:
                boxes[i_box].append((label, focal))
        else:
            assert "-" in instr
            label, _ = instr.split("-")
            i_box = solve(label)
            remove(i_box, label)
    return power(boxes)


test = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


def main():
    data = get_data(day=DAY, year=YEAR)
    print("----------------------------------------")
    print()
    assert part_1(preprocess("HASH")) == 52
    t = part_1(preprocess(test))
    assert t == 1320, t
    print("ANSWER 1: ", part_1(preprocess(data)))
    print()
    print("----------------------------------------")
    print()
    t = part_2(preprocess(test))
    assert t == 145, t
    print("ANSWER 2: ", part_2(preprocess(data)))
    print()
    print("----------------------------------------")


if __name__ == "__main__":
    main()
