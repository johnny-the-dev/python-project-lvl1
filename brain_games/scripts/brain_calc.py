#!/usr/bin/env python3

from brain_games import start, greeting
from brain_games.games.calc_game import play_calc


def main():
    greeting.greet('What is the result of the expression?')
    start.play(play_calc)


if __name__ == "__main__":
    main()
