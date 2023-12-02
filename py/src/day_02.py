from dataclasses import dataclass

from aocd import get_data


@dataclass
class Game:
    i: int
    r: int
    g: int
    b: int

    @classmethod
    def from_str(cls, s):
        prefix, suffix = s.split(":")
        i = int(prefix.split()[-1])
        games = suffix.split(";")
        max_r = max_g = max_b = 0
        for game in games:
            balls = game.split(",")
            for ball in balls:
                count, color = ball.split()
                count = int(count)
                if color == "red":
                    max_r = max(max_r, count)
                elif color == "green":
                    max_g = max(max_g, count)
                elif color == "blue":
                    max_b = max(max_b, count)
        return cls(i, max_r, max_g, max_b)


def preprocess(data):
    return [Game.from_str(line) for line in data.splitlines()]


def part_1(data):
    return sum(
        game.i for game in data if game.r <= 12 and game.g <= 13 and game.b <= 14
    )


def part_2(data):
    return sum(game.r * game.g * game.b for game in data)


test = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def main():
    data = preprocess(get_data(day=2, year=2023))
    print(part_1(preprocess(test)))
    print(part_1(data))
    print(part_2(preprocess(test)))
    print(part_2(data))


if __name__ == "__main__":
    main()
