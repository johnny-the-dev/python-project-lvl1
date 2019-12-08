import prompt

def get_user_name():
    user_name = prompt.string('May I have your name? ')
    return user_name

def run():
    user_name = get_user_name()
    print('Hello, {}!'.format(user_name))
    return user_name