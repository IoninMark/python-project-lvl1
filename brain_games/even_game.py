import prompt
from random import randint


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answ_cnt = 0
    while correct_answ_cnt < 3:
        num = randint(1, 100)
        print('Question: ', num)
        answer = prompt.string('Your answer: ')
        if num % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                correct_answ_cnt += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was 'yes'.".format(answer))
                print("Let's try again, {}!".format(name))
                return
        else:
            if answer == 'no':
                print('Correct!')
                correct_answ_cnt += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(answer))
                print("Let's try again, {}!".format(name))
                return
    print('Congratulations, {}!'.format(name))