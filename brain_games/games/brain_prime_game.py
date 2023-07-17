import random
from brain_games.core_logic import start_game

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_games():
    num1 = random.randint(1, 100)
    resp = 'yes' if is_prime(num1) else 'no'
    return num1, resp


def is_prime(num_):
    if num_ < 2:
        return False
    for i in range(2, int(num_**0.5) + 1):
        if num_ % i == 0:
            return False
    return True


def brain_prime_game():
    start_game(TASK, play_games)
