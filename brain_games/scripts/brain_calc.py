import random

answer = ("'{}' is wrong answer ;(. Correct answer was '{}'.")


def calc_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print('What is the result of the expression?')

    num_questions = 3
    correct_answers = 0

    for _ in range(num_questions):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        question = "{} {} {}".format(num1, operator, num2)
        correct_answer = str(eval(question))

        print("Question: {}".format(question))
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(answer.format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))


def main():
    calc_game()


if __name__ == '__main__':
    main()
