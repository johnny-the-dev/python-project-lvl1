#!/usr/bin/env python3

from brain_games.greeting import greet
from brain_games.start import play
from brain_games.games.progression_game import play_progression


def main():
    greet('What number is missing in the progression?')
    play(play_progression)


if __name__ == "__main__":
    main()
