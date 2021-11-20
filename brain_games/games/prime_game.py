import math
from random import randint


GAME_INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    num = randint(1, 150)
    question = str(num)
    right_answer = 'yes' if is_prime(num) else 'no'
    return (question, right_answer)


def is_prime(num):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        return True
