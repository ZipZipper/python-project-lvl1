import random
from .core_logic import start_game

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def games():
    num1 = random.randint(1, 100)
    resp = 'yes' if is_prime(num1) else 'no'
    return num1, resp


def is_prime(num_):
    return all(num_ % x for x in range(2, int(num_**.5 + 1)))


def brain_prime_game():
    start_game(TASK, games)
