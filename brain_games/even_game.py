#!/usr/bin/env python3

import random
import prompt


def play_even(user_name):
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    isright = False
    even_check = number % 2
    ANSWERS = {
        'yes': 0,
        'no': 1
    }
    if answer in ANSWERS.keys():
        if even_check == ANSWERS[answer]:
            print('Correct!')
            isright = True
        elif answer == 'yes':
            print("yes is wrong answer ;(. Correct answer was no.")
            print("Let's try again, {}!".format(user_name))
        else:
            print("no is wrong answer ;(. Correct answer was yes.")
            print("Let's try again, {}!".format(user_name))
    else:
        print('Wrong answer!')
    return isright


def brain_even():
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print()

    for idx in range(3):
        if not play_even(user_name):
            return None

    print('Congratulations, {}!'.format(user_name))
