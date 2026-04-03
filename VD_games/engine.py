import prompt

def run_game(game_logic, description):
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)
    
    for _ in range(3):
        question, answer = game_logic()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if str(user_answer) == str(answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f"Congratulations, {name}!")
