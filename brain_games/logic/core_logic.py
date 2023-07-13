import prompt


def greeting():
    print('Welcome to the Brain Games!')


def prompt_and_get_user_name():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def play_rounds(logic, name):
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
    greeting()
    user_name = prompt_and_get_user_name()
    print(task)
    play_rounds(logic, user_name)
