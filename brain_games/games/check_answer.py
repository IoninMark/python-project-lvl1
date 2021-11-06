import prompt


def check_answer(question, right_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    s = f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'."
    if str(answer) == str(right_answer):
        print('Correct!')
        return True
    else:
        print(s)
        return False
