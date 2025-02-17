# config.py

BASE_URL = "https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-algebra/?section=1"
CSS_SELECTOR = "[class^='question single-question question-type-normal']"
REQUIRED_KEYS = [
    "id",
    "description",
    "options",
    "correct_answer",
    "solution",
]
