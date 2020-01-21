#!/usr/bin/env python3

from brain_games.games.gcd_game import play_gcd
from brain_games.games.greeting import greet
from brain_games.games.start import play


def main():
    greet('Find the greatest common divisor of given numbers.')
    play(play_gcd)


if __name__ == "__main__":
    main()
