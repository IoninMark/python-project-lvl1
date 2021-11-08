from random import randint, choice
from brain_games.games.check_answer import check_answer, greet


def calc_game():
    rules = 'What is the result of the expression?'
    name = greet(rules)
    right_answ_cnt = 0
    while right_answ_cnt < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operations_list = ['+', '-', '*']
        question = str(num1) + ' ' + choice(operations_list) + ' ' + str(num2)
        right_answr = eval(question)
        if check_answer(question, right_answr, name, right_answ_cnt):
            right_answ_cnt += 1
        else:
            return
