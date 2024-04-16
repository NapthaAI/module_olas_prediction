from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    question: str = Field(..., title="Prediction question")
