import prompt


def _hello():
    print('Welcome to the Brain Games!')


def _get_name_user():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def _rounds_game(logic, name):
    count_win = 0

    while True:
        tupl_ask_and_resp = logic()
        ask, resp = tupl_ask_and_resp[0], tupl_ask_and_resp[1]
        print('Question: {}'.format(ask))
        resp_user = prompt.string('Your answer: ')

        if resp_user == resp:
            print("Correct!")
            count_win += 1

            if count_win == 3:
                print('Congratulations, {}!'.format(name))
                break
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(
                resp_user, resp))
            print('Let\'s try again, {}!'.format(name))
            break


def start_game(task, logic):
    _hello()
    user_name = _get_name_user()
    print(task)
    _rounds_game(logic, user_name)