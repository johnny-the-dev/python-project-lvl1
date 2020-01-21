#!/usr/bin/env python3

from brain_games.greeting import greet
from brain_games.games import even_game
from brain_games.start import play


def main():
    greet('Answer "yes" if number even otherwise answer "no".')
    play(even_game.play_even)


if __name__ == "__main__":
    main()
