import json
import os


def load_quiz():
    files_list = os.listdir(".")
    json_files = [file for file in files_list if file.endswith(".json")]

    print("Available quizzes:")
    for i, file in enumerate(json_files, start=1):
        print(f"{i}. {file}")

    user_choice = input(f"Choose a quiz (1-{len(json_files)}): ")
    if user_choice.isdigit() and int(user_choice) in range(1, len(json_files)+1):
        file = json_files[int(user_choice)-1]
    else:
        raise Exception("Invalid choice")

    with open(file, "r") as f:
        questions = json.load(f)
    return questions


def run_quiz(questions):
    score = 0
    for question in questions:
        print("\nQuestion: " + question["question"])
        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice['choice']}")

        user_answer = input("Enter your answer (1-4): ")
        correct_answer = question["answer"]

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")

    print(f"\nYour final score is {score}/{len(questions)}")


def main():
    try:
        questions = load_quiz()
        run_quiz(questions)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
