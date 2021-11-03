import prompt


def check_answer(question, right_answr):
    print('Question: ', question)
    answer = prompt.string('Your answer: ')
    if str(answer) == str(right_answr):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answr}'.")
        return False
