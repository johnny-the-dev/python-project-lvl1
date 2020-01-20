def result_check(user_name, ans, res):
    if ans == res:
        print('Correct!')
        return True
    else:
        print("{} is wrong answer ;(. Correct answer was {}.".format(ans, res))
        print("Let's try again, {}!".format(user_name))
        return False
