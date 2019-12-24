#!/usr/bin/env python3

import random
import prompt


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
    if ans == res:
        print('Correct!')
        return True
    else:
        print("{} is wrong answer ;(. Correct answer was {}.".format(ans, res))
        print("Let's try again, {}!".format(user_name))
        return False
