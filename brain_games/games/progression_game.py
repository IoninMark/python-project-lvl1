from random import randint


def progression_game():
    rules = 'What number is missing in the progression?'
    first_num = randint(1, 50)
    progr_diff = randint(1, 30)
    progr_len = randint(5, 9)
    index = randint(0, progr_len)
    question = create_progression(first_num, progr_len, progr_diff, index)
    right_answer = first_num + index * progr_diff
    return (rules, question, right_answer)


def create_progression(first_elem, length, diff, index):
    progression = ''
    for i in range(length + 1):
        if i == index:
            progression = progression + '.. '
        else:
            progression = progression + str(first_elem + i * diff) + ' '
    return progression
