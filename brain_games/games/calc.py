import operator
import random


RULE_TEXT = 'What is the result of the expression?'
ANSWER_PATTERN = '[-+]?\\d+'
OPERATORS = ((operator.add, '+'),
             (operator.sub, '-'),
             (operator.mul, '*'))


def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operation = random.choice(OPERATORS)
    result = operation[0](number1, number2)
    question = 'Question: {} {} {}'.format(number1, operation[1], number2)
    return result, question
