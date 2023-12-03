{-# LANGUAGE OverloadedStrings #-}

module Day01 where

import Control.Arrow ((&&&), (<<<), arr, second)
import Control.Monad
import Data.List (unsnoc)
import Data.Maybe (fromMaybe)
import qualified Data.Text as T
import Text.Megaparsec hiding (State)
import Text.Megaparsec.Char as C
import qualified Text.Megaparsec.Char.Lexer as L

type Parser = Parsec String T.Text

numberWord :: Parser Int
numberWord = string "one" *> pure 1
         <|> string "two" *> pure 2
         <|> string "three" *> pure 3
         <|> string "four" *> pure 4
         <|> string "five" *> pure 5
         <|> string "six" *> pure 6
         <|> string "seven" *> pure 7
         <|> string "eight" *> pure 8
         <|> string "nine" *> pure 9

numberWordRev :: Parser Int
numberWordRev = string "eno" *> pure 1
            <|> string "owt" *> pure 2
            <|> string "eerht" *> pure 3
            <|> string "ruof" *> pure 4
            <|> string "evif" *> pure 5
            <|> string "xis" *> pure 6
            <|> string "neves" *> pure 7
            <|> string "thgie" *> pure 8
            <|> string "enin" *> pure 9

digit :: Parser Int
digit = read . T.unpack . T.singleton <$> C.numberChar

number :: Parser Int
number = numberWord <|> digit

numberRev :: Parser Int
numberRev = numberWordRev <|> digit

fill :: Parser Int -> Parser ()
fill p = try $ manyTill anySingle (lookAhead p) *> pure ()

parseLine :: Parser Int -> Parser Int
parseLine p = fill p *> p

solve :: Parser Int -> Parser Int -> T.Text -> Either (ParseErrorBundle T.Text String) Int
solve p pRev = fmap sum
        . sequence
        . map (\l -> (+) . (10 *) <$> f l <*> g (T.reverse l))
        . T.lines
    where
    f = parse (parseLine p) ""
    g = parse (parseLine pRev) ""

day01 :: T.Text -> IO ()
day01 = either (error . show) (mapM_ putStrLn . map show)
    <<< ((zipWithM (uncurry solve)) [(digit, digit), (number, numberRev)]) . repeat
