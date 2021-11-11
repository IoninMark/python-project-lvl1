import math
from random import randint


def prime_game():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num = randint(1, 150)
    question = str(num)
    right_answer = 'yes' if is_prime(num) else 'no'
    return (rules, question, right_answer)


def is_prime(num):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        return True
