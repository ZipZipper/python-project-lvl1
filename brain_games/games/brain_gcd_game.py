import random
from brain_games.core_logic import start_game

TASK = 'Find the greatest common divisor of given numbers.'


def play_games():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return "{0} {1}".format(num1, num2), int(find_minimal_divisor(num1, num2))


def find_minimal_divisor(num1, num2):
    for n in range(min(num1, num2), 1, -1):
        if num1 % n == 0 and num2 % n == 0:
            return n
    else:
        return 1


def brain_gcd_game():
    start_game(TASK, play_games)
