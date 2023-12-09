use std::{collections::HashSet, iter};

/// e.g.
/// Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
pub struct Card {
    winning: HashSet<usize>,
    have: HashSet<usize>,
}

impl From<&str> for Card {
    fn from(s: &str) -> Self {
        let (_, nums) = s.split_once(":").unwrap();
        let (s_win, s_have) = nums.split_once("|").unwrap();
        let winning = s_win
            .split_whitespace()
            .map(|n| n.parse::<usize>().unwrap())
            .collect();
        let have = s_have
            .split_whitespace()
            .map(|n| n.parse::<usize>().unwrap())
            .collect();
        Self { winning, have }
    }
}

impl Card {
    fn n_winning(&self) -> usize {
        self.winning.intersection(&self.have).count()
    }

    fn score(&self) -> u32 {
        if self.n_winning() == 0 {
            0
        } else {
            2_u32.pow(self.n_winning() as u32 - 1)
        }
    }
}

#[aoc_generator(day4)]
pub fn get_input(input: &str) -> Vec<Card> {
    input.lines().map(|l| l.into()).collect()
}

#[aoc(day4, part1)]
pub fn part_1(cards: &Vec<Card>) -> u32 {
    cards.iter().map(Card::score).sum()
}

#[aoc(day4, part2)]
pub fn part_2(cards: &Vec<Card>) -> usize {
    let mut copies = iter::repeat(1).take(cards.len()).collect::<Vec<usize>>();
    for (i, card) in cards.iter().enumerate() {
        for j in i + 1..i + cards.len().min(card.n_winning() + 1) {
            copies[j] += copies[i];
        }
    }
    copies.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test_data/day_04.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT)), 13);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT)), 30);
    }
}
