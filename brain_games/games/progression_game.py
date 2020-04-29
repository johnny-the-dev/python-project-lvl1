from random import randrange


RULE_TEXT = 'What number is missing in the progression?'
ANSWER_PATTERN = '\\d+'


def generate_round():
    prog_step = prog_el = randrange(1, 15, 1)
    prog_list = []
    for idx in range(10):
        prog_list.append(prog_el)
        prog_el += prog_step
    el_search = randrange(len(prog_list))
    res = prog_list[el_search]
    prog_list[el_search] = '..'
    question = 'Question: {}'.format(prog_list)
    return res, question
