import prompt

COUNT_ROUNDS = 3


def run_greeting():
    print('Welcome to the Brain Games!')


def prompt_and_get_user_name():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def play_rounds(generate_question_and_answer, name):
    count_win = 0

    while True:
        question, correct_answer = generate_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print("Correct!")
            count_win += 1

            if count_win == COUNT_ROUNDS:
                print('Congratulations, {}!'.format(name))
                break
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(
                user_answer, correct_answer))
            print('Let\'s try again, {}!'.format(name))
            break


def start_game(task, logic):
    run_greeting()
    user_name = prompt_and_get_user_name()
    print(task)
    play_rounds(logic, user_name)
