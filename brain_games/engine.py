import prompt
import re


NUMBER_OF_ROUNDS = 3


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


def check_answer(user_answer, calc_result):
    if str(calc_result) != user_answer:
        print(
            f'{user_answer} is wrong answer ;(. '\
            f'Correct answer was {calc_result}.'
            )
        return False

    print('Correct!')
    return True


def play(game):
    """Launches a game, checks user`s answer and prints result.

    Arguments:
        game {module} -- the game module
    """

    user_name = get_user_name(game.RULE_TEXT)  

    for _ in range(NUMBER_OF_ROUNDS):
        result, question = game.generate_round()
        print(question)
        user_answer = prompt.string('Your answer: ').lower()
        
        while re.fullmatch(game.ANSWER_PATTERN, user_answer) == None:
            print('Answer is not correct!')
            user_answer = prompt.string('Your answer: ').lower()
        
        is_success = check_answer(user_answer, result)
        if not is_success:
            print(f'Let`s try again, {user_name}!')
            break
    
    else:
        print(f'Congratulations, {user_name}!')
