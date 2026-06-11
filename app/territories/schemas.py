from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional


class TerritoryBase(BaseModel):
    name: str
    territory_type: str
    level: int = Field(ge=0)
    description: Optional[str] = None
    geom_wkt: str


class TerritoryCreate(TerritoryBase):
    pass


class TerritoryUpdate(BaseModel):
    name: Optional[str] = None
    territory_type: Optional[str] = None
    level: Optional[int] = Field(None, ge=0)
    description: Optional[str] = None
    geom_wkt: Optional[str] = None


class TerritoryRead(BaseModel):
    id: int
    name: str
    territory_type: str
    level: int
    description: Optional[str] = None
    geom_wkt: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TerritoryMetricBase(BaseModel):
    year: int = Field(..., ge=2000, le=2100)
    population: Optional[int] = Field(None, ge=0)
    area_km2: Optional[float] = Field(None, ge=0)
    source: Optional[str] = None


class TerritoryMetricCreate(TerritoryMetricBase):
    pass


class TerritoryMetricUpdate(BaseModel):
    year: Optional[int] = Field(None, ge=2000, le=2100)
    population: Optional[int] = Field(None, ge=0)
    area_km2: Optional[float] = Field(None, ge=0)
    source: Optional[str] = None


class TerritoryMetricRead(BaseModel):
    id: int
    territory_id: int
    year: int
    population: Optional[int] = None
    area_km2: Optional[float] = None
    source: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)