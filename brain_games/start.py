import prompt
import re


ROUND_NUMBER = 3


def get_user_name(rule_text):
    """Greets user, prints rules and finds out user`s name.

    Arguments:
        rule_text {string} -- rule of the game.

    Returns:
        string -- user`s name.
    """

    print(f'Welcome to the Brain Games!\n{rule_text}\n')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')
    return user_name


def check_answer(user_ans, calc_res, ans_pattern):
    """Games has different types of answers. This function checks user`s
    answer for matching to the pattern of the game`s answer and then compares
    user`s answer with the correct result.

    Arguments:
        user_ans {string} -- user`s answer
        calc_res {integer or string} -- calculated correct result, can be
            integer or [yes|no]
        ans_pattern {string} -- pattern of the game`s answer

    Returns:
        boolean -- result of checking
    """

    if not re.match(ans_pattern, user_ans):
        print('Wrong answer!')
        return False

    if str(calc_res) != user_ans:
        print(f'{user_ans} is wrong answer ;(. Correct answer was {calc_res}.')
        return False

    print('Correct!')
    return True


def play(game):
    """Launches a game, checks user`s answer and prints result.

    Arguments:
        game {module} -- the game module
    """

    user_name = get_user_name(game.RULE_TEXT)
    isSuccess = True

    for _ in range(ROUND_NUMBER):
        res, question = game.generate_round()
        print(question)
        ans = prompt.string('Your answer: ').lower()
        ans_pattern = game.ANSWER_PATTERN
        isSuccess = check_answer(ans, res, ans_pattern)
        if not isSuccess:
            print(f'Let`s try again, {user_name}!')
            break

    if isSuccess:
        print(f'Congratulations, {user_name}!')
