import random


RULE_TEXT = 'What is the result of the expression?'
ANSWER_PATTERN = '[-+]?\\d+'


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-'])
    if operation == '+':
        res = number1 + number2
    else:
        res = number1 - number2
    question = 'Question: {} {} {}'.format(number1, operation, number2)
    return res, question
