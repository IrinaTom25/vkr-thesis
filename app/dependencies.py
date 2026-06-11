from fastapi import Depends
from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel
from app.services.runtime_config import RuntimeConfigService

_dependencies = {}

def init_dependencies() -> dict:
    global _dependencies
    
    app_config = AppConfigModel(
        app_name="Laboratory FastAPI App",
        app_version="1.0.0",
        app_description="Educational application for lab 6",
        app_authors=["IrinaTom25"]
    )
    
    initial_runtime = RuntimeConfigModel()
    runtime_service = RuntimeConfigService(initial_runtime)
    
    _dependencies = {
        "app_config": app_config,
        "runtime_config_service": runtime_service,
    }
    
    return _dependencies

def get_app_config() -> AppConfigModel:
    return _dependencies.get("app_config")

def get_runtime_config_service() -> RuntimeConfigService:
    return _dependencies.get("runtime_config_service")