#!/usr/bin/env python3

from brain_games.games.greeting import greet
from brain_games.games.start import play
from brain_games.games.calc_game import play_calc


def main():
    greet('What is the result of the expression?')
    play(play_calc)


if __name__ == "__main__":
    main()
