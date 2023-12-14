#![feature(iter_intersperse)]
#![feature(let_chains)]

#[macro_use]
extern crate aoc_runner_derive;
#[macro_use]
extern crate ndarray;

mod grid;
mod search;

mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;
mod day_08;
mod day_10;
mod day_13;

aoc_lib! { year = 2023 }
