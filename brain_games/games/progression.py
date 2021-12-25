from random import randrange


RULE_TEXT = 'What number is missing in the progression?'
ANSWER_PATTERN = '\\d+'


def generate_round():
    step = randrange(1, 15, 1)
    element = randrange(1, 20, 1)
    progression = []
    for _ in range(10):
        progression.append(element)
        element += step
    element_to_search = randrange(len(progression))
    result = progression[element_to_search]
    progression[element_to_search] = '..'
    question = 'Question: {}'.format(' '.join(map(str, progression)))
    return result, question
