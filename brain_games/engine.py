import importlib
from brain_games.cli import ask, welcome_user


def play_game(game):
    new_game = importlib.import_module(game)
    tries_num = 3
    name = welcome_user()
    print(new_game.GAME_INFO)
    for i in range(tries_num):
        (question, right_ans) = new_game.make_question()
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
