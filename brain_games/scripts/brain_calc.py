#!/usr/bin/env python3

from brain_games.games import calc_game
from brain_games.games import start
from brain_games.games import greeting


def main():
    greeting.greet('What is the result of the expression?')
    start.play(calc_game.play_calc)


if __name__ == "__main__":
    main()