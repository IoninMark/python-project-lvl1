from random import randint, choice


def calc_game():
    rules = 'What is the result of the expression?'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operations_list = ['+', '-', '*']
    question = str(num1) + ' ' + choice(operations_list) + ' ' + str(num2)
    right_answer = eval(question)
    return (rules, question, right_answer)
