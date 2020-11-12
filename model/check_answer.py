def check_answer(chars):
    if chars not in ('y', 'n'):
        print('You did something wrong. Bye-bye.')
        return False
    if chars == 'n':
        print('Get it! Bye!')
        return False
    if chars == 'y':
        return True