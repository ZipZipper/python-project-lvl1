import random

answer = ("'{}' is wrong answer ;(. Correct answer was '{}'.")


def generate_progression(start, step, length):
    progression = []
    current = start
    for _ in range(length):
        progression.append(current)
        current += step
    return progression


def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_value, progression


def progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, {}!".format(name))
    print('What number is missing in the progression?')
    num_questions = 3
    correct_answers = 0

    for _ in range(num_questions):
        prg_length = random.randint(5, 10)
        start_value = random.randint(1, 10)
        step_value = random.randint(1, 10)
        progression = generate_progression(start_value, step_value, prg_length)

        hidden_value, question = hide_element(progression)

        print("Question:", " ".join(map(str, question)))
        user_answer = input("Your answer: ")

        if user_answer == str(hidden_value):
            print("Correct!")
            correct_answers += 1
        else:
            print(answer.format(user_answer, hidden_value))
            print("Let's try again, {}!".format(name))
            return
    print("Congratulations, {}!".format(name))


def main():
    progression_game()
