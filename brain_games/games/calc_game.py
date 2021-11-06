import prompt
from random import randint, choice
from brain_games.games.check_answer import check_answer


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operations_list = ['+', '-', '*']
        question = str(num1) + ' ' + choice(operations_list) + ' ' + str(num2)
        right_answr = eval(question)
        if check_answer(question, right_answr):
            right_answ_cnt += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
