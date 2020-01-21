#!/usr/bin/env python3

from brain_games.games.greeting import greet
from brain_games.games.even_game import play_even
from brain_games.games.start import play


def main():
    greet('Answer "yes" if number even otherwise answer "no".')
    play(play_even)


if __name__ == "__main__":
    main()
