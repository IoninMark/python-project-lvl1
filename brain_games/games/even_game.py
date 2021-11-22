from random import randint


GAME_INFO = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_answer():
    num = randint(1, 100)
    right_answer = 'yes' if num % 2 == 0 else 'no'
    return (num, right_answer)
