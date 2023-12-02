use std::collections::HashMap;

#[aoc_generator(day1)]
pub fn get_input(input: &str) -> String {
    input.to_string()
}

#[aoc(day1, part1)]
pub fn part_1(input: &String) -> usize {
    input
        .trim()
        .lines()
        .map(|l| {
            let first = l.chars().filter_map(|c| c.to_digit(10)).next().unwrap();
            let last = l
                .chars()
                .rev()
                .filter_map(|c| c.to_digit(10))
                .next()
                .unwrap();
            first * 10 + last
        })
        .sum::<u32>() as usize
}

#[aoc(day1, part2)]
pub fn part_2(input: &String) -> usize {
    let number_words = vec![
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let numbers = number_words
        .iter()
        .enumerate()
        .map(|(i, w)| (w.to_string(), i))
        .collect::<HashMap<String, usize>>();
    let numbers_rev: HashMap<String, usize> = numbers
        .iter()
        .map(|(w, i)| (w.chars().rev().collect(), *i))
        .collect();
    let is_digit_or_number_word = |s: &[u8], i: usize| -> Option<usize> {
        numbers
            .iter()
            .find_map(|(w, n)| {
                if (s[i..]).starts_with(w.as_bytes()) {
                    Some(*n)
                } else {
                    None
                }
            })
            .or_else(|| (s[i] as char).to_digit(10).map(|n| n as usize))
    };
    let is_digit_or_number_rev_word = |s: &[u8], i: usize| -> Option<usize> {
        numbers_rev
            .iter()
            .find_map(|(w, n)| {
                if (s[i..]).starts_with(w.as_bytes()) {
                    Some(*n)
                } else {
                    None
                }
            })
            .or_else(|| (s[i] as char).to_digit(10).map(|n| n as usize))
    };
    input
        .trim()
        .lines()
        .map(|l| {
            let first = l
                .chars()
                .enumerate()
                .find_map(|(i, _c)| is_digit_or_number_word(l.as_bytes(), i))
                .unwrap();
            let last = l
                .chars()
                .rev()
                .enumerate()
                .find_map(|(i, _c)| {
                    is_digit_or_number_rev_word(l.chars().rev().collect::<String>().as_bytes(), i)
                })
                .unwrap();
            first * 10 + last
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT_1: &str = include_str!("../test_data/day_01_1.txt");
    const INPUT_2: &str = include_str!("../test_data/day_01_2.txt");

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&get_input(INPUT_1)), 142);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&get_input(INPUT_2)), 281);
    }
}
