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

def iseven(num):
    return num % 2 == 0

def brain_even():
    user_name = cli.run()
    for idx in range(3):
        number = random.randint(1, 100)
        isright = False
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        
        if (iseven(number) and answer == 'yes') or (not iseven(number) and answer == 'no'):
            print('Correct!')
            isright = True
        elif iseven(number) and answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again,", user_name)
        elif not iseven(number) and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again,", user_name)
        else:
            print('Wrong answer!')

        if isright:
            print('Congratulations, {}!'.format(user_name))
        else:
            return None
