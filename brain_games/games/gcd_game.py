from random import randint


GAME_INFO = 'Find the greatest common divisor of given numbers.'


def make_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = str(num1) + ' ' + str(num2)
    right_answer = find_gcd(num1, num2)
    return (question, right_answer)


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
