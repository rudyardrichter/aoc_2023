#![feature(iter_intersperse)]
#![feature(let_chains)]

#[macro_use]
extern crate aoc_runner_derive;

mod grid;
mod search;

mod day_01;
mod day_02;
mod day_03;
mod day_06;
mod day_08;

aoc_lib! { year = 2023 }
