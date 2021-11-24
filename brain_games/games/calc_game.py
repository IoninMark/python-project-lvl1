from random import randint, choice


GAME_INFO = 'What is the result of the expression?'


def make_question_and_answer():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    operation = choice(['+', '-', '*'])
    question = str(num1) + ' ' + operation + ' ' + str(num2)
    right_answer = calculate_expression(num1, num2, operation)
    return (question, right_answer)


def calculate_expression(num1, num2, operation):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        raise ValueError(f'Unknown operation! Operation: {operation}')
    return result
