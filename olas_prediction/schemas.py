from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    question: str = Field(..., title="Prediction question")
    prediction_prompt: str = Field(..., title="Prediction prompt")
    system_message: str = Field(default='You are a helpful AI assistant.', title="System Message")
    model: str = Field(..., title="Model name")
    max_tokens: int = Field(..., title="Max tokens")
    temperature: int = Field(..., title="Temperature")
    api_base: str = Field(default='http://localhost:11434', title="API base url")