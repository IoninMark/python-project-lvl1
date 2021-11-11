import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    right_ans_cnt = 0
    while right_ans_cnt < 3:
        (rules, question, right_ans) = game()
        if right_ans_cnt == 0:
            print(rules)
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        end1 = f"'{ans}' is wrong answer ;(. Correct answer was '{right_ans}'."
        end2 = f"\nLet's try again, {name}!"
        if str(ans) == str(right_ans):
            print('Correct!')
            right_ans_cnt += 1
        else:
            print(end1 + end2)
            return
    print(f'Congratulations, {name}!')
