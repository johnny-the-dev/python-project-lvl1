import prompt
import re


ROUND_NUMBER = 3


def get_user_name(rule_text):
    print(f'Welcome to the Brain Games!\n{rule_text}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')
    return user_name


def play(game):
    user_name = get_user_name(game.RULE_TEXT)
    isFinalSucess = True
    for _ in range(ROUND_NUMBER):
        res, question = game.generate_round()
        print(question)
        ans = prompt.string('Your answer: ').lower()
        if not re.match(game.ANSWER_PATTERN, ans):
            print('Wrong answer!')
            isFinalSucess = False
            break
        if str(res) != ans:
            print(f'{ans} is wrong answer ;(. Correct answer was {res}.')
            print(f'Let`s try again, {user_name}!')
            isFinalSucess = False
            break
        print('Correct!')

    if isFinalSucess:
        print(f'Congratulations, {user_name}!')
