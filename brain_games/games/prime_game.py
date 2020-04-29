import random
import math


RULE_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_PATTERN = 'yes|no'


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


def generate_round():
    number = random.randint(2, 300)
    res = prime_check(number)
    question = 'Question: {}'.format(number)
    return res, question
