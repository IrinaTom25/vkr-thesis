from pydantic import BaseModel, Field
from typing import List

class AppConfigModel(BaseModel):
    app_name: str = Field(default="Laboratory FastAPI App", description="Application name")
    app_version: str = Field(default="1.0.0", description="Version")
    app_description: str = Field(default="Educational application for lab 6", description="Description")
    app_authors: List[str] = Field(default=["IrinaTom25"], description="Authors")