import random
from engine import run_game

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = "yes" if number % 2 == 0 else "no"
    return question, answer

def main():
    run_game(generate_round, DESCRIPTION)

if __name__ == "__main__":
    main()
