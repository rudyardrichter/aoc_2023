{-# LANGUAGE OverloadedStrings #-}

module Main (main) where

import Prelude hiding (readFile)
import Control.Arrow
import Control.Monad
import qualified Data.Text as T
import Data.Text.IO (readFile)
import System.Environment (getArgs)
import Text.Printf (printf)

import Day01 (day01)

getInput :: Int -> IO T.Text
getInput n = readFile $ "inputs/day_" ++ printf "%02d" n ++ ".txt"

day :: Int -> T.Text -> IO ()
day 1 = day01
day _ = \_ -> putStrLn "Not implemented"

main :: IO ()
main = fmap (read . head) getArgs >>= \n -> getInput n >>= day n
