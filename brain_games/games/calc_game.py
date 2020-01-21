#!/usr/bin/env python3

import random
import prompt
from brain_games.result_check import result_check


def play_calc(user_name):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(('+', '-'))
    print('Question: {} {} {}'.format(number1, operation, number2))
    ans = prompt.integer('Your answer: ')
    if operation == "+":
        res = number1 + number2
    else:
        res = number1 - number2
    return result_check(user_name, ans, res)
