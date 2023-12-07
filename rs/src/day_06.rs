use std::ops::Div;

use crate::search;

pub struct Part1 {
    times: Vec<u32>,
    dists: Vec<u32>,
}

impl TryFrom<&str> for Part1 {
    type Error = String;

    fn try_from(s: &str) -> Result<Self, Self::Error> {
        let (times_str, dists_str) = s.split_once('\n').ok_or_else(|| "no newlines")?;
        let parse = |s: &str| -> Result<Vec<u32>, String> {
            let (_, s) = s.split_once(':').ok_or_else(|| "no :")?;
            s.split_whitespace()
                .map(|s| s.parse::<u32>().map_err(|e| e.to_string()))
                .collect::<Result<Vec<_>, _>>()
                .map_err(|e| e.to_string())
        };
        let times = parse(times_str)?;
        let dists = parse(dists_str)?;
        Ok(Part1 { times, dists })
    }
}

pub struct Part2 {
    time: u32,
    dist: u32,
}

impl TryFrom<&str> for Part2 {
    type Error = String;

    fn try_from(s: &str) -> Result<Self, Self::Error> {
        let (time_str, dist_str) = s.split_once('\n').ok_or_else(|| "no newlines")?;
        let parse = |s: &str| -> Result<u32, String> {
            let (_, s) = s.split_once(':').ok_or_else(|| "no :")?;
            s.split_whitespace()
                .intersperse("")
                .collect::<String>()
                .parse::<u32>()
                .map_err(|e| e.to_string())
        };
        let time = parse(time_str)?;
        let dist = parse(dist_str)?;
        Ok(Part2 { time, dist })
    }
}

#[aoc_generator(day6)]
pub fn get_input(input: &str) -> (Part1, Part2) {
    (input.try_into().unwrap(), input.try_into().unwrap())
}

fn ways_to_win(t: u32, d: u32) -> u32 {
    let lo_0 = 0;
    let hi_0 = t.div_ceil(2);
    let wins = |hold: &u32| hold * (t - hold) > d;
    let (_, first) = search::search(&search::binary, &wins, lo_0, hi_0);
    let last = t.div(2) + t.div_ceil(2) - first;
    last - first + 1
}

#[aoc(day6, part1)]
pub fn part_1(input: &(Part1, Part2)) -> u32 {
    input
        .0
        .times
        .iter()
        .zip(input.0.dists.iter())
        .map(|(&t, &d)| ways_to_win(t, d))
        .product()
}

#[aoc(day6, part2)]
pub fn part_2(input: &(Part1, Part2)) -> u32 {
    ways_to_win(input.1.time, input.1.dist)
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test_data/day_06.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT)), 288);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT)), 71503);
    }
}
