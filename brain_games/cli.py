import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def ask(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer
