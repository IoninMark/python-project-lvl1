import prompt
from random import randint
from brain_games.games.check_answer import check_answer


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        question = str(num1) + ' ' + str(num2)
        right_answr = find_gcd(num1, num2)
        if check_answer(question, right_answr):
            right_answ_cnt += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def find_gcd(num1, num2):
    if num1 > num2:
        dividend = num1
        divider = num2
    else:
        dividend = num2
        divider = num1
    modulo = divider
    while modulo != 0:
        divider = modulo
        modulo = dividend % divider
        dividend = divider
    return divider
