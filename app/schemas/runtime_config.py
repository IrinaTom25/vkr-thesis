from pydantic import BaseModel, Field
from typing import Literal

class RuntimeConfigModel(BaseModel):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(default="INFO")
    feature_flag: bool = Field(default=True)
    maintenance_mode: bool = Field(default=False)
    runtime_message: str = Field(default="Application is running normally")

class RuntimeConfigUpdateModel(BaseModel):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(default="INFO")
    feature_flag: bool = Field(default=True)
    maintenance_mode: bool = Field(default=False)
    runtime_message: str = Field(default="Application is running normally")