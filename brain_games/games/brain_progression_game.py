import random
from brain_games.core_logic import start_game

TASK = 'What number is missing in the progression?'


def play_games():
    step = random.randint(1, 10)
    index = random.randint(0, 9)
    progression = [str(i) for i in range(4 + step, 5 + step * 10, step)]
    print("index ===", index, end="\n")
    print("progression ===", progression)
    resp = progression[index]
    progression[index] = '..'

    return " ".join(progression), str(resp)


def brain_progression_game():
    start_game(TASK, play_games)
