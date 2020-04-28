import random


RULE_TEXT = 'Answer "yes" if number even otherwise answer "no".'
ANSWER_PATTERN = 'yes|no'


def even_check(number):
    return 'yes' if number % 2 == 0 else 'no'


def generate_round():
    number = random.randint(1, 100)
    res = even_check(number)
    return res, 'Question: {}'.format(number)
