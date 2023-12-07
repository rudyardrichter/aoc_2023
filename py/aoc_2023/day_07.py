from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import total_ordering

from aocd import get_data

YEAR = 2023
DAY = 7


def char_to_card(c):
    if c.isdigit():
        return int(c)
    elif c == "T":
        return 10
    elif c == "J":
        return 11
    elif c == "Q":
        return 12
    elif c == "K":
        return 13
    else:
        assert c == "A", c
        return 14


ranks = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,),
]
ranks = dict(zip(ranks, range(len(ranks))))


@total_ordering
@dataclass
class Hand:
    cards: list[int]
    s: str

    @classmethod
    def from_str(cls, s):
        return cls(list(map(char_to_card, s)), s)

    def rank(self) -> int:
        return ranks[tuple(sorted(Counter(self.cards).values()))]  # type: ignore

    def rank_wild(self) -> int:
        c = Counter(self.cards)
        if 1 in c:
            if c[1] == 5:
                return ranks[(5,)]  # type: ignore
            d = dict(c)
            d.pop(1)
            best = max(d.keys(), key=lambda k: d[k])
            c[best] += c.pop(1)
        return ranks[tuple(sorted(c.values()))]  # type: ignore

    def __lt__(self, other):
        return (self.rank(), self.cards) < (other.rank(), other.cards)


@total_ordering
@dataclass
class Hand2(Hand):
    def __lt__(self, other):
        return (self.rank_wild(), self.cards) < (other.rank_wild(), other.cards)


@total_ordering
@dataclass
class D:
    hand: Hand
    bid: int

    @classmethod
    def from_str(cls, s):
        hand, bid = s.split()
        return cls(Hand.from_str(hand), int(bid))

    def __lt__(self, other):
        return self.hand < other.hand


@total_ordering
@dataclass
class D2:
    hand: Hand2
    bid: int

    @classmethod
    def from_str(cls, s):
        hand, bid = s.split()
        return cls(Hand2.from_str(hand), int(bid))

    def __lt__(self, other):
        return self.hand < other.hand


def preprocess_1(data):
    return [D.from_str(line) for line in data.splitlines()]


def preprocess_2(data):
    return [D2.from_str(line.replace("J", "1")) for line in data.splitlines()]


def part_1(data):
    result = 0
    for i, d in enumerate(sorted(data)):
        result += d.bid * (i + 1)
    return result


def part_2(data):
    result = 0
    for i, d in enumerate(sorted(data)):
        result += d.bid * (i + 1)
    return result


test = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


t = part_1(preprocess_1(test))
assert t == 6440, t

t = part_2(preprocess_2(test))
assert t == 5905, t


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
