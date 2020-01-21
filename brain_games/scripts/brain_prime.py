#!/usr/bin/env python3

from brain_games.games import prime_game
from brain_games import start
from brain_games.greeting import greet


def main():
    greet('Answer "yes" if given number is prime. Otherwise answer "no".')
    start.play(prime_game.play_prime)


if __name__ == "__main__":
    main()
