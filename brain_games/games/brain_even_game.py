import random
from brain_games.core_logic import start_game

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def games():
    num1 = random.randint(1, 100)
    return num1, is_even(num1)


def is_even(num_):
    if num_ % 2 == 0:
        return True
    else:
        return False


def brain_even_game():
    start_game(TASK, games)
