from random import randint


GAME_INFO = 'What number is missing in the progression?'


def make_question():
    first_num = randint(1, 50)
    progr_diff = randint(1, 20)
    progr_len = randint(5, 9)
    index = randint(0, progr_len - 1)
    question = create_progression(first_num, progr_len, progr_diff, index)
    right_answer = first_num + index * progr_diff
    return (question, right_answer)


def create_progression(first_elem, length, diff, index):
    progression = []
    for i in range(length):
        progression.append(str(first_elem + i * diff))
    progression[index] = '..'
    return ' '.join(progression)
