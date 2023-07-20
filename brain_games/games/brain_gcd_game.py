import random

TASK = 'Find the greatest common divisor of given numbers.'


def find_minimal_divisor(num1, num2):
     for divider in range(min(num1, num2), 0, -1):
        if num1 % divider == 0 and num2 % divider == 0:
            return divider


def play_games():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    question_msg = f'{num1} {num2}'
    answer = find_minimal_divisor(num1, num2)
    return question_msg, str(answer)
