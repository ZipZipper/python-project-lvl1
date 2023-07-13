from brain_games.core_logic import start_game
import random

TASK = 'What is the result of the expression?'


def games():
    random_sign = ["+", "-", "*"][random.randint(0, 2)]
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result_print = "{0} {1} {2}".format(num1, random_sign, num2)

    return result_print, is_correct_result_exp(num1, random_sign, num2)


def is_correct_result_exp(num1, sing, num2):
    if sing == "+":
        return str(num1 + num2)
    elif sing == "-":
        return str(num1 - num2)
    elif sing == "*":
        return str(num1 * num2)


def brain_calc_game():
    start_game(TASK, games)
