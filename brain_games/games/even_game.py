from random import randint


def even_game():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = randint(1, 100)
    right_answer = 'yes' if num % 2 == 0 else 'no'
    return (rules, num, right_answer)
