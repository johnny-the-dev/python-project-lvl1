#!/usr/bin/env python3

from brain_games.games import gcd_game, start, greeting


def main():
    greeting.greet('Find the greatest common divisor of given numbers.')
    start.play(gcd_game.play_gcd)


if __name__ == "__main__":
    main()
