import prompt
import re


ROUND_NUMBER = 3


def get_user_name(rule_text):
    print('Welcome to the Brain Games!\n{}\n'.format(rule_text))
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(user_name))
    return user_name


def play(game):
    user_name = get_user_name(game.RULE_TEXT)
    isFinalSucess = True
    for _ in range(ROUND_NUMBER):
        res, question = game.generate_round()
        print(question)
        ans = prompt.string('Your answer: ').lower()
        if re.match(game.ANSWER_PATTERN, ans):
            if str(res) == ans:
                print('Correct!')
            else:
                print("{} is wrong answer ;(. Correct answer was {}.".format(ans, res))
                print("Let's try again, {}!".format(user_name))
                isFinalSucess = False
                break
        else:
            print('Wrong answer!')
            isFinalSucess = False
            break
    if isFinalSucess:
        print('Congratulations, {}!'.format(user_name))
