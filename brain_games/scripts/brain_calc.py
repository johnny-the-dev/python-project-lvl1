#!/usr/bin/env python3

from brain_games import start
from brain_games.games import calc_game


def main():
    start.play(calc_game)


if __name__ == "__main__":
    main()
