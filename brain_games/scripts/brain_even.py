import random


def is_even(number):
    return number % 2 == 0


def even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    print()

    correct_answers_count = 0
    while correct_answers_count <3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").lower()

        if (is_even(number) and user_answer == "yes") or (not is_even(number) and user_answer == "no"):
            print("Correct!")
            correct_answers_count += 1
        else:
            correct_answer = "no" if is_even(number) else "yes"
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            print()
            return
    print(f"Congratulations, {name}!")

def main():
    even_game()

 
if __name__ == '__main__':
    main()     