#!/usr/bin/env python3

import prompt


def play(game):
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print()

    for idx in range(3):
        if not game(user_name):
            return None

    print('Congratulations, {}!'.format(user_name))
