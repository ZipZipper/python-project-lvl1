import random


answer = ("'{}' is wrong answer ;(. Correct answer was '{}'.")


def prim(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    num_questions = 3
    correct_answers = 0

    for _ in range(num_questions):
        number = random.randint(1, 100)

        print("Question:", number)
        an = input("Your answer: ")

        if (an == "yes" and prim(number)) or (an == "no" and not prim(number)):
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = "yes" if prim(number) else "no"
            print(answer.format(an, correct_answer))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))


def main():
    prime_game()
