#!/usr/bin/env python3

from brain_games.result_check import result_check
from random import randrange
import prompt


def play_progression(user_name):
    prog_step = prog_el = randrange(1, 15, 1)
    prog_list = []
    for idx in range(10):
        prog_list.append(prog_el)
        prog_el += prog_step
    el_search = randrange(len(prog_list))
    res = prog_list[el_search]
    prog_list[el_search] = '..'
    print('Question: {}'.format(prog_list))
    ans = prompt.integer('Your answer: ')
    return result_check(user_name, ans, res)
