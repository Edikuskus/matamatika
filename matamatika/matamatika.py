import random

def grade_quiz(score, num_questions):
    percentage = (score / num_questions) * 100
    if percentage < 60:
        return "Hinne 2"
    elif 60 <= percentage < 75:
        return "Hinne 3"
    elif 75 <= percentage < 90:
        return "Hinne 4"
    else:
        return "Hinne 5"

def run_quiz():
    print("Welcome to the Math Quiz!")
    difficulty = int(input("Choose difficulty level (1, 2, or 3): "))
    num_questions = int(input("How many questions do you want to answer? "))

    operations = ['+', '-', '*', '/', '**']
    score = 0

    for _ in range(num_questions):
        operation = random.choice(operations)
        num1 = random.randint(1, difficulty * 10)
        num2 = random.randint(1, difficulty * 10) if operation != '/' else random.randint(1, num1)

        question = f"What is {num1} {operation} {num2}? "
        user_answer = float(input(question)) if operation == '/' else int(input(question))
        
        if eval(f"{num1}{operation}{num2}") == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {eval(f'{num1}{operation}{num2}')}\n")

    grade = grade_quiz(score, num_questions)
    print(f"Quiz completed! Your score: {score}/{num_questions}. Your grade: {grade}")

run_quiz()

