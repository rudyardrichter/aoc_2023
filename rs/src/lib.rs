#![feature(iter_intersperse)]
#![feature(let_chains)]

#[macro_use]
extern crate aoc_runner_derive;

mod binary_search;
mod grid;

mod day_01;
mod day_02;
mod day_06;

aoc_lib! { year = 2023 }
