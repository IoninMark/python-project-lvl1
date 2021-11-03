import prompt
from random import randint
from brain_games.games.check_answer import check_answer


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            if check_answer(num, 'yes'):
                right_answ_cnt += 1
            else:
                print(f"Let's try again, {name}!")
                return
        else:
            if check_answer(num, 'no'):
                right_answ_cnt += 1
            else:
                print(f"Let's try again, {name}!")
                return
    print(f'Congratulations, {name}!')
