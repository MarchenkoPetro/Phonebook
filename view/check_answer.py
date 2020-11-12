def check_answer(answer):
    if answer not in ('y', 'n'):
        print('You did something wrong. Bye-bye.')
        return False
    if answer == 'n':
        print('Get it! Bye!')
        return False
    return True
