from fastapi import APIRouter, Depends
from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from app.schemas.responses import HealthResponse
from app.services.runtime_config import RuntimeConfigService
from app.dependencies import get_app_config, get_runtime_config_service

router = APIRouter(prefix="/config", tags=["Configuration"])

@router.get("/app", response_model=AppConfigModel)
async def get_app_config(
    app_config: AppConfigModel = Depends(get_app_config)
) -> AppConfigModel:
    return app_config

@router.get("/runtime", response_model=RuntimeConfigModel)
async def get_runtime_config(
    service: RuntimeConfigService = Depends(get_runtime_config_service)
) -> RuntimeConfigModel:
    return service.get_config()

@router.put("/runtime", response_model=RuntimeConfigModel)
async def put_runtime_config(
    new_config: RuntimeConfigUpdateModel,
    service: RuntimeConfigService = Depends(get_runtime_config_service)
) -> RuntimeConfigModel:
    return service.update_config(new_config)

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok")