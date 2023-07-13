import random
from .core_logic import start_game

TASK = 'What number is missing in the progression?'


def games():
    step = random.randint(1, 10)
    index = random.randint(0, 9)
    progression = [str(i) for i in range(4 + step, 5 + step * 10, step)]
    hidden_value = progression[index]
    progression[index] = '..'

    return " ".join(progression), str(hidden_value)


def brain_progression_game():
    start_game(TASK, games)
