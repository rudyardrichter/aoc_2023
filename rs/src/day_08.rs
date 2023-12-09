use num::Integer;
use sscanf::scanf;
use std::{collections::HashMap, iter::Cycle};

enum Step {
    L,
    R,
}

impl TryFrom<char> for Step {
    type Error = ();

    fn try_from(value: char) -> Result<Self, Self::Error> {
        match value {
            'L' => Ok(Step::L),
            'R' => Ok(Step::R),
            _ => Err(()),
        }
    }
}

struct Path(u64, u64, u64);

fn tag_to_u64(s: &str) -> Result<u64, ()> {
    (s.len() == 3)
        .then(|| s.chars().fold(0, |acc, c| (acc << 8) + c as u64))
        .ok_or(())
}

impl TryFrom<&str> for Path {
    type Error = ();

    fn try_from(s: &str) -> Result<Self, Self::Error> {
        let (a, b, c) = scanf!(s, "{str} = ({str}, {str})").map_err(|_| ())?;
        Ok(Path(tag_to_u64(a)?, tag_to_u64(b)?, tag_to_u64(c)?))
    }
}

pub struct Input {
    steps: Vec<Step>,
    paths: HashMap<u64, (u64, u64)>,
}

#[aoc_generator(day8)]
pub fn get_input(input: &str) -> Input {
    let (steps_s, paths_s) = input.split_once("\n\n").unwrap();
    let steps = steps_s
        .chars()
        .map(Step::try_from)
        .collect::<Result<Vec<Step>, ()>>()
        .unwrap();
    let paths = paths_s
        .lines()
        .map(|l| Path::try_from(l).map(|p| (p.0, (p.1, p.2))))
        .collect::<Result<HashMap<u64, (u64, u64)>, ()>>()
        .unwrap();
    Input { steps, paths }
}

#[aoc(day8, part1)]
pub fn part_1(input: &Input) -> u64 {
    let mut current = tag_to_u64("AAA").unwrap();
    for (i, step) in (0..).zip(input.steps.iter().cycle()) {
        current = match step {
            Step::L => input.paths[&current].0,
            Step::R => input.paths[&current].1,
        };
        if current == tag_to_u64("ZZZ").unwrap() {
            return i + 1;
        }
    }
    panic!("didn't find end");
}

#[aoc(day8, part2)]
pub fn part_2(input: &Input) -> u64 {
    input
        .paths
        .iter()
        .filter(|(&k, _)| (k & 0xFF) == ('A' as u64))
        .fold(1, |acc, (&k, _)| {
            let mut current = k;
            for (i, step) in (0..).zip(input.steps.iter().cycle()) {
                current = match step {
                    Step::L => input.paths[&current].0,
                    Step::R => input.paths[&current].1,
                };
                if (current & 0xFF) == ('Z' as u64) {
                    return (i + 1).lcm(&acc);
                }
            }
            panic!()
        })
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT_1: &str = include_str!("../test_data/day_08.txt");
    const INPUT_2: &str = include_str!("../test_data/day_08_2.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT_1)), 2);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT_2)), 6);
    }
}
