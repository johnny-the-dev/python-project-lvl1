#!/usr/bin/env python3

import random
import prompt
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    brain_even()


if __name__ == "__main__":
    main()


def brain_even():
    user_name = cli.get_user_name()
    print('Hello, {}'.format(user_name))
    ANSWERS = {
        'yes': 0,
        'no': 1
    }
    for idx in range(3):
        isright = False
        number = random.randint(1, 100)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        even_check = number % 2

        if answer in ANSWERS.keys():
            if even_check == ANSWERS[answer]:
                print('Correct!')
                isright = True
            elif answer == 'yes':
                print("yes is wrong answer ;(. Correct answer was no.")
                print("Let's try again,", user_name)
            else:
                print("no is wrong answer ;(. Correct answer was yes.")
                print("Let's try again,", user_name)
        else:
            print('Wrong answer!')

        if isright:
            print('Congratulations, {}!'.format(user_name))
        else:
            return None
