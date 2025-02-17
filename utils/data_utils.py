import csv

from models.question import Question

def is_duplicate_question(question_id: int, seen_ids: set) -> bool:
    return question_id in seen_ids


def is_complete_question(question: dict, required_keys: list) -> bool:
    return all(key in question for key in required_keys)


def save_question_to_csv(questions: list, filename: str):
    if not questions:
        print("No venues to save.")
        return

    # Use field names from the Venue model
    fieldnames = Question.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(questions)
    print(f"Saved {len(questions)} venues to '{filename}'.")
