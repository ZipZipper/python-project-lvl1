import prompt


def greetings():
    print('Welcome to the Brain Games!')


def prompt_and_get_user_name():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    return name


def play_roundsss(logic, name):
    count_win = 0
    count_loss = 0

    while True:
        ask, resp = logic()
        print('Question: {}'.format(ask))
        resp_user = prompt.string('Your answer: ')

        if resp_user == resp:
            print("Correct!")
            count_win += 1

            if count_win == 3:
                print('Congratulations, {}!'.format(name))
                break
        else:
            count_loss += 1
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(
                resp_user, resp))
            print('Let\'s try again, {}!'.format(name))

            if count_loss == 3:
                print('You have reached the maximum number of attempts.')
                break


def start_game(TASK, logic):
    greetings()
    user_name = prompt_and_get_user_name()
    print(TASK)
    play_roundsss(logic, user_name)
