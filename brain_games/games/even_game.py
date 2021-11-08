from random import randint
from brain_games.games.check_answer import check_answer, greet


def even_game():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = greet(rules)
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            if check_answer(num, 'yes', name):
                right_answ_cnt += 1
            else:
                return
        else:
            if check_answer(num, 'no', name):
                right_answ_cnt += 1
            else:
                return
    print(f'Congratulations, {name}!')
