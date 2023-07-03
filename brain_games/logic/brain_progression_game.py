import random
from .core_logic import start_game

task = 'What number is missing in the progression?'


def logic():
    step = random.randint(1, 10)
    invsible_value = random.randint(0, 9)
    progression = [str(i) for i in range(4 + step, 5 + step * 10, step)]
    resp = progression[invsible_value]
    progression[invsible_value] = '..'

    return " ".join(progression), str(resp)


def brain_progression_game():
    start_game(task, logic)
