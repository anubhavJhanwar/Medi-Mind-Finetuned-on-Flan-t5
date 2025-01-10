"""
Pydantic schemas for request/response validation.
"""
from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000, example="What is diabetes?")


class AnswerResponse(BaseModel):
    question: str
    base_answer: str
    finetuned_answer: str
    model_loaded: bool = True


class HealthResponse(BaseModel):
    status: str
    base_model_loaded: bool
    finetuned_model_loaded: bool
