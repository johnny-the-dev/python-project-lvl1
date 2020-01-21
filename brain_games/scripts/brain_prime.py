#!/usr/bin/env python3

from brain_games.games.greeting import greet
from brain_games.games.start import play
from brain_games.games.prime_game import play_prime


def main():
    greet('Answer "yes" if given number is prime. Otherwise answer "no".')
    play(play_prime)


if __name__ == "__main__":
    main()
