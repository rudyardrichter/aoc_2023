pub struct Game {
    i: usize,
    r: usize,
    g: usize,
    b: usize,
}

impl From<&str> for Game {
    fn from(input: &str) -> Self {
        let (prefix, suffix) = input.split_once(":").unwrap();
        let i = prefix.split_once(" ").unwrap().1.parse::<usize>().unwrap();
        let mut max_r = 0;
        let mut max_g = 0;
        let mut max_b = 0;
        for game in suffix.split(";") {
            for ball in game.split(",") {
                let (count, color) = ball.trim().split_once(" ").unwrap();
                match color {
                    "red" => {
                        max_r = max_r.max(count.parse::<usize>().unwrap());
                    }
                    "green" => {
                        max_g = max_g.max(count.parse::<usize>().unwrap());
                    }
                    "blue" => {
                        max_b = max_b.max(count.parse::<usize>().unwrap());
                    }
                    _ => panic!("Unknown color {}", color),
                }
            }
        }
        Self {
            i,
            r: max_r,
            g: max_g,
            b: max_b,
        }
    }
}

#[aoc_generator(day2)]
pub fn get_input(input: &str) -> Vec<Game> {
    input.lines().map(|l| l.into()).collect()
}

#[aoc(day2, part1)]
pub fn part_1(games: &Vec<Game>) -> usize {
    games
        .iter()
        .filter_map(|g| {
            if g.r <= 12 && g.g <= 13 && g.b <= 14 {
                Some(g.i)
            } else {
                None
            }
        })
        .sum()
}

#[aoc(day2, part2)]
pub fn part_2(games: &Vec<Game>) -> usize {
    games.iter().map(|g| g.r * g.g * g.b).sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test_data/day_02.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT)), 8);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT)), 2286);
    }
}
