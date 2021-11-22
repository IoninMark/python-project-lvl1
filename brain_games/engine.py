from brain_games.cli import ask, welcome_user


ROUNDS_NUMBER = 3


def play_game(game):
    name = welcome_user()
    print(game.GAME_INFO)
    for i in range(ROUNDS_NUMBER):
        (question, right_ans) = game.make_question_and_answer()
        ans = ask(question)
        if str(ans) == str(right_ans):
            print('Correct!')
        else:
            print(
                f"'{ans}' is wrong answer ;(. "
                f"Correct answer was '{right_ans}'."
                f"\nLet's try again, {name}!"
            )
            return
    print(f'Congratulations, {name}!')
