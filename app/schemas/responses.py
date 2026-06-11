from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(default="ok", description="Server status")

class ErrorResponse(BaseModel):
    detail: str