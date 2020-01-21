#!/usr/bin/env python3

import random
import prompt
from brain_games.result_check import result_check


def even_check(number):
    return 'yes' if number % 2 == 0 else 'no'


def play_even(user_name):
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    ans = prompt.string('Your answer: ')
    res = even_check(number)
    if ans in ['yes', 'no']:
        return result_check(user_name, ans, res)
    else:
        print('Wrong answer!')
        return False
