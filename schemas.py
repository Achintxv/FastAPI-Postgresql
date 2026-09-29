from pydantic import BaseModel
from typing import List

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class Choice(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

class Question(BaseModel):
    id: int
    question_text: str
    choices: List[Choice] = []

    class Config:
        from_attributes = True