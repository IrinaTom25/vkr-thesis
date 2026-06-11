from pydantic import BaseModel
from typing import List

class AppConfig(BaseModel):
    app_name: str = "Laboratory FastAPI App"
    app_version: str = "1.0.0"
    app_description: str = "Educational application for laboratory work No. 5"
    app_authors: List[str] = ["IrinaTom25"]

app_config = AppConfig()