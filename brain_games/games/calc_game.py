#!/usr/bin/env python3

import random
import prompt


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
    if ans == res:
        print('Correct!')
        return True
    else:
        print("{} is wrong answer ;(. Correct answer was {}.".format(res, ans))
        print("Let's try again, {}!".format(user_name))
        return False
