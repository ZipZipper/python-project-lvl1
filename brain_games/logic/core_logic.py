import prompt


def greetings():
    print('Welcome to the Brain Games!')


def prompt_and_get_user_name():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def play_rounds(logic, name):
    count_win = 0

    ask, resp = logic()

    while True:
        print('Question: {}'.format(ask))
        resp_user = prompt.string('Your answer: ')

        if resp_user == resp:
            print("Correct!")
            count_win += 1

            if count_win == 3:
                print('Congratulations, {}!'.format(name))
                break
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(resp_user, resp))
            print('Let\'s try again, {}!'.format(name))
            break


def start_game(TASK, logic):
    greetings()
    user_name = prompt_and_get_user_name()
    print(TASK)
    play_rounds(logic, user_name)
