from pydantic import BaseModel


class Question(BaseModel):
    """
    Represents the data structure of a question.
    """

    id: str
    description: str
    options: str
    correct_answer: str
    solution: str
