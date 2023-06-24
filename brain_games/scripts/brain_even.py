import random

answer = (' is wrong answer ;(. Correct answer was ')


def even(number):
    return number % 2 == 0


def even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    correct_answers_count = 0
    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        an = input("Your answer: ").lower()
        if (even(number) and an == "yes") or (not even(number) and an == "no"):
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = "no" if even(number) else "yes"
            print(f"'{an}{answer}{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    even_game()


if __name__ == '__main__':
    main()
