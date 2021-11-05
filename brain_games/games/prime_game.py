import prompt
import math
from random import randint
from brain_games.games.check_answer import check_answer


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num = randint(1, 150)
        question = str(num)
        if is_prime(num):
            right_answr = 'yes'
        else:
            right_answr = 'no'
        if check_answer(question, right_answr):
            right_answ_cnt += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def is_prime(num):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        return True
