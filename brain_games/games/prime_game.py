#!/usr/bin/env python3

import random
import prompt
import math
from brain_games.result_check import result_check


def prime_check(number):
    if number == 2:
        return 'yes'
    divider = int(math.sqrt(number))
    while number % divider != 0:
        divider -= 1
    if divider == 1:
        return 'yes'
    else:
        return 'no'


def play_prime(user_name):
    number = random.randint(2, 300)
    print('Question: {}'.format(number))
    res = prime_check(number)
    ans = prompt.string('Your answer: ')
    if ans in ['yes', 'no']:
        return result_check(user_name, ans, res)
    else:
        print('Wrong answer!')
        return False
