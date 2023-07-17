from brain_games.core_logic import start_game
import random
import operator

TASK = 'What is the result of the expression?'


def play_games():
    random_sign = random.choice(["+", "-", "*"])
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result_print = "{0} {1} {2}".format(num1, random_sign, num2)

    return result_print, calculate_expression_result(num1, random_sign, num2)


def calculate_expression_result(num1, sign, num2):
    if sign == "+":
        return str(operator.add(num1, num2))
    elif sign == "-":
        return str(operator.sub(num1, num2))
    elif sign == "*":
        return str(operator.mul(num1, num2))


def brain_calc_game():
    start_game(TASK, play_games)
