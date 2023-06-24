import random

answer = ("'{}' is wrong answer ;(. Correct answer was '{}'.")


def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def gcd_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print('Find the greatest common divisor of given numbers.')
    num_questions = 3
    correct_answers = 0

    for _ in range(num_questions):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = "{} {}".format(num1, num2)
        correct_answer = str(calculate_gcd(num1, num2))

        print("Question:", question)
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
    gcd_game()
