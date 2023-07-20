import random

TASK = 'What number is missing in the progression?'


def play_games():
    step = random.randint(1, 10)
    index = random.randint(0, 9)
    progression = [str(i) for i in range(4 + step, 5 + step * 10, step)]
    resp = progression[index]
    progression[index] = '..'

    return " ".join(progression), str(resp)
