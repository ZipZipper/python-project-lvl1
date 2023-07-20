import random
import operator

TASK = 'What is the result of the expression?'


def play_games():
    val1 = random.randint(1, 100)
    val2 = random.randint(1, 100)
    operations = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    )
    operation_name, operation_method = random.choice(operations)

    question_msg = f'{val1} {operation_name} {val2}'
    result = operation_method(val1, val2)
    return question_msg, str(result)
