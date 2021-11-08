from random import randint
from brain_games.games.check_answer import check_answer, greet


def progression_game():
    rules = 'What number is missing in the progression?'
    name = greet(rules)
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        first_num = randint(1, 50)
        progr_diff = randint(1, 30)
        progr_len = randint(5, 9)
        index = randint(0, progr_len)
        question = create_progression(first_num, progr_len, progr_diff, index)
        right_answr = first_num + index * progr_diff
        if check_answer(question, right_answr, name):
            right_answ_cnt += 1
        else:
            return
    print(f'Congratulations, {name}!')


def create_progression(first_elem, length, diff, index):
    progression = ''
    for i in range(length + 1):
        if i == index:
            progression = progression + '.. '
        else:
            progression = progression + str(first_elem + i * diff) + ' '
    return progression
