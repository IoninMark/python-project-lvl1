import prompt


def greet(rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n' + rules)
    return name


def check_answer(question, right_answer, name):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    s1 = f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'."
    s2 = f"Let's try again, {name}!"
    if str(answer) == str(right_answer):
        print('Correct!')
        return True
    else:
        print(s1 + '\n' + s2)
        return False
