import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_games():
    num1 = random.randint(1, 100)
    return num1, bool_to_answer(is_even(num1))


def is_even(num_):
    return num_ % 2 == 0


def bool_to_answer(value):
    return "yes" if value else "no"
