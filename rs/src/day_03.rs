use std::collections::HashMap;

use crate::grid::Grid;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Cell {
    Blank,
    Digit(usize),
    Symbol,
    Gear,
}

impl Cell {
    fn is_part(&self) -> bool {
        match self {
            Cell::Symbol => true,
            Cell::Gear => true,
            _ => false,
        }
    }
}

impl From<char> for Cell {
    fn from(c: char) -> Self {
        match c {
            '.' => Cell::Blank,
            '0'..='9' => Cell::Digit(c.to_digit(10).unwrap() as usize),
            '*' => Cell::Gear,
            _ => Cell::Symbol,
        }
    }
}

#[aoc_generator(day3)]
pub fn get_input(input: &str) -> Grid<Cell> {
    let w = input.lines().next().unwrap().len();
    let items: Vec<Cell> = input
        .lines()
        .map(|l| l.chars().map(Cell::from))
        .flatten()
        .collect();
    Grid { items, w }
}

#[aoc(day3, part1)]
pub fn part_1(grid: &Grid<Cell>) -> usize {
    let mut result = 0;
    let mut i = 0;
    let next_to_part = |i| grid.neighbors_all(i).iter().any(|c| c.is_part());
    while i < grid.items.len() {
        if let Cell::Digit(_) = grid[i] {
            let mut n = 0;
            let mut part = false;
            let mut di = 0;
            while (i % grid.w) + di < grid.w
                && let Cell::Digit(d) = grid[i + di]
            {
                n = n * 10 + d;
                part = part || next_to_part(i + di);
                di += 1;
            }
            if part {
                result += n;
            }
            i += di;
        }
        i += 1;
    }
    result
}

#[aoc(day3, part2)]
pub fn part_2(grid: &Grid<Cell>) -> usize {
    let mut gear_nums: HashMap<usize, Vec<usize>> = HashMap::new();
    let mut i = 0;
    let next_to_gear = |i| {
        grid.neighbor_ixs_all(i)
            .iter()
            .find_map(|&j| (grid[j] == Cell::Gear).then(|| j))
    };
    while i < grid.items.len() {
        if let Cell::Digit(_) = grid[i] {
            let mut n = 0;
            let mut gear = None;
            let mut di = 0;
            while (i % grid.w) + di < grid.w
                && let Cell::Digit(d) = grid[i + di]
            {
                n = n * 10 + d;
                gear = gear.or(next_to_gear(i + di));
                di += 1;
            }
            if let Some(i_gear) = gear {
                gear_nums.entry(i_gear).or_default().push(n);
            }
            i += di;
        }
        i += 1;
    }
    gear_nums
        .iter()
        .filter_map(|(_, v)| (v.len() == 2).then(|| v[0] * v[1]))
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test_data/day_03.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT)), 4361);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT)), 467835);
    }
}
