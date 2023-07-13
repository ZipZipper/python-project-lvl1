import random
from .core_logic import start_game

task = 'Find the greatest common divisor of given numbers.'


def logic():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return "{0} {1}".format(num1, num2), _is_minimal_div(num1, num2)


def _is_minimal_div(num1, num2):
    for n in range(min(num1, num2), 1, -1):
        if num1 % n == 0 and num2 % n == 0:
            return str(n)
    else:
        return str(1)


def brain_gcd_game():
    start_game(task, logic)
