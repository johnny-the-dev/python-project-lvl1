#!/usr/bin/env python3

import random
import prompt
from brain_games.games.result_check import result_check


def gcd(num1, num2):
    a = num1
    b = num2
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def play_gcd(user_name):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Question: {} {}'.format(number1, number2))
    ans = prompt.integer('Your answer: ')
    res = gcd(number1, number2)
    return result_check(user_name, ans, res)
