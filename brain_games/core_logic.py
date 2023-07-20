import prompt
import sys

COUNT_ROUNDS = 3


def start_game(game_task, get_game_question_answer):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print(
        f"Hello, {user_name}!\n"
        f"{game_task}"
    )

    cycles_count = 3
    # num_cycles = 3
    for cycle in range(cycles_count):
        question, correct_answer = get_game_question_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            sys.exit()

    print(f'Congratulations, {user_name}!')
